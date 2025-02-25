# Skeet Skeet
Automated Skeet shooting analysis of general performance metrics and report generation.

## What's the Plan?
This project aims to allow users to upload skeet shooting scoring metrics and automatically provide performance insights, trend analysis, and actionable feedback through statistical analysis and report generation.

The goal is to use data-driven methods to analyze shooting performance over time, comparing different shooting techniques and providing insights into what works best.

## What Needs to Be Done?
The project will be built in several phases, starting with basic data ingestion and moving towards full statistical analysis, reporting, and automated feedback.

As the project evolves, this README and the corresponding Wiki pages should be updated to reflect the current project status.

## Phase 1: Data Collection and Storage
### Recording Data
#### Format:
Data will be recorded in Excel (.xlsx) format.

#### Storage Location:
Google Drive (for easy access and versioning).

#### Data Structure Considerations:

Date of session

Shooter name

Round number

Station-by-station hit/miss results

Environmental factors (weather, wind, lighting conditions, etc.)

Firearm & ammo type used (optional but useful for deeper insights)


### Fetching Data from Google Drive
#### Automation
A GitHub Actions workflow will fetch the latest data from Google Drive on a scheduled basis.

#### Transformation
The raw .xlsx data will be cleaned and formatted using Python.

#### Storage Options:
PostgreSQL (preferred for structured storage and querying)

CSV/JSON files (as an interim solution before full database integration)

Google Sheets API (if real-time collaborative editing is needed)


## Phase 2: Data Processing and Analysis
#### Data Processing Workflow
The scheduled workflow will:

Retrieve and normalize the latest data.

Append it to the master dataset in PostgreSQL (or another storage format).

Perform data integrity checks (detect missing entries, incorrect formats, etc.).

#### Data Analysis
The system will process the master dataset to compute:

✅ Basic Statistics: Average score per round, station accuracy breakdown, trends over time.

✅ Performance Trends: Identify strengths/weaknesses at specific stations or conditions.

✅ Anomaly Detection: Identify inconsistencies or potential scoring errors.

✅ Predictive Analytics (future expansion): Machine learning-based score prediction models.

## Phase 3: Report Generation and Publishing
#### Report Generation
Reports will be generated as PDFs, HTML, or Markdown files.

#### Report Contents
Overall performance trends.

Station-specific strengths and weaknesses.

Suggested drills or improvements based on trends.

#### Data Access and Publishing
We will explore multiple ways to access the reports:

✅ GitHub Actions Artifacts (initial method)

✅ Project Badges (for tracking Ian and Grant’s results at a glance)

✅ Email Reports (automated email notifications)

✅ Web Dashboard (future expansion)

## Potential Future Features
🚀 Machine Learning Integration: Predict score trends based on historical data.

📊 Interactive Web Dashboard: A UI to explore results dynamically.

📡 IoT Sensor Data: Integration with electronic shooting trainers. (This is for you Ian)

📱 Mobile App: For real-time score logging and analysis.

## Next Steps
Finalize the database schema for efficient storage and retrieval.

Define the first set of analysis metrics (what insights are most valuable?).

Implement the first version of the data pipeline (from Google Drive → Database → Report).

Automate the first report generation and evaluate output.


