# GENERATIVE_TEXT_MODEL 🚀

![Frontend](https://github.com/UmeshSamartapu/GENERATIVE_TEXT_MODEL_GPT2/blob/main/App/Input/TextgenwithGPT2-Frontend.png)


## Overview

A text generation project using **GPT-2** and **LSTM** models to generate coherent paragraphs based on user prompts. Includes both notebook implementations and a deployable FastAPI web app.

## 📌 Project Overview

**Objective:**  
Create text generation models using:
1. **GPT-2** (via Hugging Face Transformers) for modern language generation.
2. **LSTM** (trained on Shakespeare's *Hamlet*) for poetic/dramatic text.

**Deliverables:**
- Jupyter Notebooks for GPT-2 and LSTM text generation.
- A FastAPI web app for interactive text generation.

---

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CODTECH-04-GENERATIVE_TEXT_MODEL.git
   cd CODTECH-04-GENERATIVE_TEXT_MODEL
   ```
### 2.Install dependencies:
```bash
pip install -r requirements.txt
```

# 📂 Directory Structure
```bash
CODTECH-04-GENERATIVE_TEXT_MODEL/
├── notebooks/
│   ├── gpt2_text_generation.ipynb    # GPT-2 Colab notebook
│   └── lstm_text_generation.ipynb    # LSTM Colab notebook
├── app/                              # FastAPI web app
│   ├── app.py                        # FastAPI backend
│   └── templates/
│       └── index.html                # Frontend HTML
├── requirements.txt                  # Python dependencies
└── README.md
```

# 🧠 Models & Features

### 1. GPT-2 Model
- **Library:** Hugging Face transformers
- **Features:**
- Generates modern, coherent paragraphs.
- Handles casual/informative prompts (e.g., "How to build a website...").
- Optimized for Google Colab.

### 2. LSTM Model
- **Dataset:** Shakespeare's Hamlet (via NLTK).
- **Features:**
- Generates poetic/dramatic text.
- Works best with Shakespearean prompts (e.g., "To be or not to be...").
- Compatible with GPU (CuDNN acceleration).

### 3. FastAPI Web App
- **Interactive UI:** Input prompts and view generated text.
- **Deployment-ready:** Run locally or deploy to cloud services.

# 🚀 Usage

## Notebooks (Google Colab)
- **Open the notebook** 
- gpt2_text_generation.ipynb or lstm_text_generation.ipynb).
- **Run cells sequentially to:**
- Install dependencies.
- Load the model.
- Generate text from prompts.

## FastAPI App

#### 1.Navigate to the app directory:
```bash
cd app
```

#### 2.Run the app:
```bash
uvicorn app:app --reload
```

#### Open http://127.0.0.1:8000 in your browser.
```bash
http://127.0.0.1:8000 
```

# 📋 Requirements
```bash
fastapi==0.95.1
uvicorn[standard]==0.22.0
transformers==4.34.0
torch==2.0.1
jinja2==3.1.2
nltk==3.8.1
tensorflow==2.12.0
````
# 💡 Example Prompts

- **GPT-2 (Modern Language):**
- "The future of artificial intelligence is..."
- "How to build a website using HTML and CSS..."
- **LSTM (Shakespearean Style):**
- "To be or not to be, that is..."
- "O, what a noble mind is here..."

## Demo 
### You can watch the ([youtube video]( )) for demo
<p align="center">
  <img src="https://github.com/UmeshSamartapu/GENERATIVE_TEXT_MODEL_GPT2/blob/main/App/Input/TextgenwithGPT2-Demo.gif" />
</p>  


## 📫 Let's Connect

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/umeshsamartapu/)
[![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://x.com/umeshsamartapu)
[![Email](https://img.shields.io/badge/-Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:umeshsamartapu@gmail.com)
[![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/umeshsamartapu/)
[![Buy Me a Coffee](https://img.shields.io/badge/-Buy%20Me%20a%20Coffee-FBAD19?style=flat-square&logo=buymeacoffee&logoColor=black)](https://www.buymeacoffee.com/umeshsamartapu)

---

🔥 Always exploring new technologies and solving real-world problems with code!
