import random
from fastapi import FastAPI

app = FastAPI()

jokes = [
    {"id": 1, "type": "programming", "setup": "Manager: Bhai code optimize karo!", "punchline": "Developer: Bhai pehlay optimize ho chuka hai, ab error fix kar raha hoon. 😭"},
    {"id": 2, "type": "programming", "setup": "Interviewer: Tum React jaante ho?", "punchline": "Me: Haan React ka tutorial 3 baar dekh chuka hoon! 😎"},
    {"id": 3, "type": "programming", "setup": "Backend Developer: API ban gayi! 🏆", "punchline": "Frontend Developer: Bhai iska UI kidhar hai? 😵"},
    {"id": 4, "type": "programming", "setup": "Python Developer: Python easy hai!", "punchline": "Java Developer: Achaaaa? Phir 'self' likhne ka kya scene hai? 🤣"},
    {"id": 5, "type": "programming", "setup": "SQL query likhna aasan hai?", "punchline": "Me: SELECT * FROM `brain` WHERE `knowledge` > `sleep` 😴🤯"},
    {"id": 6, "type": "programming", "setup": "Intern: Bhai yeh 'this' kya hota hai JavaScript mai?", "punchline": "Senior Dev: Yeh woh hai jo har developer ki life ko mushkil banata hai! 😆"},
    {"id": 7, "type": "programming", "setup": "Frontend Developer: UI ready hai!", "punchline": "Backend Developer: Bhai API thoda slow hai... Spinner daal dete hain! 😂"},
    {"id": 8, "type": "programming", "setup": "Me debugging at 2 AM:", "punchline": "if (bug) { sleep = false; } 😭"},
    {"id": 9, "type": "programming", "setup": "Me: Laptop thoda slow ho raha hai!", "punchline": "Task Manager: 'Google Chrome 37 tabs open, RAM 98% used' 😵💀"},
    {"id": 10, "type": "programming", "setup": "Me: Yaar aik aur framework seekhna hai!", "punchline": "React, Next.js, Vue, Angular, Svelte: 'Humein bhi seekh lo na!' 🥺"}
]

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Pakistani Coding Jokes API! Use /joke for a random joke, /all-jokes for all jokes."
    }

@app.get("/jokes")
def get_random_joke():
    '''Returns a random jokes'''
    return {"Jokes": random.choice(jokes)}
