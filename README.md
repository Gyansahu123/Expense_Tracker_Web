# 💰 Expense Tracker Web Application

A secure and user-friendly **Expense Tracker Web Application** built using **Python and Django**. This application helps users track their daily financial activities, visualize spending habits with dynamic charts, and manage expenses efficiently.

It follows the **MVT (Model-View-Template)** architecture and implements full **CRUD (Create, Read, Update, Delete)** operations with secure user authentication.

---

## 🚀 Features

### 🔐 Authentication

- **User Registration & Login:** Secure account creation using Django's built-in authentication system.
- **Data Privacy:** Users can only access and manage their own expense data.

### 📊 Dashboard & Analytics

- **Real-time Summary:** View Total, Today's, and Current Month's expenses instantly.
- **Visual Reports:** Interactive **Doughnut Chart** (using Chart.js) to visualize category-wise spending.
- **Recent Activity:** A list of the 5 most recent transactions.

### 💸 Expense Management

- **Add Expenses:** Log expenses with Amount, Category (Food, Travel, etc.), and Description.
- **Edit/Delete:** Update or remove expense records easily.
- **Date Tracking:** Expenses are automatically timestamped.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (Default) / PostgreSQL (Production ready)
- **Frontend:** HTML5, Bootstrap 5, JavaScript
- **Visualization:** Chart.js
- **Deployment Ready:** Configured with `gunicorn`, `whitenoise`, and `dj-database-url`.

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/Gyansahu123/Expense_Tracker_Web
    cd expense_project
    ```

2.  **Create a Virtual Environment**

    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Migrations**

    ```bash
    python manage.py migrate
    ```

5.  **Run the Server**

    ```bash
    python manage.py runserver
    ```

6.  **Access the App**
    Open your browser and go to: `http://127.0.0.1:8000/`

---

## 📂 Project Structure

```text
expense_project/
│
├── expense_project/    # Project configuration (settings, urls)
├── tracker/            # Main App (models, views, forms)
├── templates/          # HTML Templates (Bootstrap UI)
├── static/             # Static files (CSS, JS for Charts)
├── db.sqlite3          # Local Database
├── manage.py           # Django command-line utility
└── requirements.txt    # Project dependencies
```

---

## 🔮 Future Scope

- 📅 **Date Range Filter:** Export reports for specific dates.
- 📩 **Email Alerts:** Notify users when budget limits are exceeded.
- 📄 **Export Data:** Download expenses as CSV or PDF.

---


