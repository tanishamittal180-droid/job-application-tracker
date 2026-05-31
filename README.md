
# 💼 Job Application Tracker

## 📌 Project Overview

The Job Application Tracker is a web-based application that helps job seekers organize, monitor, and manage their job applications efficiently. Instead of tracking applications manually in spreadsheets or notebooks, users can store all application details in one place and monitor their progress through different recruitment stages.

This project is especially useful for students, fresh graduates, and professionals applying to multiple companies simultaneously.

# 🎯 Problem Statement

Job seekers often apply to dozens of companies and struggle to keep track of:

* Applied positions
* Company details
* Application dates
* Interview schedules
* Application status
* Follow-up actions

The Job Application Tracker solves this problem by providing a centralized dashboard to manage all job applications.
# 🚀 Features

### User Features

✅ Add New Job Applications

✅ Update Application Status

✅ Delete Applications

✅ Search Applications

✅ Filter by Status

✅ View Application History

✅ Dashboard Analytics

✅ Track Interview Dates

✅ Track Follow-Ups

✅ Personal Notes Section
# 📊 Application Status Tracking

The system supports multiple statuses:

* Applied
* Under Review
* Interview Scheduled
* Technical Round
* HR Round
* Offer Received
* Rejected
* Accepted

# 🛠️ Technology Stack

### Frontend

* Streamlit
* HTML
* CSS

### Backend

* Python

### Database

* SQLite

### Libraries

* Pandas
* SQLite3
* Streamlit
* Plotly (Optional)

# 🏗️ System Architecture

User Interface
↓
Application Logic
↓
SQLite Database

### Modules

1. Authentication Module
2. Job Application Module
3. Status Management Module
4. Analytics Dashboard
5. Search & Filter Module
# 📂 Project Structure

Job-Application-Tracker/

├── app.py

├── database.py

├── tracker.db

├── assets/

│ └── style.css

├── pages/

│ ├── Dashboard.py

│ ├── Add_Application.py

│ ├── Applications.py

│ ├── Analytics.py

│ └── Profile.py

├── requirements.txt

└── README.md

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/job-application-tracker.git
cd job-application-tracker
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

# 🗄️ Database Schema

## Applications Table

| Column           | Type    |
| ---------------- | ------- |
| id               | INTEGER |
| company          | TEXT    |
| role             | TEXT    |
| location         | TEXT    |
| application_date | DATE    |
| status           | TEXT    |
| interview_date   | DATE    |
| notes            | TEXT    |

---

# 📸 Screenshots

### Home Dashboard

* Overview of total applications
<img width="1366" height="673" alt="Screenshot 2026-05-31 152931" src="https://github.com/user-attachments/assets/647ddf95-c32f-4829-bf5f-febef8aaab23" />

### Add Application Page

* Form to add job applications
<img width="1352" height="641" alt="Screenshot 2026-05-31 153403" src="https://github.com/user-attachments/assets/561b8cc9-28ea-429f-8f02-7ef24407ec9b" />

### Applications Page

* View all applications
<img width="1349" height="620" alt="Screenshot 2026-05-31 153433" src="https://github.com/user-attachments/assets/8e983cf0-0e85-4445-9d4d-079613305e46" />

### Status Tracker

* Monitor recruitment progress
<img width="1363" height="701" alt="Screenshot 2026-05-31 153508" src="https://github.com/user-attachments/assets/2e7952ff-7e9b-4394-9801-03cf6941cf44" />


# 📈 Dashboard Analytics

The dashboard provides:

* Total Applications
* Interviews Scheduled
* Offers Received
* Rejections
* Success Rate
* Monthly Application Trends
# 🔍 Search & Filter

Users can:

* Search by Company Name
* Search by Job Role
* Filter by Status
* Sort by Application Date
# 🔐 Security Features

* User Authentication
* Session Management
* Input Validation
* Database Integrity Checks
# 🎓 Learning Outcomes

This project demonstrates:

* Python Development
* Streamlit Application Development
* Database Design
* CRUD Operations
* Data Visualization
* Dashboard Development
* Project Documentation
* GitHub Project Management

# 🚀 Future Enhancements

* Resume Upload
* Email Notifications
* Interview Reminders
* AI Resume Matching
* LinkedIn Job Integration
* Multi-User Support
* Cloud Deployment
* Mobile Application

# 💡 Real-World Applications

* Students applying for internships
* Fresh graduates searching for jobs
* Professionals managing multiple applications
* Career counseling platforms
* Recruitment tracking systems

# 👨‍💻 Author

Developed as a Full Stack Development and Database Management project for learning and portfolio purposes.
# 📜 License

This project is intended for educational and portfolio use.
