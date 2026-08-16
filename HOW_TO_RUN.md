# 🤖 LangChain Chatbot - Complete Setup Guide

## Step-by-Step Instructions to Run the Project

### **Step 1: Prerequisites Check** ✅
Make sure you have:
- **Python 3.7+** installed on your computer
- **pip** (Python package manager) - usually comes with Python
- **Git** (to clone repositories)
- **Google Gemini API Key** (free - see Step 4)

**Check Python version:**
```bash
python --version
```

---

### **Step 2: Download/Clone the Project**

#### Option A: If not already cloned
```bash
git clone https://github.com/Ankitsingh9555/gemini-chatbot.git
cd gemini-chatbot
```

#### Option B: If already downloaded (your case)
```bash
cd c:\Users\meera\Downloads\LANGCHAIN\gemini-chatbot
```

---

### **Step 3: Create a Virtual Environment** 🔒

A virtual environment keeps project dependencies separate and clean.

#### **Windows:**
```bash
python -m venv myenv
```

#### **Activate Virtual Environment:**
```bash
myenv\Scripts\Activate.ps1
```

**On Mac/Linux:**
```bash
python3 -m venv myenv
source myenv/bin/activate
```

**How to know if it's activated:** You should see `(myenv)` at the beginning of your terminal line.

---

### **Step 4: Get Google Gemini API Key** 🔑

1. Go to: **https://ai.google.dev/**
2. Click **"Get API Key"**
3. Click **"Create API Key in new project"**
4. Copy the generated API key
5. Keep it safe - you'll need it in Step 5

---

### **Step 5: Set Up Environment Variables**

Create a `.env` file in your project folder with your API key:

**File location:** `c:\Users\meera\Downloads\LANGCHAIN\gemini-chatbot\.env`

**Content:**
```
GEMINI_API_KEY=your_actual_api_key_here
```

**Example:**
```
GEMINI_API_KEY=AIzaSyDxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

### **Step 6: Install Dependencies** 📦

Make sure your virtual environment is activated, then run:

```bash
pip install -r requirements.txt
```

**This will install:**
- `langchain` - LLM framework
- `langchain-google-genai` - Google Gemini integration
- `google-generativeai` - Google AI SDK
- `streamlit` - Web interface
- `python-dotenv` - Environment variable loader

**Wait for all packages to install successfully...**

---

### **Step 7: Run the Chatbot** 🚀

```bash
python main.py
```

**You should see:**
```
🤖 Chatbot: Hello! Ask me anything. (Type 'exit' to quit)
--------------------------------------------------
```

---

### **Step 8: Interact with the Chatbot** 💬

**Type your questions:**
```
📝 You: What is machine learning?
🤖 Chatbot: Machine Learning is a branch of Artificial Intelligence...
```

**Continue asking questions, or exit by typing:**
- `exit`
- `quit`
- `bye`

---

## **Quick Reference Commands**

| Command | Purpose |
|---------|---------|
| `python --version` | Check Python version |
| `python -m venv myenv` | Create virtual environment |
| `myenv\Scripts\Activate.ps1` | Activate (Windows PowerShell) |
| `myenv\Scripts\activate.bat` | Activate (Windows Command Prompt) |
| `source myenv/bin/activate` | Activate (Mac/Linux) |
| `pip install -r requirements.txt` | Install dependencies |
| `python main.py` | Run the chatbot |
| `deactivate` | Deactivate virtual environment |

---

## **Troubleshooting** 🔧

### **Problem: "Python is not recognized"**
- Install Python from https://www.python.org/
- Add Python to PATH during installation

### **Problem: "ModuleNotFoundError: No module named..."**
- Make sure virtual environment is activated: `(myenv)` should show in terminal
- Run: `pip install -r requirements.txt` again
- Wait for all packages to install

### **Problem: "GEMINI_API_KEY not found"**
- Check if `.env` file exists in the project folder
- Check if you copied the API key correctly (no spaces)
- Restart the Python script

### **Problem: "API Key invalid or expired"**
- Generate a new API key from https://ai.google.dev/
- Update your `.env` file
- Restart the chatbot

### **Problem: Permission Denied on Windows**
If you get a permission error when activating, try:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then activate again.

---

## **Project Structure** 📁

```
gemini-chatbot/
├── main.py              # Main chatbot script (RUN THIS!)
├── requirements.txt     # List of dependencies
├── .env                 # API key (create this)
├── .gitignore           # Files to ignore in Git
├── README.md            # Project documentation
└── myenv/               # Virtual environment (auto-created)
```

---

## **What the Project Does** 🎯

1. **Loads your Gemini API Key** from `.env` file
2. **Creates a ChatGPT-like chatbot** using Google's Gemini AI
3. **Accepts your questions** via command line
4. **Generates intelligent responses** using LangChain
5. **Loops until you exit** (type: exit, quit, or bye)

---

## **Success! 🎉**

You should now have a fully working AI chatbot! 

Questions? Refer back to the troubleshooting section or check the README.md file.

---

**Happy Chatting!** 🚀
