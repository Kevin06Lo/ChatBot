# 💬 Drax Chatbot

A simple rule-based chatbot built in Python that can remember your name, hold basic conversations, and respond to user intents defined in a JSON file.

---

## 🚀 Features

- Rule-based conversation system using regex patterns.
- Memory system that remembers your name across sessions.
- JSON-based intent configuration for flexible conversation design.
- Modular project structure (easy to extend and maintain).
- Runs in a virtual environment.

---

## 🗂️ Project Structure

```bash
ChatBot/
│
├── data/
│ ├── intents.json # Conversation patterns and responses
│ └── memory.json # Stores user memory (e.g., name)
│
├── src/
│ ├── init.py
│ ├── chatbot.py # ChatBot class definition
│ └── main.py # Entry point logic for the chatbot
│
├── run.py # Script to start the chatbot
├── requirements.txt # Dependencies
├── .gitignore # Files and folders ignored by Git
└── README.md # You are here
```
---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/ChatBot.git
   cd ChatBot
2. **Create Virtual environment**
    ```bash
    python -m venv venv
3. **Activate it**
    ```bash
    on Windows (PowerShell):
        venv\Scripts\activate
    on Mac/Linux
        source venv/bin/activate
4. **Install dependencies**
    ```bash
    pip install -r requirements.txt
5. **Start your chatbot by running**
    ```bash
    python run.py

    Example conversation:
        Drax: Hello! Type exit to quit.

        You: My name is Thor
        Drax: Nice to meet you, Thor!

        You: I'm fine
        Drax: Awesome 😄
## You can modify data/intents.json to expand your conversation
```bash
{
  "tag": "greeting",
  "patterns": ["hi", "hello", "hey"],
  "responses": ["Hey there!", "Hello!", "Hi! How are you doing?"]
}
```

## Memory
The chatbot saves your name and other details in data/memory.json, so it remembers you between sessions.

## Improvements on the way
* Add GUI using Tkinter or a web framework (Flask/Streamlit)

* Implement NLP for smarter pattern matching

* Save full chat history

## Author
* Kevin Lopez
* jimenez.kevin0601@gmail.com
* GitHub: Kevin06Lo
