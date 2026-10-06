# 🛒 MinimalShop - E-Commerce Platform with Django & Bootstrap

A sleek, lightweight, and robust e-commerce web application built with **Django 6** and designed using **Bootstrap 5**. This project features a complete purchase flow, real-time inventory management, and a custom customer authentication system independent of the Django admin panel.

## ✨ Core Features
- **Dynamic Catalog:** Instant product filtering based on store categories.
- **Interactive Shopping Cart:** Full-featured, session-backed local cart that allows users to increment, decrement, and remove items with automated total recalculations.
- **Inventory Control:** Automatic stock deduction from the database immediately after a purchase is successfully simulated.
- **Independent Authentication:** Custom Registration, Login, and secure POST-based Logout screens tailored specifically for standard customers.
- **Optimized Performance:** All Bootstrap static files (CSS/JS) are served 100% locally, eliminating third-party CDN dependencies and securing lightning-fast load times.

## 🛠️ Tech Stack
- **Backend:** Python / Django 6
- **Frontend:** Bootstrap 5 (Local)
- **Database:** SQLite (Development environment)
- **Production Server:** Gunicorn / Uvicorn

## 🚀 Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd TiendaOnline
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply database migrations and launch the local server:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
   Open [http://127.0.0] in your web browser.

---
*Developed as a modern e-commerce project following clean architecture patterns in Django.*
