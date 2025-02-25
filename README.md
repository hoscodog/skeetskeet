# 🎯 Skeet Skeet  
**Automated Skeet Shooting Analysis & Performance Metrics**  

---

## 📌 What's the Plan?  
This project aims to allow users to upload skeet shooting scoring metrics and automatically generate:  
✅ Performance insights  
✅ Statistical analysis  
✅ Actionable feedback & improvement suggestions  

We are developing this project to gain **scientific backing** for our historical data while simultaneously tracking the effectiveness of different shooting techniques to determine what works best.  

---

## 🛠️ What Needs to Be Done?  
The initial goal is to process **time-series-based skeet shooting data**, where scores reflect actual skeet shooting results.  

Below are the immediate action steps. As the project evolves, this README and the corresponding Wiki pages should be updated accordingly.  

---

## 📊 **Phase 1: Data Collection & Storage**  

### 🔹 **Record Data**  
- Data will be recorded and stored in **Excel (.xlsx) format**.  
- This format is chosen for **easy editing & cloud storage** (Google Drive).  

### 🔹 **Fetch Data**  
- A **GitHub Actions workflow** will automatically fetch the latest data from Google Drive on a **scheduled basis (TBD).**  
- The raw `.xlsx` data will be processed in **Python** and stored in a **master dataset**.  
- Possible storage solutions:  
  - **PostgreSQL Database** (preferred)  
  - **CSV/JSON** (interim solution before full database integration)  
  - **Google Sheets API** (for real-time editing)  

---

## ⚙️ **Phase 2: Data Processing & Analysis**  

### 🔹 **Processing Workflow**  
- The scheduled workflow will:  
  ✅ Retrieve & normalize the latest data  
  ✅ Append it to the master dataset  
  ✅ Perform **data integrity checks** (missing entries, incorrect formats, etc.)  

### 🔹 **Data Analysis**  
- Key analytics to be performed:  
  ✅ **Basic Stats**: Average score per round, station accuracy breakdown, trends over time  
  ✅ **Performance Trends**: Identifying weaknesses & strengths at specific stations  
  ✅ **Anomaly Detection**: Detect inconsistencies or potential scoring errors  
  ✅ **Predictive Analytics (Future Expansion)**: Machine learning-based score predictions  

---

## 📑 **Phase 3: Report Generation & Publishing**  

### 🔹 **Generate Reports**  
- Reports will be generated as **PDFs, HTML documents, or Markdown summaries**.  
- Reports will include:  
  ✅ Performance trends  
  ✅ Station-specific insights  
  ✅ Suggested drills & improvement areas  

### 🔹 **Publish Data**  
- Reports will be **accessible via:**  
  ✅ **GitHub Actions Artifacts** (initial method)  
  ✅ **Automated Email Reports** (future expansion)  
  ✅ **Web Dashboard** (long-term goal)  
  ✅ **Project Badges** (showing results for Ian & Grant)  

---

## 🚀 **Future Considerations & Expansions**  
🔹 **Machine Learning Integration**: Predict score trends based on historical data  
🔹 **Interactive Web Dashboard**: UI to visualize shooting performance over time  
🔹 **IoT Sensor Data**: Integration with electronic shooting trainers  
🔹 **Mobile App**: For real-time score logging & analysis  

---

## 📅 **Next Steps**  
🔹 Finalize database schema for structured storage  
🔹 Define key performance metrics for analysis  
🔹 Build the first data pipeline (Google Drive → Database → Report)  
🔹 Automate the first report generation & evaluate results  

---

📢 **Stay tuned for updates as this project evolves!** 🎯  
