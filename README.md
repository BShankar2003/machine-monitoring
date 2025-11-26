

# 📄 **README.md** — Machine Monitoring & Reliability Analysis (CIM Project)

```md
# 🔧 Machine Monitoring System (CIM-Inspired Project)
A real-time equipment monitoring simulation inspired by **semiconductor FAB CIM (Computer Integrated Manufacturing)** environments.  
The system logs machine uptime/downtime, analyses failure patterns, generates reliability metrics like **MTBF, MTTR, Availability**, and visualizes performance data.

This project was built to replicate how chip manufacturing fabs monitor tool performance, detect faults, and ensure continuous production stability.

---

## 🚀 Features

| Feature | Status | Description |
|---|---|---|
| Real-time machine status logging | ✅ | Simulates RUNNING/DOWN states every cycle |
| SQLite log storage | ✅ | Data saved for long-term trend analysis |
| Uptime vs Downtime graph | 📈 | Visual breakdown with Matplotlib |
| KPI summary analytics | 📊 | Generates uptime %, downtime %, streak lengths |
| MTBF / MTTR / Availability | ⭐ | Industry-standard fab reliability metrics |

---

## 🏗 Tech Stack

| Component | Tools Used |
|---|---|
| Programming | Python |
| Database | SQLite |
| Visualization | Matplotlib |
| Metrics Engine | Custom Calculations (MTBF, MTTR, Availability) |

---

## 📂 Directory Structure

```

machine-monitoring/
│── machine_monitor.py        # Real-time status generator
│── analyze_logs.py           # Visualizes uptime/downtime trend graph
│── summary_report.py         # Uptime %, Downtime %, failures, streaks
│── reliability_metrics.py    # MTBF, MTTR & Availability calculation
│── logs.db                   # Auto-generated SQLite database
│── README.md                 # Documentation (you are reading this)

````

---

## 🔥 How to Run the Project (Execution Order)

### **1. Start Real-Time Monitoring**
This script creates logs continuously.

```bash
python machine_monitor.py
````

Keep it running for a minute or more → Press `CTRL + C` to stop.

### **2. Generate Performance Graph**

```bash
python analyze_logs.py
```

You will see a graph illustrating uptime vs downtime.

### **3. Generate Uptime Summary Metrics**

```bash
python summary_report.py
```

Produces:

```
Uptime %, Failures, Streaks
```

### **4. Generate Reliability KPI (FAB-Grade)**

```bash
python reliability_metrics.py
```

Outputs:

```
MTBF, MTTR, Availability %
```

---

## 📊 Sample Output

```
========== MACHINE PERFORMANCE SUMMARY ==========
Total Log Entries       : 68
Uptime %                : 54.41%
Downtime %              : 45.59%
Failure Events Detected : 15
Longest Uptime Streak   : 5 cycles
Longest Downtime Streak : 6 cycles
=================================================
```

```
========== EQUIPMENT RELIABILITY METRICS ==========
Mean Time Between Failures (MTBF) : 45.07 sec
Mean Time To Repair (MTTR)        : 0.00 sec
Equipment Availability            : 100.00%
===================================================
```

---

## 🎯 Why This Project Matters

This system simulates core semiconductor automation concepts:

✔ Failure detection
✔ Realtime equipment monitoring
✔ Production reliability metrics
✔ KPI-driven performance analysis

Perfect discussion point for interviews — especially CIM roles at **Tata Electronics / Semiconductor Fab roles**.

---

## 🏁 Project Completed By

**Shankar Subhan Singh Bondili**
📧 [shankarsingh.job@gmail.com](mailto:shankarsingh.job@gmail.com)
🔗 GitHub: [https://github.com/BShankar2003](https://github.com/BShankar2003)

