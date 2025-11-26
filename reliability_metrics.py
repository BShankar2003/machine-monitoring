import sqlite3
from datetime import datetime

# Connect to DB
conn = sqlite3.connect("logs.db")
cursor = conn.cursor()
cursor.execute("SELECT timestamp, status FROM machine_logs")
rows = cursor.fetchall()

if len(rows) < 2:
    print("Not enough data to compute reliability metrics.")
    exit()

# Convert timestamps into datetime objects
logs = [(datetime.strptime(t, "%Y-%m-%d %H:%M:%S"), s) for t, s in rows]

# Identify failure (RUNNING→DOWN) and recovery (DOWN→RUNNING)
failure_times = []
repair_times = []

for i in range(1, len(logs)):
    prev_time, prev_status = logs[i-1]
    curr_time, curr_status = logs[i]

    # Failure event
    if prev_status == "RUNNING" and curr_status == "DOWN":
        failure_times.append(curr_time)

    # Recovery event
    if prev_status == "DOWN" and curr_status == "RUNNING":
        repair_times.append(curr_time)

# ============================  MTTR (MEAN TIME TO REPAIR)  ============================

pairs = min(len(failure_times), len(repair_times))
downtime_durations = []

for i in range(pairs):
    downtime = (repair_times[i] - failure_times[i]).total_seconds()

    if downtime > 0:  # Avoid negative MTTR
        downtime_durations.append(downtime)

MTTR = (sum(downtime_durations) / len(downtime_durations)) if downtime_durations else 0

# ============================  MTBF (MEAN TIME BETWEEN FAILURES) ============================

if len(failure_times) > 1:
    failure_intervals = []
    for i in range(1, len(failure_times)):
        diff = (failure_times[i] - failure_times[i-1]).total_seconds()
        if diff > 0:
            failure_intervals.append(diff)

    MTBF = sum(failure_intervals) / len(failure_intervals) if failure_intervals else 0
else:
    MTBF = 0

# ============================  AVAILABILITY CALCULATION  ============================

if MTBF + MTTR > 0:
    availability = (MTBF / (MTBF + MTTR)) * 100
else:
    availability = 0

# Ensure % never exceeds valid range
availability = min(max(availability, 0), 100)

# ============================ FINAL OUTPUT ============================

print("\n========== EQUIPMENT RELIABILITY METRICS ==========")
print(f"Mean Time Between Failures (MTBF) : {MTBF:.2f} sec")
print(f"Mean Time To Repair (MTTR)        : {MTTR:.2f} sec")
print(f"Equipment Availability            : {availability:.2f}%")
print("===================================================\n")
