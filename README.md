# 📘 Full Step-by-Step Guide

## Using this folder as the root location

```text
C:\Users\nicholas.pannunzio\Downloads\TEMPLATES\Excel & PowerBI Templates\_CAREER DEVELOPMENT\AGENTIC AI DEVELOPMENT
```

This guide is split into two sections:

## 🧩 Part 1 — Initial Setup from Scratch

## 🔁 Part 2 — How to reopen the project later and run it again

I will also clearly tell you **where** each step happens:

* 🟦 **PowerShell**
* 🟪 **VS Code**
* 🌐 **Browser / Windows**

---

# 🧩 Part 1 — Initial Setup from Scratch

---

## ✅ What you will end up with

By the end of setup, you will have:

* a project folder in your chosen location
* a Python virtual environment
* Ollama installed and working
* a tool-capable local model
* a configuration file using `.env`
* a LangChain connection test
* three runnable agent scripts:

  * `simple_agent_hardcoded`
  * `simple_agent_prompted`
  * `simple_agent_loop`

---

## 🛑 Step 1 — Close everything first

### 📍 Where: **Windows**

Before you begin:

1. Close **VS Code**
2. Close all open **PowerShell** windows
3. If Ollama is open in the system tray, you can close it too

This helps ensure you are starting clean.

---

## 📂 Step 2 — Open PowerShell

### 📍 Where: **Windows**

Open a fresh **PowerShell** window.

---

## 📁 Step 3 — Go to your chosen root folder

### 📍 Where: **PowerShell**

Run this command exactly:

```powershell id="j6ygmz"
cd "C:\Users\nicholas.pannunzio\Downloads\TEMPLATES\Excel & PowerBI Templates\_CAREER DEVELOPMENT\AGENTIC AI DEVELOPMENT"
```

### ✅ Why the quotes matter

Your folder path contains:

* spaces
* the `&` character

So the full path must be wrapped in **double quotes**.

---

## 🧹 Step 4 — Decide how to handle an old project folder

### 📍 Where: **PowerShell**

If you already have an old `phase1-langchain-starter` folder in this location, the safest approach is to rename it before creating the new one.

Run this:

```powershell id="muhyc9"
Rename-Item "phase1-langchain-starter" "phase1-langchain-starter-old" -ErrorAction SilentlyContinue
```

### ✅ What this does

* If the old folder exists, it gets renamed
* If it does not exist, PowerShell quietly ignores it

---

## 🏗️ Step 5 — Create the fresh project folder

### 📍 Where: **PowerShell**

Run:

```powershell id="1rvjlwm"
mkdir phase1-langchain-starter -Force
cd phase1-langchain-starter
```

Now verify where you are:

```powershell id="pncr7n"
pwd
```

You should be inside:

```text
C:\Users\nicholas.pannunzio\Downloads\TEMPLATES\Excel & PowerBI Templates\_CAREER DEVELOPMENT\AGENTIC AI DEVELOPMENT\phase1-langchain-starter
```

---

## 🧱 Step 6 — Create the base project structure

### 📍 Where: **PowerShell**

Run:

```powershell id="h63r76"
git init
mkdir src
mkdir config
ni README.md, requirements.txt, .gitignore, .env, .env.example -ItemType File
ni src\__init__.py, config\__init__.py -ItemType File
```

### ✅ What this creates

Your folder will now contain:

```text
phase1-langchain-starter/
│
├─ config/
│  └─ __init__.py
│
├─ src/
│  └─ __init__.py
│
├─ .env
├─ .env.example
├─ .gitignore
├─ README.md
└─ requirements.txt
```

### ✅ Why the `__init__.py` files matter

They help Python treat `src` and `config` as packages, which is important for imports like:

```python
from config.settings import settings
```

---

## 🐍 Step 7 — Create the Python virtual environment

### 📍 Where: **PowerShell**

Run:

```powershell id="stjjsz"
py -3.11 -m venv .venv
```

This creates a private Python environment for this project only.

---

## ▶️ Step 8 — Activate the virtual environment

### 📍 Where: **PowerShell**

Run:

```powershell id="p4j6di"
.\.venv\Scripts\Activate.ps1
```

### ✅ What you should see

Your prompt should now begin with:

```text
(.venv)
```

That means the environment is active.

---

## 🚫 Step 9 — If PowerShell blocks activation

### 📍 Where: **PowerShell**

If activation fails, run:

```powershell id="mrdb7m"
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then:

1. close PowerShell
2. reopen PowerShell
3. run these again:

```powershell id="0ryq6x"
cd "C:\Users\nicholas.pannunzio\Downloads\TEMPLATES\Excel & PowerBI Templates\_CAREER DEVELOPMENT\AGENTIC AI DEVELOPMENT\phase1-langchain-starter"
.\.venv\Scripts\Activate.ps1
```

---

## 📦 Step 10 — Upgrade pip using the truststore version

### 📍 Where: **PowerShell**, with `(.venv)` visible

This is the correct version for **your machine**:

```powershell id="kjlwm1"
python -m pip install --use-feature=truststore --upgrade pip setuptools wheel
```

### ✅ Important

For your computer, this replaces the simpler pip upgrade command.

---

## 💻 Step 11 — Open the project in VS Code

### 📍 Where: **PowerShell**

Run:

```powershell id="eogk2k"
code .
```

If that does not work:

1. Open **VS Code**
2. Click **File**
3. Click **Open Folder**
4. Open:

```text
C:\Users\nicholas.pannunzio\Downloads\TEMPLATES\Excel & PowerBI Templates\_CAREER DEVELOPMENT\AGENTIC AI DEVELOPMENT\phase1-langchain-starter
```

---

## 🧩 Step 12 — Install the VS Code Python extensions

### 📍 Where: **VS Code**

In VS Code:

1. Click the **Extensions** icon on the left
2. Search for and install:

   * **Python**
   * **Pylance**
   * **Python Environments**

---

## 🎯 Step 13 — Select the correct Python interpreter

### 📍 Where: **VS Code**

1. Press `Ctrl + Shift + P`
2. Type:

```text
Python: Select Interpreter
```

3. Choose:

```text
.venv\Scripts\python.exe
```

This tells VS Code to use your project environment.

---

## 🖥️ Step 14 — Open a terminal inside VS Code

### 📍 Where: **VS Code**

1. Click **Terminal**
2. Click **New Terminal**

If the terminal does not show `(.venv)`, activate it manually:

```powershell id="ctkh6v"
.\.venv\Scripts\Activate.ps1
```

---

## 🤖 Step 15 — Install Ollama

### 📍 Where: **Browser / Windows**

If Ollama is not already installed:

1. Go to the official Ollama website
2. Download the Windows installer
3. Run the installer
4. Complete the installation

---

## ✅ Step 16 — Confirm Ollama is installed

### 📍 Where: **VS Code terminal** or **PowerShell**

Run:

```powershell id="jjlwm3"
ollama --version
```

If you see a version number, Ollama is installed.

---

## 📥 Step 17 — Pull the tool-capable model

### 📍 Where: **VS Code terminal** or **PowerShell**

Run:

```powershell id="lwjlwm"
ollama run orieg/gemma3-tools
```

### ✅ Why this model

This is the version that supports **tools**, which your LangChain agent needs.

When it starts:

* type something simple like `Hello`
* then press `Ctrl + C` to stop it

---

## 🌐 Step 18 — Confirm the Ollama local API is responding

### 📍 Where: **VS Code terminal** or **PowerShell**

Run:

```powershell id="0k78ew"
Invoke-RestMethod http://localhost:11434/api/ps
```

### ✅ What a normal result looks like

You may see something like:

```json
{"models":[]}
```

That is okay.

It means:

* Ollama is running
* the API is reachable
* no model is currently loaded into memory at that moment

---

## 📝 Step 19 — Fill in `.env.example`

### 📍 Where: **VS Code**

Open `.env.example` and paste:

```env id="545fix"
APP_ENV=dev
MODEL_PROVIDER=ollama
OLLAMA_MODEL=orieg/gemma3-tools
OLLAMA_BASE_URL=http://localhost:11434
```

Save the file.

---

## 📝 Step 20 — Fill in `.env`

### 📍 Where: **VS Code**

Open `.env` and paste:

```env id="vjlwm7"
APP_ENV=dev
MODEL_PROVIDER=ollama
OLLAMA_MODEL=orieg/gemma3-tools
OLLAMA_BASE_URL=http://localhost:11434
```

Save the file.

---

## 🚫 Step 21 — Fill in `.gitignore`

### 📍 Where: **VS Code**

Open `.gitignore` and paste:

```gitignore id="jlwmh8"
.venv/
__pycache__/
*.pyc
.env
```

Save the file.

---

## 📚 Step 22 — Fill in `requirements.txt`

### 📍 Where: **VS Code**

Open `requirements.txt` and paste:

```txt id="lwkjlwm"
langchain
langchain-ollama
python-dotenv
```

Save the file.

---

## 📦 Step 23 — Install the Python packages

### 📍 Where: **VS Code terminal**, with `(.venv)` active

Run these one by one:

```powershell id="jlwmg1"
python -m pip install --use-feature=truststore langchain
python -m pip install --use-feature=truststore langchain-ollama
python -m pip install --use-feature=truststore python-dotenv
```

---

## ⚙️ Step 24 — Create `config/settings.py`

### 📍 Where: **VS Code**

Create the file:

```text
config/settings.py
```

Paste this code:

```python id="jlwmr1"
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    app_env: str = os.getenv("APP_ENV", "dev")
    model_provider: str = os.getenv("MODEL_PROVIDER", "ollama")
    ollama_model: str = os.getenv("OLLAMA_MODEL", "orieg/gemma3-tools")
    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

settings = Settings()
```

Save it.

---

## 🧪 Step 25 — Create `src/test_connection.py`

### 📍 Where: **VS Code**

Create the file:

```text
src/test_connection.py
```

Paste this code:

```python id="jlwm0g"
from config.settings import settings
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model=settings.ollama_model,
    base_url=settings.ollama_base_url,
)

response = llm.invoke("Reply with exactly these two words: connection successful")

print(response.content)
```

Save it.

---

## 🧠 Step 26 — Create `src/simple_agent_hardcoded.py`

### 📍 Where: **VS Code**

Create the file:

```text
src/simple_agent_hardcoded.py
```

Paste this code:

```python id="0il1ze"
from config.settings import settings
from langchain.agents import create_agent
from langchain_ollama import ChatOllama

def get_phase_goal(phase_name: str) -> str:
    """Return the learning goal for a named phase."""
    goals = {
        "phase 1": "Set up a clean Python workspace and build one simple LangChain agent that can use a tool."
    }
    return goals.get(phase_name.lower().strip(), "Unknown phase")

model = ChatOllama(
    model=settings.ollama_model,
    base_url=settings.ollama_base_url,
)

agent = create_agent(
    model=model,
    tools=[get_phase_goal],
    system_prompt="You are a beginner-friendly AI tutor. Use tools when helpful."
)

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is the goal of Phase 1? Use your tool if needed."
            }
        ]
    }
)

print("\nAgent response:")
print(result["messages"][-1].content)
```

Save it.

---

## 💬 Step 27 — Create `src/simple_agent_prompted.py`

### 📍 Where: **VS Code**

Create the file:

```text
src/simple_agent_prompted.py
```

Paste this code:

```python id="jlwmrk"
from config.settings import settings
from langchain.agents import create_agent
from langchain_ollama import ChatOllama

def get_phase_goal(phase_name: str) -> str:
    """Return the learning goal for a named phase."""
    goals = {
        "phase 1": "Set up a clean Python workspace and build one simple LangChain agent that can use a tool."
    }
    return goals.get(phase_name.lower().strip(), "Unknown phase")

model = ChatOllama(
    model=settings.ollama_model,
    base_url=settings.ollama_base_url,
)

agent = create_agent(
    model=model,
    tools=[get_phase_goal],
    system_prompt="You are a beginner-friendly AI tutor. Use tools when helpful."
)

print("Ask a question about Phase 1.")
print("Example: What is the goal of Phase 1?")

user_question = input("\nYour question: ")

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": user_question
            }
        ]
    }
)

print("\nAgent response:")
print(result["messages"][-1].content)
```

Save it.

---

## 🔁 Step 28 — Create `src/simple_agent_loop.py`

### 📍 Where: **VS Code**

Create the file:

```text
src/simple_agent_loop.py
```

Paste this code:

```python id="vzjlwm"
from config.settings import settings
from langchain.agents import create_agent
from langchain_ollama import ChatOllama

def get_phase_goal(phase_name: str) -> str:
    """Return the learning goal for a named phase."""
    goals = {
        "phase 1": "Set up a clean Python workspace and build one simple LangChain agent that can use a tool."
    }
    return goals.get(phase_name.lower().strip(), "Unknown phase")

model = ChatOllama(
    model=settings.ollama_model,
    base_url=settings.ollama_base_url,
)

agent = create_agent(
    model=model,
    tools=[get_phase_goal],
    system_prompt="You are a beginner-friendly AI tutor. Use tools when helpful."
)

print("Phase 1 Agent Chat")
print("Ask a question about Phase 1.")
print("Type 'exit' to quit.\n")

while True:
    user_question = input("Your question: ").strip()

    if user_question.lower() in {"exit", "quit"}:
        print("\nGoodbye!")
        break

    if not user_question:
        print("\nPlease enter a question.\n")
        continue

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_question
                }
            ]
        }
    )

    print("\nAgent response:")
    print(result["messages"][-1].content)
    print()
```

Save it.

---

## ✅ Step 29 — Run the connection test

### 📍 Where: **VS Code terminal**

Run:

```powershell id="jlwmw2"
python -m src.test_connection
```

---

## ✅ Step 30 — Run the hardcoded version

### 📍 Where: **VS Code terminal**

Run:

```powershell id="jlwm0n"
python -m src.simple_agent_hardcoded
```

---

## ✅ Step 31 — Run the prompted version

### 📍 Where: **VS Code terminal**

Run:

```powershell id="03jlwm"
python -m src.simple_agent_prompted
```

---

## ✅ Step 32 — Run the loop version

### 📍 Where: **VS Code terminal**

Run:

```powershell id="s4jlwm"
python -m src.simple_agent_loop
```

---

# 🔁 Part 2 — How to reopen the project later and run it again

Once setup is complete, you do **not** need to repeat everything.

You only need to do the steps below.

---

## 📂 Step 1 — Open the project folder

### 📍 Where: **PowerShell** or **VS Code**

### Option A — Through PowerShell

Run:

```powershell id="jlwm19"
cd "C:\Users\nicholas.pannunzio\Downloads\TEMPLATES\Excel & PowerBI Templates\_CAREER DEVELOPMENT\AGENTIC AI DEVELOPMENT\phase1-langchain-starter"
code .
```

### Option B — Through VS Code

1. Open VS Code
2. Click **File**
3. Click **Open Folder**
4. Open the folder:

```text
C:\Users\nicholas.pannunzio\Downloads\TEMPLATES\Excel & PowerBI Templates\_CAREER DEVELOPMENT\AGENTIC AI DEVELOPMENT\phase1-langchain-starter
```

---

## 🐍 Step 2 — Activate the virtual environment

### 📍 Where: **VS Code terminal** or **PowerShell**

Run:

```powershell id="jlwmrl"
.\.venv\Scripts\Activate.ps1
```

You should see:

```text
(.venv)
```

---

## 🤖 Step 3 — Make sure Ollama is running

### 📍 Where: **Windows**

If needed, start Ollama again from the Start menu.

You can confirm it with:

```powershell id="fjlwmn"
ollama --version
```

Optional API check:

```powershell id="jlwmzf"
Invoke-RestMethod http://localhost:11434/api/ps
```

---

## ▶️ Step 4 — Run whichever script you want

### Test the model connection

```powershell id="zjlwm8"
python -m src.test_connection
```

### Run the hardcoded agent

```powershell id="jlwmvv"
python -m src.simple_agent_hardcoded
```

### Run the prompted agent

```powershell id="jlwmzc"
python -m src.simple_agent_prompted
```

### Run the loop agent

```powershell id="jlwmra"
python -m src.simple_agent_loop
```

---

# ⚠️ Important rule when running the scripts

Because of how your project is structured, **do not** run them like this:

```powershell id="bnq3mv"
python .\src\simple_agent_loop.py
```

Instead, always run them like this:

```powershell id="jlwmv1"
python -m src.simple_agent_loop
```

That is what keeps the imports working properly.

---

# ✅ Quick “reopen later” checklist

Whenever you come back later, follow this order:

## 1. Open the project folder

## 2. Activate `.venv`

## 3. Make sure Ollama is running

## 4. Run the script you want

That is all.

---

# 💡 Recommended everyday workflow

For regular testing, this is the easiest flow:

### In PowerShell

```powershell id="jlwmzu"
cd "C:\Users\nicholas.pannunzio\Downloads\TEMPLATES\Excel & PowerBI Templates\_CAREER DEVELOPMENT\AGENTIC AI DEVELOPMENT\phase1-langchain-starter"
code .
```

### In the VS Code terminal

```powershell id="jlwmxx"
.\.venv\Scripts\Activate.ps1
python -m src.simple_agent_loop
```

That gives you the fastest way to reopen the project and keep chatting with the agent.
