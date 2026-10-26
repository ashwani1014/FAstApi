# 🚀 FastAPI & Python Backend Learning Roadmap

A comprehensive, hands-on repository documenting the step-by-step journey of mastering Python backend development, Object-Oriented Programming (OOP), Pydantic validation, and production-ready FastAPI applications.

---

## 📁 Repository Structure

```text
FAstApI/
├── Week1/
│   ├── Calculator.py                # Interactive Python CLI Calculator
│   ├── DataStructure.py             # Python data transformations & comprehensions
│   ├── Oops_pydantic/
│   │   ├── basicoops.py             # OOP principles (Encapsulation, @property, validations)
│   │   └── pydantic.py              # Pydantic schema validation & FastAPI response models
│   ├── Validation_project/
│   │   ├── validators/              # Modular custom validators (age, price, number)
│   │   │   ├── age_validate.py
│   │   │   ├── number_val.py
│   │   │   └── price_validate.py
│   │   ├── Log_project/             # Structured logging & user service workflow
│   │   │   ├── main.py
│   │   │   └── user_service.py
│   │   └── main.py                  # Validation demo runner
│   └── Crud/
│       └── main.py                  # Full RESTful CRUD API with FastAPI & Pydantic
├── Week2/
│   ├── DynamicParam/                # Path parameters & dynamic routing (in progress)
│   └── QueryParam/
│       └── main.py                  # Query parameters, Enum filters & pagination
├── .gitignore                       # Git ignore rules for Python & virtual environments
└── README.md                        # Project documentation
```

---

## 📚 Curriculum & Modules

### 📅 Week 1: Python Fundamentals, OOP, Validations & First REST API

#### 1. Interactive CLI Calculator (`Week1/Calculator.py`)
- Command-line arithmetic calculator (`+`, `-`, `*`, `/`).
- Input validation and graceful exception handling (`ValueError`, `ZeroDivisionError`).
- Interactive continuous loop with exit command (`q`).
- **Run:**
  ```bash
  python Week1/Calculator.py
  ```

#### 2. Data Transformations & Comprehensions (`Week1/DataStructure.py`)
- Python data manipulation using list and dictionary comprehensions.
- Filtering active records, string normalization (`.strip().title()`), field projections, sorting, and conditional selections.
- **Run:**
  ```bash
  python Week1/DataStructure.py
  ```

#### 3. Object-Oriented Programming & Pydantic (`Week1/Oops_pydantic/`)
- **`basicoops.py`**:
  - Encapsulation using private attributes (`__balance`).
  - Getter properties (`@property`) and methods with business constraint validation (`deposit`, `withdraw`).
  - **Run:** `python Week1/Oops_pydantic/basicoops.py`
- **`pydantic.py`**:
  - Request body validation with `BaseModel`, `Field(min_length, max_length, ge, le)`, and `EmailStr`.
  - Schema separation between input (`UserCreate`) and output (`UserResponse`).
  - FastAPI status codes (`status_code=201`).
  - **Run:** `uvicorn Week1.Oops_pydantic.pydantic:app --reload`

#### 4. Custom Validations & Logging (`Week1/Validation_project/`)
- **Modular Validators (`validators/`)**: Reusable validation functions for age ranges, numeric types, and price bounds.
- **Structured Logging (`Log_project/`)**:
  - Configured `logging.basicConfig` with formatted timestamps, log levels (`INFO`, `ERROR`), and module names.
  - Integration with business service (`user_service.py`).
- **Run:**
  ```bash
  python Week1/Validation_project/main.py
  python Week1/Validation_project/Log_project/main.py
  ```

#### 5. Full RESTful CRUD API (`Week1/Crud/main.py`)
- Complete implementation of RESTful endpoints:
  - `GET /users` — Retrieve all users.
  - `GET /users/{user_id}` — Retrieve user by ID with `404 Not Found` handling.
  - `POST /users` — Create user with duplicate email checks (`409 Conflict`) and Pydantic validation.
  - `PUT /users/{user_id}` — Replace entire user entity.
  - `PATCH /users/{user_id}` — Partial updates with `exclude_unset=True` and null-value guards (`422 Unprocessable Entity`).
  - `DELETE /users/{user_id}` — Remove user with `204 No Content`.
- **Run:**
  ```bash
  uvicorn Week1.Crud.main:app --reload
  ```

---

### 📅 Week 2: Advanced FastAPI Parameters & Routing

#### 1. Query Parameters, Enums & Pagination (`Week2/QueryParam/main.py`)
- Production-ready filtering using string-backed `Enum` classes (`TaskStatus`, `TaskPriority`).
- Type-safe query parameters with default fallbacks and Swagger UI dropdown integration.
- Pagination support with the `limit` query parameter.
- **Run:**
  ```bash
  uvicorn Week2.QueryParam.main:app --reload
  ```

#### 2. Dynamic Path Parameters (`Week2/DynamicParam/`)
- Advanced URL path parameter parsing, converter validations, and nested routing patterns (upcoming).

---

## 🛠️ Getting Started

### 1. Prerequisites
- Python 3.10+
- Virtual environment tool (`venv`)

### 2. Setup Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install fastapi uvicorn pydantic[email]
```

---

## 📖 Interactive API Documentation

FastAPI automatically generates interactive API documentation for running servers:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).
