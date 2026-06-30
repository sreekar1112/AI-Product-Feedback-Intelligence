# 🤖 AI Product Feedback Intelligence Platform

> **Transform customer reviews into actionable product insights using Generative AI, Retrieval-Augmented Generation (RAG), and Large Language Models.**

![Python](https://img.shields.io/badge/Python-3.10-blue)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![Gradio](https://img.shields.io/badge/Gradio-UI-orange)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-red)
![Groq](https://img.shields.io/badge/Groq-LLM-purple)

---

## 📌 Overview

Product Managers often spend hours manually reading thousands of customer reviews to identify recurring issues and prioritize product improvements.

This project automates that process using **Retrieval-Augmented Generation (RAG)**.

The platform analyzes real ChatGPT customer reviews and generates:

* 📊 Product Issue Prioritization
* 🔥 Trending Topics
* 📝 AI-generated Jira Tickets
* 📑 Sprint Summaries
* 💬 Natural Language Q&A over customer reviews

The goal is to help Product Managers make faster, data-driven product decisions.

---

# 🚀 Live Demo

**Hugging Face Space**

https://huggingface.co/spaces/Shrekh/ai-product-feedback-intelligence

---

# ✨ Features

### 💬 Ask AI

Ask natural language questions about customer reviews.

Examples:

* What are users saying about memory?
* Why are users giving low ratings?
* What are the biggest customer complaints?
* What feature requests are customers asking for?

---

### 📊 Issue Prioritization Matrix

Automatically identifies the most critical product issues and ranks them by business impact.

Example:

| Rank | Issue         | Priority    |
| ---- | ------------- | ----------- |
| 1    | Memory Issues | 🔴 Critical |
| 2    | Voice Mode    | 🟠 High     |
| 3    | Performance   | 🟡 Medium   |

---

### 🔥 Trending Topics

Automatically discovers the most discussed product topics from customer reviews.

Examples:

* Memory
* Voice Mode
* UI Improvements
* Performance
* Subscription
* Login
* Feature Requests

---

### 📑 Sprint Summary Generator

Generates sprint-ready summaries including:

* Executive Summary
* Top Customer Issues
* Sprint Goals
* Risks
* Recommendations

---

### 📝 Jira Ticket Generator

Automatically generates professional Jira tickets containing:

* Issue Type
* Summary
* Description
* Priority
* Severity
* Labels
* Acceptance Criteria
* Definition of Done

---

# 🏗 Architecture

```
                    Customer Reviews (CSV)
                              │
                              ▼
                    LangChain Documents
                              │
                              ▼
                  HuggingFace Embeddings
                              │
                              ▼
                         FAISS Vector DB
                              │
                              ▼
                  Semantic Similarity Search
                              │
                              ▼
                        Retrieved Context
                              │
                              ▼
                     Groq Llama 3.3 70B LLM
                              │
            ┌─────────────────┼──────────────────┐
            ▼                 ▼                  ▼
        Ask AI         Sprint Summary      Jira Ticket
                              │
                              ▼
                        Gradio Interface
```

---

# 🛠 Tech Stack

### Language

* Python

### AI / LLM

* LangChain
* Groq
* Llama 3.3 70B
* HuggingFace Embeddings

### Vector Database

* FAISS

### Frontend

* Gradio

### Data

* Google Play Store Reviews

---

# 📂 Project Structure

```
AI-Product-Feedback-Intelligence/

├── app.py
├── rag.py
├── prompts.py
├── requirements.txt
├── README.md

├── chatgpt_reviews_cleaned.csv

├── index.faiss
├── index.pkl
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Product-Feedback-Intelligence.git
```

Move into the project

```bash
cd AI-Product-Feedback-Intelligence
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a Hugging Face Secret or environment variable:

```
GROQ_API_KEY=your_api_key
```

---

# ▶️ Run Locally

```bash
python app.py
```

---

# 📊 Dataset

The application uses **Google Play Store reviews** for the ChatGPT mobile application.

The dataset was:

* Collected using `google-play-scraper`
* Cleaned and preprocessed
* Converted into LangChain Documents
* Embedded using HuggingFace Embeddings
* Indexed with FAISS

---

# 📸 Application Preview

Add screenshots here after deployment.

Examples:

* Dashboard
* Ask AI
* Sprint Summary
* Jira Ticket Generator

---

# 📈 Future Improvements

* Semantic Review Clustering
* Interactive Product Analytics Dashboard
* PDF Report Generation
* Version Comparison
* Export Jira Tickets
* Agentic AI Product Manager
* Multi-Agent Product Intelligence Workflow

---

# 👨‍💻 Author

**Sreekar Regulavalasa**

GitHub:
https://github.com/sreekar1112

LinkedIn:
https://www.linkedin.com/in/sreekar-regulavalasa-3798b134a/

---

# ⭐ If you found this project useful, consider giving it a star!

