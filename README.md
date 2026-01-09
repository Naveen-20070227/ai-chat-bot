# 🤖 AI Chatbot API (FastAPI + Phi-2)

An **AI Chatbot REST API** built using **FastAPI** and powered by **Microsoft Phi-2**, leveraging **Hugging Face Transformers** for natural language generation. This project demonstrates how to serve a lightweight open-source language model as an API for chatbot-style interactions.

The API is designed for learning, experimentation, and early-stage AI integration into applications.

---

## 🚀 Features

* AI-powered conversational responses
* Powered by **Microsoft Phi-2** language model
* RESTful API built with FastAPI
* Text generation using Hugging Face Transformers
* Request and response validation using Pydantic
* Interactive API documentation (Swagger UI)

---

## 🛠️ Tech Stack

* **Backend Framework:** FastAPI
* **Language:** Python
* **AI Model:** Microsoft Phi-2
* **ML Library:** Hugging Face Transformers
* **Model Source:** Hugging Face Hub
* **Data Validation:** Pydantic
* **Server:** Uvicorn

---

## 📂 Project Structure

```
ai-chatbot-api/
│── main.py
│── schemas.py
│── chatbot.py
│── requirements.txt
```

---

## ⚙️ Installation & Setup

1. Clone the repository

   ```bash
   git clone https://github.com/your-username/ai-chatbot-api.git
   cd ai-chatbot-api
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Run the API server

   ```bash
   uvicorn main:app --reload
   ```

---

## 📌 API Documentation

After starting the server, access:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📬 Sample Endpoint

* `POST /chat`

  * Accepts a user prompt
  * Returns an AI-generated response using Phi-2

---

## 🎯 Learning Outcomes

* Serving LLMs via REST APIs
* Using Hugging Face models in backend applications
* FastAPI integration with AI/ML models
* Building scalable AI-powered services

---

## 🔮 Future Improvements

* Conversation memory / chat history
* Streaming responses
* Model fine-tuning integration
* Authentication & rate limiting
* Deployment with Docker and cloud platforms

---

## ⚠️ Notes

* Phi-2 is used in an **early-stage / experimental setup**
* Performance depends on system resources (CPU/GPU)
* Intended for educational and prototype use

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is open-source and available under the MIT License.

---

### ⭐ If you find this project useful, give it a star on GitHub!

