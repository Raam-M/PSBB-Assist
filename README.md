# 🖥️ PSBB Assist – Teacher Utility Desktop Application

**PSBB Assist** is a desktop application built with **Python (Tkinter)** and **MySQL** to assist educators in digitizing and managing classroom workflows. It provides a structured interface for recording **session summaries**, maintaining **anecdotal records**, and capturing **student attendance**, helping streamline routine administrative tasks in educational institutions.

---

## 📌 Features

### 📚 Session Log
- Record and manage summaries for each teaching session.
- Search and update logs by date, class, and subject.

### 📝 Anecdotal Records
- Capture positive or negative observations about students.
- Maintain a searchable, class-wise log of anecdotal inputs.

### 📅 Attendance Management
- Mark and update daily attendance by selecting absentees.
- Retrieve historical attendance data by date and class.

---

## 🛠️ Tech Stack

| Component     | Description                         |
|---------------|-------------------------------------|
| **Frontend**  | Python with Tkinter GUI             |
| **Backend**   | MySQL (via `mysql-connector-python`)|
| **Libraries** | `tkcalendar`, `PIL`, `datetime`, `ttk`|

---

## 🗂️ Project Structure
<pre lang="markdown"><code>
PSBB-Assist/
├── View/
│   ├── main.py             # Main UI and routing logic
│   ├── anecdata.py         # Anecdotal records logic
│   ├── attendance.py       # Attendance module
│   ├── sessionlog.py       # Session logging logic
│   ├── student.py          # Student DB access
│   ├── classconfig.py      # Class/subject configuration
│   ├── dbconfig.py         # DB connection configuration
├── DBScript/
│   └── DBScript.sql        # MySQL schema and seed data
├── Image/
│   └── psbblogo.jpg        # Application logo
└── README.md               # Project documentation
</code></pre>


---

## 🗃️ Database Overview

### Core Tables
- `sessionlog`: Stores class-wise session notes.
- `anecdote`: Stores categorized observations about students.
- `attendance`: Records daily absentees.
- `student`, `teacher`, `classconfig`, `classsubject`, `studentclass`, `subject`: Supporting and master data tables.

### Views Used
- `vw_anecdote`
- `vw_studentclass`
- `vw_attendstudclass`
- `vw_sesslogsubject`
- `vw_classsubject`

---

## ✅ Key Functional Highlights

- Modular Python backend with logical separation of concerns
- Clean and intuitive UI using **Tkinter** widgets and calendar pickers
- Live integration with **MySQL**, with support for insert, update, and query operations
- Maintains application state across modules (e.g., class lists, student data)
- Feedback and save confirmation via popup dialogs

---

## 🚧 Limitations

- Currently available only as a **desktop application**
- No user authentication implemented
- Designed with support for three key modules; extensible but limited in scope

---

## 🚀 Future Enhancements

- Transition to a **web-based platform** using Django or Flask
- Add features like:
  - Exam grading and report card generation
  - Notification/reminder system for assignments
  - Syllabus planning dashboard
  - User login and role-based access control

---

## 📚 References

- [MySQL Connector Python Documentation](https://dev.mysql.com/doc/connector-python/en/)
- [Tkinter Tutorials – GeeksforGeeks](https://www.geeksforgeeks.org/python-tkinter-tutorial/)
- [Codemy YouTube Series on Tkinter](https://youtu.be/YTqDYmfccQU)

---

## 👨‍💻 Author

**Raam M**
Developer & Contributor
Feel free to reach out for suggestions, feedback, or collaboration opportunities.

---
