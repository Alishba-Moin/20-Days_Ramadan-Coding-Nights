# Simple API with FastAPI & UV

A lightweight and efficient API built using **FastAPI**, **UV**, and **Python**. This API provides random side hustle ideas and money quotes. It also includes a **count feature** to track the number of available entries.

## 🚀 Features

- **Side Hustles Endpoint**: Get random side hustle suggestions.
- **Money Quotes Endpoint**: Fetch random financial wisdom quotes.
- **Count Endpoint**: Retrieve the total number of side hustles and quotes.
- **FastAPI & UV**: Super-fast performance and automatic API documentation.
- **API Key Security**: Restricted access to endpoints.

## 🛠 Installation & Setup

### 1️⃣ Install UV
Install UV (if not already installed):
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```
For Windows:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Verify installation:
```sh
uv --version
```

### 2️⃣ Create and Initialize the Project
```sh
uv init simple-api
cd simple-api
```

### 3️⃣ Install FastAPI (Dependency)
```sh
uv add fastapi[standard]
```

### 4️⃣ Activate UV Virtual Environment
#### Windows:
```sh
.venv\Scripts\activate
```
#### Linux/macOS:
```sh
source .venv/bin/activate
```

### 5️⃣ Run the API
```sh
fastapi dev main.py
```

## 🔍 Testing the API
Paste the following into your browser:
- **Side Hustles**: [http://127.0.0.1:8000/side_hustles?api_key=1234567890](http://127.0.0.1:8000/side_hustles?api_key=1234567890)
- **Money Quotes**: [http://127.0.0.1:8000/money_quotes?api_key=1234567890](http://127.0.0.1:8000/money_quotes?api_key=1234567890)
- **Count (New Feature)**: [http://127.0.0.1:8000/count?api_key=1234567890](http://127.0.0.1:8000/count?api_key=1234567890)

### Or via Swagger UI:
- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (Interactive API Playground)

## 📌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/side_hustles` | GET | Returns a random side hustle idea |
| `/money_quotes` | GET | Returns a random money quote |
| `/count` | GET | Returns the total count of side hustles and quotes |

## 🛡️ API Security
This API requires an **API Key** for access. The default API key is `1234567890`. Pass it as a query parameter: `?api_key=YOUR_API_KEY`

## 🔥 Why FastAPI?
- **Super Fast** 🚀 – Async support makes it one of the fastest Python frameworks.
- **Auto-Generated Docs** 📜 – Comes with built-in Swagger UI.
- **Easy & Modern** 💡 – Type hints, automatic validation, and dependency injection.

---
💻 **Happy Coding!** 🚀

