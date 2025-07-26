# AI CodeGen Portal

A Django‑powered web portal that brings AI into your developer workflow. Conceptualized and developed to seamlessly incorporate AI into code editing, this project harnesses OpenAI’s GPT‑4 to provide real‑time code correction and intelligent suggestions across 30+ programming languages—all inside a polished, responsive interface.

---

## 🚀 Features

- **AI‑Driven Code Fixer**  
  Submit your snippet and receive corrected code instantly in the same language.  
- **AI‑Powered Code Suggestions**  
  Ask for examples or patterns (e.g. “How to implement debounce in JavaScript?”) and get ready‑to‑use snippets.  
- **Multi‑Language Support**  
  C, C++, C#, Java, JavaScript, Python, Ruby, Rust, SQL, …and more.  
- **User Authentication & Profiles**  
  Register, log in, and manage your account (username/password updates).  
- **Snippet History**  
  View, delete, and paginate through all past “fix” and “suggest” sessions.  
- **Dashboard Metrics**  
  At‑a‑glance cards for **Codes Fixed** and **Codes Suggested**.  
- **Syntax Highlighting**  
  Prism.js with line numbers for a clean, readable code display.  
- **Polished UI & UX**  
  Bootstrap 5 layout, SweetAlert2 notifications, and custom theming for an intuitive experience.  
- **Secure Configuration**  
  Environment variables via a `.env` file (python‑decouple) to keep API keys and secrets safe.  

---

## 📦 Tech Stack

- **Backend:** Django 5.x, Python 3.10+  
- **AI API:** OpenAI GPT‑4  
- **Database:** PostgreSQL (or SQLite for local dev)  
- **Frontend:** Bootstrap 5, Prism.js, SweetAlert2  
- **Secrets Management:** python‑decouple (`.env`)  
- **Version Control:** Git & GitHub  

---

## 🛠️ Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/ai-codegen-portal.git
   cd ai-codegen-portal
   
2. Create & activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables
Create a .env file in the project root:
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/DB_NAME
OPENAI_API_KEY=sk-your_openai_key_here

5. python manage.py migrate

6. python manage.py runserver

7. Open your browser at http://localhost:8000/

🎯 Usage

    Register a new account or Log in.

    Use the Fix Code tab to paste or type your snippet, select a language, and click Fix Code.

    View and copy the corrected code.

    Switch to Suggest Code to get generated examples or patterns.

    Check History to revisit or delete past sessions.

    Visit Account Settings to update your username or password.
Made with ❤️ by Abdulrasheed Shittu