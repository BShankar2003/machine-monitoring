import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

conn = sqlite3.connect("logs.db")
cursor = conn.cursor()
cursor.execute("SELECT timestamp, status FROM machine_logs")
data = cursor.fetchall()

timestamps = [datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S") for row in data]
status = [1 if row[1] == "RUNNING" else 0 for row in data]

plt.plot(timestamps, status, marker='o')
plt.yticks([0,1], ["DOWN", "RUNNING"])
plt.xlabel("Time")
plt.ylabel("Machine Status")
plt.title("Machine Uptime vs Downtime Log")
plt.show()
