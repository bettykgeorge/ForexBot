# 💱 ForexBot — Real-Time Currency Converter

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Webhook-000000?logo=flask&logoColor=white)
![Dialogflow](https://img.shields.io/badge/Dialogflow-NLP-FF9800?logo=dialogflow&logoColor=white)
![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?logo=render&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

A Telegram chatbot that performs **real-time currency conversion** using a Flask-based webhook, Dialogflow NLP, and the ExchangeRate API — deployed on Render for 24/7 availability.

---

## 📌 Overview

ForexBot lets users convert between any currencies directly inside Telegram by typing natural language messages like:

> *"Convert 100 USD to INR"* → **100 USD is 8312.0 INR**

The bot uses **Dialogflow** to understand user intent and extract currency/amount parameters, then calls a **Flask webhook** which fetches live exchange rates and returns the converted value instantly.

---

## 🏗️ Architecture

```
User (Telegram)
      ↓
Dialogflow (NLP — intent & parameter extraction)
      ↓
Flask Webhook on Render (app.py)
      ↓
ExchangeRate API (live conversion rates)
      ↓
Response back to Telegram
```

---

## ✨ Features

- 💬 **Natural language input** — powered by Dialogflow intent recognition
- 📈 **Live exchange rates** — fetched in real-time via ExchangeRate API
- ⚡ **Instant responses** — Flask webhook handles fulfillment in milliseconds
- 🌍 **Supports all major currencies** — USD, EUR, INR, GBP, JPY, and more
- ☁️ **Always online** — backend deployed on Render for 24/7 uptime
- 🛡️ **Error handling** — graceful fallback messages for unexpected inputs

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core backend language |
| Flask | Webhook server & REST endpoint |
| Dialogflow | NLP — intent detection & parameter extraction |
| Telegram Bot API | User-facing chat interface |
| ExchangeRate API | Live forex conversion rates |
| Gunicorn | Production WSGI server |
| Render | Cloud deployment & hosting |

---

## 🗂️ Project Structure

```
ForexBot/
│
├── app.py              # Flask webhook — handles Dialogflow fulfillment
├── main.py             # Entry point / PyCharm template (placeholder)
├── requirements.txt    # Python dependencies
├── Procfile            # Render deployment config (gunicorn)
└── README.md
```

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.x
- A [Dialogflow](https://dialogflow.cloud.google.com/) agent with currency conversion intent set up
- A [Telegram Bot](https://core.telegram.org/bots#botfather) token from BotFather
- A free API key from [exchangerate-api.com](https://www.exchangerate-api.com/)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/bettykgeorge/ForexBot.git
cd ForexBot
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure your API key

In `app.py`, replace the ExchangeRate API key in the URL:

```python
url = f"https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/{source}"
```

### 4️⃣ Run locally

```bash
python app.py
```

Use [ngrok](https://ngrok.com/) to expose your local server for Dialogflow webhook testing:

```bash
ngrok http 5000
```

### 5️⃣ Deploy to Render

Push to GitHub and connect the repo to [Render](https://render.com/). The `Procfile` handles the rest:

```
web: gunicorn app:app
```

---

## 💬 Example Interaction

```
User:  Convert 200 EUR to GBP
Bot:   200 EUR is 171.46 GBP

User:  What is 500 USD in JPY?
Bot:   500 USD is 74823.5 JPY
```

---

## 🔮 Future Improvements

- [ ] Add support for cryptocurrency conversion (BTC, ETH)
- [ ] Provide conversion history per user
- [ ] Add inline keyboard for quick currency selection
- [ ] Multi-language support via Dialogflow

---

## 🧠 Key Concepts Demonstrated

- Webhook-based chatbot architecture (Dialogflow fulfillment)
- REST API integration with real-time data fetching
- Flask route handling and JSON request/response parsing
- Cloud deployment with Render and Gunicorn
- Natural language processing for dynamic parameter extraction

---

## 👩‍💻 Author

**Betty K George**

[![GitHub](https://img.shields.io/badge/GitHub-bettykgeorge-181717?logo=github)](https://github.com/bettykgeorge)

---

## 📌 License

This project is for academic and learning purposes.

<img width="1144" height="1122" alt="image" src="https://github.com/user-attachments/assets/442f7510-165e-4409-835a-8434c504dadb" />
