import sqlite3
from datetime import datetime

# Connect DB
conn = sqlite3.connect("logs.db")
cursor = conn.cursor()

# Fetch log data
cursor.execute("SELECT timestamp, status FROM machine_logs")
rows = cursor.fetchall()

if not rows:
    print("No data found. Run machine_monitor.py first.")
    exit()

# ---- Stats Processing ----
total = len(rows)
running_count = sum(1 for (_, s) in rows if s == "RUNNING")
down_count = total - running_count

uptime_percent = (running_count / total) * 100
downtime_percent = (down_count / total) * 100

# Detect number of failure events + longest streaks
failures = 0
current_up = current_down = 0
max_up = max_down = 0

for _, status in rows:
    if status == "RUNNING":
        current_up += 1
        max_up = max(max_up, current_up)
        current_down = 0
    else:
        current_down += 1
        max_down = max(max_down, current_down)
        current_up = 0

# Failures counted when DOWN follows RUNNING
for i in range(1, len(rows)):
    if rows[i][1] == "DOWN" and rows[i-1][1] == "RUNNING":
        failures += 1

# ---- Final Summary Output ----
print("\n========== MACHINE PERFORMANCE SUMMARY ==========")
print(f"Total Log Entries       : {total}")
print(f"Uptime %                : {uptime_percent:.2f}%")
print(f"Downtime %              : {downtime_percent:.2f}%")
print(f"Failure Events Detected : {failures}")
print(f"Longest Uptime Streak   : {max_up} cycles")
print(f"Longest Downtime Streak : {max_down} cycles")
print("=================================================\n")
