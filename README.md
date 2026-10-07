# 🧠 Doubt Slayer ChatBot

> **An AI-powered chatbot designed to help users overcome self-doubt through motivation, cognitive reframing, and realistic guidance.**

Doubt Slayer is an AI-based chatbot that helps users deal with **self-doubt, negative thoughts, lack of confidence, fear of failure, overthinking, and motivational struggles**.

The chatbot analyzes the user's input and generates an appropriate response using different motivational approaches such as **aggressive motivation, cognitive reframing, and realism**.

---

## 📌 Project Overview

Self-doubt can negatively affect confidence, decision-making, productivity, and personal growth.

**Doubt Slayer ChatBot** was developed to provide users with an interactive AI-based companion that responds to their doubts and negative thoughts in a direct and motivating manner.

Instead of providing generic motivational quotes, the system attempts to understand the user's input and provide a response based on the nature of their doubt.

### 💡 Example

**User:**
> "I don't think I am good enough to become a software developer."

**Doubt Slayer:**
> Provides a motivational and realistic response designed to challenge the user's negative thinking and encourage action.

---

## ✨ Features

- 🤖 **AI-powered chatbot**
- 🧠 Helps users overcome self-doubt
- 💪 Aggressive motivational responses
- 🔄 Cognitive reframing of negative thoughts
- 🎯 Realistic and practical responses
- 💬 Interactive chat interface
- 📊 Large response dataset
- 🌐 Flask-based web application
- ⚡ Fast response generation
- 📱 Simple and user-friendly interface

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Flask** | Web application framework |
| **Cohere API** | AI-powered response generation |
| **HTML** | Frontend structure |
| **CSS** | Frontend styling |
| **JavaScript** | Frontend interaction |
| **CSV** | Prompt and response datasets |
| **Git & GitHub** | Version control and source code management |
| **Vercel** | Deployment |

---

## 🏗️ Project Architecture

```text
                    ┌─────────────────────┐
                    │       User          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Flask Web App     │
                    │      (app.py)       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ User Input Analysis │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┼─────────────┐
                 ▼             ▼             ▼
          ┌────────────┐ ┌────────────┐ ┌────────────┐
          │Aggressive  │ │ Cognitive  │ │  Realistic │
          │Motivation  │ │ Reframing  │ │ Guidance   │
          └─────┬──────┘ └─────┬──────┘ └─────┬──────┘
                │              │              │
                └──────────────┼──────────────┘
                               ▼
                    ┌─────────────────────┐
                    │    Cohere API       │
                    │ AI Response Engine  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Generated Reply   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       User          │
                    └─────────────────────┘
```

---

## 📂 Project Structure

```text
Doubt-Slayer-ChatBot/
│
├── templates/
│   └── index.html
│
├── app.py
│
├── doubtslayer_prompts_500.csv
│
├── doubtslayer_prompts_8000.csv
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

### File Description

**`app.py`**

Main Flask application responsible for:

- Starting the web server
- Receiving user messages
- Processing user input
- Connecting with the AI API
- Generating chatbot responses

**`templates/`**

Contains the HTML templates used by the Flask frontend.

**`doubtslayer_prompts_500.csv`**

Dataset containing approximately 500 prompts/responses used by the project.

**`doubtslayer_prompts_8000.csv`**

Larger dataset containing approximately 8,000 prompts/responses for the chatbot.

**`requirements.txt`**

Contains the Python dependencies required to run the project.

---

# 🚀 Getting Started

Follow the steps below to run Doubt Slayer locally.

## 1. Clone the Repository

```bash
git clone https://github.com/041diksha/Doubt-Slayer-ChatBot.git
```

Navigate into the project directory:

```bash
cd Doubt-Slayer-ChatBot
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available in your local version, install Flask and the required AI SDK manually according to the imports used in `app.py`.

---

# 🔑 API Configuration

Doubt Slayer uses the **Cohere API** for AI-powered responses.

You should **never commit your API key directly into `app.py` or GitHub**.

Create an environment variable instead.

### Windows PowerShell

```powershell
$env:COHERE_API_KEY="your_api_key_here"
```

### macOS / Linux

```bash
export COHERE_API_KEY="your_api_key_here"
```

Then access it in Python:

```python
import os

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
```

### ⚠️ Security Warning

Never write:

```python
COHERE_API_KEY = "your-secret-api-key"
```

inside a public repository.

If an API key has already been pushed to GitHub, **revoke/rotate it immediately** and replace it with an environment variable.

---

# ▶️ Running the Application

Start the Flask application:

```bash
python app.py
```

You should see a local server similar to:

```text
Running on http://127.0.0.1:5000/
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

# 💬 How It Works

The basic workflow of Doubt Slayer is:

```text
User enters a doubt
        ↓
Flask receives the message
        ↓
Input is analyzed
        ↓
Appropriate motivational approach is selected
        ↓
Prompt is sent to AI model
        ↓
AI generates response
        ↓
Response is displayed to user
```

The chatbot focuses on three major response styles:

### 💪 1. Aggressive Motivation

Used when the user needs a strong push to stop procrastinating or doubting themselves.

### 🧠 2. Cognitive Reframing

Attempts to challenge negative assumptions and help the user look at the situation from another perspective.

### 🎯 3. Realistic Guidance

Provides a more practical response when the user's situation requires realistic expectations and actionable thinking.

---

# 📊 Dataset

The project includes two datasets:

```text
doubtslayer_prompts_500.csv
doubtslayer_prompts_8000.csv
```

These datasets contain prompts and responses related to:

- Self-doubt
- Confidence
- Fear of failure
- Career uncertainty
- Procrastination
- Overthinking
- Motivation
- Personal growth
- Failure
- Productivity

The larger dataset can be used for improving response coverage and experimentation with future AI/ML approaches.

---

# 🎯 Use Cases

Doubt Slayer can be useful for users experiencing:

- 😟 Self-doubt
- 😰 Fear of failure
- 🧠 Overthinking
- 😴 Lack of motivation
- 💼 Career uncertainty
- 📚 Academic pressure
- 💔 Loss of confidence
- 🚀 Difficulty taking action

---

# 🔮 Future Improvements

Some possible improvements for future versions include:

- [ ] Fine-tune a dedicated NLP model
- [ ] Add user authentication
- [ ] Store conversation history
- [ ] Add personalized responses
- [ ] Implement sentiment analysis
- [ ] Add emotion detection
- [ ] Improve prompt classification
- [ ] Add multiple AI models
- [ ] Add voice-based interaction
- [ ] Add multilingual support
- [ ] Create a mobile application
- [ ] Add conversation analytics
- [ ] Improve UI/UX
- [ ] Add automated testing
- [ ] Deploy using CI/CD

---

# 🔐 Privacy & Security

Doubt Slayer should not be considered a replacement for professional mental-health or medical support.

Users should avoid entering:

- Passwords
- API keys
- Financial information
- Personal identification documents
- Other highly sensitive information

API credentials should always be stored using **environment variables or secure deployment secrets**.

---

# 🤝 Contributing

Contributions are welcome!

### 1. Fork the repository

```bash
git fork https://github.com/041diksha/Doubt-Slayer-ChatBot
```

### 2. Clone your fork

```bash
git clone <your-fork-url>
```

### 3. Create a new branch

```bash
git checkout -b feature/new-feature
```

### 4. Make your changes

Implement your improvements and test them locally.

### 5. Commit your changes

```bash
git add .
git commit -m "Add new feature"
```

### 6. Push your branch

```bash
git push origin feature/new-feature
```

### 7. Create a Pull Request

Open a Pull Request on GitHub describing your changes.

---

# 📜 License

This project is intended for educational and development purposes.

If you want to use this project commercially or redistribute it, please contact the repository owner.

---

# 👨‍💻 Author

**Diksha Batham**

GitHub:  
https://github.com/041diksha

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

Your support helps improve and expand the project!

---

## 🚀 Project Status

**Status:** Active Development

Doubt Slayer is an evolving project and future versions may include improved AI models, personalization, emotion detection, conversation memory, and additional features.

---

### Made with ❤️ using Python, Flask & AI
