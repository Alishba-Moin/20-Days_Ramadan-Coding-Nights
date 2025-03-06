# Simple API with FastAPI & UV

This project is a simple API built using **Python**, **FastAPI**, and **UV**. It provides random **side hustle ideas** and **money quotes** to inspire users. The API supports fetching a single item or multiple items using a count parameter.

## 🚀 Features
- **Get Side Hustle Ideas** 💡
- **Fetch Money Quotes** 💰
- **Support for Single or Multiple Entries**
- **FastAPI Auto-generated Docs (Swagger UI)**
- **API Key Security for Restricted Access**

---

## 🔧 Installation & Setup

### 1️⃣ Install UV
Install UV if you haven't already:
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
For **Windows**:
```sh
.venv\Scripts\activate
```
For **Linux/macOS**:
```sh
source .venv/bin/activate
```

### 5️⃣ Run the API Server
```sh
fastapi dev main.py
```

---

##  Usage & Endpoints

###  Get a Random Side Hustle Idea
**Single Result:**
```
GET /side_hustles?api_key=1234567890
```
**Multiple Results (Specify Count):**
```
GET /side_hustles?api_key=1234567890&count=3
```

###  Get a Random Money Quote
**Single Result:**
```
GET /money_quotes?api_key=1234567890
```
**Multiple Results (Specify Count):**
```
GET /money_quotes?api_key=1234567890&count=2
```

###  Test in Swagger UI
You can test the API in Swagger UI:
```
http://127.0.0.1:8000/docs
```

---

##  Example Responses

### **Single Side Hustle Idea**
```json
{
  "side_hustle": "Freelancing - Start offering your skills online!"
}
```

### **Multiple Side Hustles**
```json
{
  "side_hustles": [
    "Dropshipping - Sell without handling inventory!",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Earn by promoting products!"
  ]
}
```

### **Single Money Quote**
```json
{
  "money_quote": "Money is a terrible master but an excellent servant. – P.T. Barnum"
}
```

### **Multiple Money Quotes**
```json
{
  "money_quotes": [
    "If you don’t find a way to make money while you sleep, you will work until you die. – Warren Buffett",
    "Opportunities don’t happen. You create them. – Chris Grosser"
  ]
}
```

---

##  Why FastAPI?
- **Super Fast** – Async support for blazing speed!
- **Auto-Generated Docs** – Built-in Swagger UI for easy API testing.
- **Easy & Modern** – Type hints, validation, and dependency injection.

---

## 📌 License
This project is open-source and free to use! 🎉

