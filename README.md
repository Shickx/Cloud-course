# Azure Practice 2 – FastAPI + Azure SQL

This project is a FastAPI application connected to an Azure SQL Database.  
It demonstrates basic CRUD operations across multiple services using separate schemas.

---

## 🧱 Architecture

The project is split into 3 services:

### 👨‍🍳 Chef Service
Handles chefs data:
- Get all chefs
- Get chef by ID
- Create chef

### 📦 Class Service
Handles cooking classes:
- Get all classes
- Create class
- Get bookings for a class

### 💬 Feedback Service
Handles feedback:
- Get all feedbacks
- Create feedback

---

## 🗄️ Database Structure (Azure SQL)

Schemas used:

- `s20230535_chefs`
- `s20230535_classes`
- `s20230535_feedbacks`

### Tables:

- chefs.chef
- classes.class
- classes.booking
- feedbacks.feedback

---

## 🚀 How to run locally

### 1. Activate virtual environment
```bash
.\venv\Scripts\activate

2. Install dependencies

pip install -r requirements.txt

3. Initialize database (run once)

python init_db.py

4. Start server

uvicorn main:app --reload
