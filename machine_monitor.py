import sqlite3
import time
import random
from datetime import datetime
from config import CHECK_INTERVAL, DOWNTIME_ALERT_THRESHOLD

# DB setup
conn = sqlite3.connect("logs.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS machine_logs (
        timestamp TEXT,
        status TEXT
    )
""")

prev_down_start = None

def log_status():
    global prev_down_start

    status = random.choice(["RUNNING", "DOWN"])  # machine simulation
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("INSERT INTO machine_logs VALUES (?, ?)", (timestamp, status))
    conn.commit()

    print(f"[{timestamp}] Machine Status → {status}")

    # Check downtime alert
    if status == "DOWN":
        if prev_down_start is None:
            prev_down_start = time.time()
        elif time.time() - prev_down_start >= DOWNTIME_ALERT_THRESHOLD:
            print("⚠ ALERT: Machine down for too long! Escalate to engineering team.")
    else:
        prev_down_start = None

if __name__ == "__main__":
    print("🔍 Starting Machine Monitoring System...")
    while True:
        log_status()
        time.sleep(CHECK_INTERVAL)
