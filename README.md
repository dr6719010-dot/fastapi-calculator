# calculator-api

my first project that actually worked lol

a full stack calculator built with FastAPI on the backend and vanilla JS on the frontend. you type numbers, pick an operation, hit calculate — it calls a real API and gives you the result. nothing crazy, but it's mine and it runs.

---

## what it does

- **4 operations** — sum, product, difference, division
- **input validation** — handles empty lists, division by zero, wrong data types
- **recent history** — tracks your last 5 calculations
- **auto-generated API docs** at `/docs` (FastAPI does this for free)

---

## tech stack

| Layer | Tech |
|-------|------|
| Backend | Python, FastAPI |
| Validation | Pydantic |
| Frontend | HTML, CSS, Vanilla JS |
| Server | Uvicorn |
| Version Control | Git + GitHub |

---

## how to run it

**1. clone the repo**
```bash
git clone https://github.com/dr6719010-dot/calculator-api.git
cd calculator-api
```

**2. install dependencies**
```bash
pip install fastapi uvicorn
```

**3. start the backend**
```bash
uvicorn main:app --reload
```

**4. open the frontend**

just open `index.html` in your browser. that's it.

API runs on `http://127.0.0.1:8000`
Docs available at `http://127.0.0.1:8000/docs`

---

## project structure

```
calculator-api/
├── main.py          # FastAPI routes
├── calculator.py    # core logic (sum, product, difference, division)
├── models.py        # Pydantic request model
├── index.html       # frontend UI
└── .gitignore
```

---

## API endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | health check |
| POST | `/calculate` | runs a calculation |
| GET | `/history` | returns last 3 calculations |

**example request:**
```json
POST /calculate
{
  "operation": "sum",
  "numbers": [10, 20, 30]
}
```

**example response:**
```json
{
  "operation": "sum",
  "result": 60
}
```

---

## what i learned building this

- how to structure a backend API with FastAPI
- git from scratch — init, commit, push, the whole thing
- HTTP methods, status codes, CORS
- connecting a frontend to a real backend
- pydantic validation and why it matters

---

built by [DR4VEN](https://github.com/dr6719010-dot) · pre-college, aspiring backend/devops engineer
## Logarithm Operations

CalcX now supports logarithmic calculations with dynamic base selection.

### Features
- Supports custom logarithm bases
- Handles natural logarithms (`base e`)
- Input validation for invalid log operations
- Dynamic interface rendering for log-specific inputs
- Proper exception handling for mathematical edge cases

### Example Request

```json
{
  "operation": "log",
  "number": 100,
  "base": 10
}