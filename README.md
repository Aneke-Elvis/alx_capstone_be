# Trading Dashboard Backend API

## 📌 Project Overview

This project is the **backend service** for a Trading Dashboard application built as part of the **ALX Capstone Project**. The backend provides RESTful APIs that power trading-related features such as portfolio management, trade tracking, asset information, and price alerts.

The backend is implemented using **Django**, **Django REST Framework**, and **MySQL**, following best practices in API design, authentication, and data modeling.

---

## 🎯 Project Objectives

* Design a clean and scalable backend architecture
* Implement a well-structured database using an ERD
* Expose RESTful API endpoints for frontend consumption
* Handle authentication and user-specific data securely
* Demonstrate backend engineering skills using Django & DRF

---

## 🛠️ Tech Stack

* **Backend Framework:** Django
* **API Framework:** Django REST Framework (DRF)
* **Database:** SQLite (development)
* **Authentication:** Django Authentication (Session / Token-based)
* **Language:** Python 3
* **Version Control:** Git & GitHub

---

## 🗂️ Project Structure

```
trading_dashboard_backend/
│
├── trading_dashboard/        # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── trading/                  # Core trading app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── users/                    # User-related extensions (future use)
│   └── models.py
│
├── manage.py
└── README.md
```

---

## 🧩 Database Design (ERD Summary)

### Entities

* **User** (Django built-in)
* **Asset**
* **Portfolio**
* **Trade**
* **Alert**

### Relationships

* A **User** has one **Portfolio** (1:1)
* A **User** can create many **Trades** (1:M)
* An **Asset** can be associated with many **Trades** (1:M)
* A **User** can create many **Alerts** (1:M)
* An **Asset** can have many **Alerts** (1:M)

The ERD diagram is included in the project documentation (Google Doc) as required by the capstone guidelines.

---

## 🔌 API Endpoints Overview

### Authentication

### Assets

* `GET /api/trading/assets/` – List all tradable assets
* `GET /api/trading/assets/{id}/` – Retrieve asset details

### Portfolio

* `GET /api/trading/portfolio/{id}` – Retrieve user portfolio

### Trades

* `GET /api/trading/trades/` – List user trades
* `POST /api/trading/trades/` – Create a new trade

### Alerts

* `GET /api/trading/alerts/` – List price alerts
* `POST /api/trading/alerts/` – Create a new alert

> Authentication is planned but not enforced at this stage.

---

## 🚀 Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Aneke-Elvis/alx_capstone_be.git
cd alx_capstone_be
```

### 2️⃣ Create Virtual Environment

```bash 
python -m venv .venv

activate virtual environment
.env\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Update database credentials in `settings.py`:

```python
DATABASES = {
    'default': {
        'NAME': 'trading_db',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 7️⃣ Start Development Server

```bash
python manage.py runserver
```

---

## ✅ Current Progress (Capstone – Part 3)

* Project setup completed
* Core models implemented
* ERD designed and documented
* REST API endpoints working and consumed by frontend
* Repository initialized and pushed to GitHub

---

## Frontend Respository link
 * Frontend Repository: https://github.com/Aneke-Elvis/alx_capstone_fe

## ⚠️ Challenges Faced

* Clarifying entity relationships in the ERD
* Deciding between One-to-One vs One-to-Many relationships
* Structuring apps for scalability

These challenges were resolved by refining the ERD and aligning it strictly with project requirements.

---

## 🔜 Next Steps

* Complete CRUD operations for all entities
* Add authentication and permissions
* Write unit tests
* Improve API documentation
* Prepare final demo video

---

## 👨‍💻 Author

**Name: Aneke Elvis**

Built as part of the **ALX Software Engineering Capstone Project**.

---

## 📄 License

This project is for educational purposes only.
