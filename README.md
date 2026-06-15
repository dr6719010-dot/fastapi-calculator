# CalcX 🚀

A full-stack calculator web application built with FastAPI, Vanilla JavaScript, and SQLite.

## 🌐 Live Demo

**Frontend:**
https://calcx-jhx4.onrender.com/app

**API Documentation:**
https://calcx-jhx4.onrender.com/docs

---

## ✨ Features

* Addition
* Subtraction
* Multiplication
* Division
* Logarithms
* Calculation history tracking
* SQLite database persistence
* REST API endpoints
* Interactive Swagger documentation
* Responsive web interface

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* SQLite
* Uvicorn

### Frontend

* HTML
* CSS
* Vanilla JavaScript

### Deployment

* Render

---

## 📡 API Endpoints

| Method | Endpoint     | Description           |
| ------ | ------------ | --------------------- |
| GET    | `/`          | Health Check          |
| GET    | `/app`       | Frontend Interface    |
| GET    | `/history`   | Calculation History   |
| POST   | `/calculate` | Perform Calculations  |
| GET    | `/docs`      | Swagger Documentation |

---

## Example Request

```json
{
  "numbers": [5, 2],
  "operation": "division"
}
```

## Example Response

```json
{
  "operation": "division",
  "result": 2.5
}
```

---

## 🚀 Running Locally

```bash
git clone https://github.com/dr6719010-dot/fastapi-calculator.git

cd fastapi-calculator

pip install -r requirements.txt

uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/app
```

---

## 📚 What I Learned

* Building REST APIs using FastAPI
* Creating custom exception handling
* Working with SQLite databases
* Logging and debugging techniques
* Frontend-backend integration
* Git and GitHub workflows
* Cloud deployment and hosting
* Debugging production issues
* Troubleshooting API routing and networking problems

---

## 📈 Project Status

✅ Live and deployed

---

## 👨‍💻 Author

**Digvijay Rana**
