# 📝 To-Do App

A feature-rich, modern To-Do application built using **Flask**, **Bootstrap**, and **JavaScript**, designed to manage tasks effectively with advanced functionalities like categories, priorities, due dates, drag-and-drop sorting, CSV export, and dark mode.

---

## 🚀 About the Project

This To-Do App helps users keep track of their daily tasks with a clean and intuitive interface. It supports full CRUD operations, task filtering, user authentication, and additional productivity-enhancing features. Designed with both beginner and advanced developers in mind, it demonstrates how a real-world Flask application is structured and scaled.

---

## 💡 How to Approach this Project

1. **Understand the Structure**:
   - Backend: Flask + Flask-SQLAlchemy + Flask-Login
   - Frontend: Jinja Templates + Bootstrap 5 + JavaScript (optionally Vue 2)
   - REST API: Flask-RESTful for async data interactions

2. **Set Up Environment**:
   - Create a virtual environment:  
     `python -m venv venv`
   - Install dependencies:  
     `pip install -r requirements.txt`

3. **Run the App**:
   - Set environment variables:
     ```bash
     export FLASK_APP=app.py
     export FLASK_ENV=development
     ```
   - Run the app:  
     `flask run`

4. **Explore Features**:
   - Register/Login to access dashboard
   - Add, edit, delete, and filter tasks
   - Try out advanced features like drag-and-drop, CSV export, and dark mode

---

## 🛠 Tools & Technologies Used

### Backend:
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-RESTful Api

### Frontend:
- HTML, CSS, Bootstrap 5
- JavaScript (ES6+)
- Jinja Templating
- Vue 2 (optional for drag-and-drop UI)

### Database:
- SQLite (default, easy to set up)
- PostgreSQL (for production-ready deployment)

---

## ✅ Key Features

- User Registration and Authentication
- Create, Read, Update, Delete (CRUD) Tasks
- Filter Tasks: All, Completed, Pending
- Mark Tasks as Completed
- Task Priorities (Low, Medium, High)
- Due Date Selector
- Task Categories
- Flash Messaging and Alerts
- Responsive UI using Bootstrap 5

---

## 🌟 Advanced Features

- 🌓 **Dark Mode** (persistent using `localStorage`)
- 🔃 **Drag & Drop Sorting** (using JavaScript or Vue 2)
- 📁 **Export Tasks to CSV**
- 🔍 **Search, Sort, and Pagination**
- 📡 **Async REST API** with `Flask-RESTful` + `Fetch API`
- 📂 Filter by Category, Priority, and Status
- 📅 Optional Due Date Reminders (in roadmap)

---

## 🐛 Known Issues & Log

| Issue ID | Description | Status |
|----------|-------------|--------|
| #001 | Drag-and-drop sorting sometimes doesn't persist on slow connections | ❗ Pending |
| #002 | Dark mode affects navbar text visibility | ✅ Fixed |
| #003 | Exported CSV not respecting current task filters | ❗ Pending |
| #004 | Pagination breaks when search query is empty | ✅ Fixed |
| #005 | API routes need authentication middleware for security | ⚠️ In progress |

---

## 🙌 Contributions

This project is a great starting point for beginners learning full-stack Flask apps. You're welcome to contribute by fixing bugs, improving UI/UX, or adding new features.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---
