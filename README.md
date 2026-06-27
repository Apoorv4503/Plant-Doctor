---
title: Plant Doctor
emoji: 🏢
colorFrom: blue
colorTo: blue
sdk: gradio
sdk_version: 6.19.0
python_version: '3.13'
app_file: app.py
pinned: false
license: mit
short_description: 🌿 AI-powered plant disease detection using Llama Vision, Gr
---

# 🌿 Multimodal Plant Doctor

> An AI-powered plant disease detection system combining **Llama Vision**, **Groq LLM**, and **real-time weather data** to provide personalized treatment recommendations.

[![Live Demo](https://img.shields.io/badge/🤗_Hugging_Face-Live_Demo-orange)](https://huggingface.co/spaces/Apoorv4503/plant-doctor)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black)](https://github.com/Apoorv4503/Plant-Doctor)
[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://python.org)
[![Gradio](https://img.shields.io/badge/Gradio-UI-orange)](https://gradio.app)
[![Groq](https://img.shields.io/badge/Groq-LLM-green)](https://groq.com)

---

## 🎯 What Is This?

**Multimodal Plant Doctor** is a production-ready AI application that helps farmers and gardeners diagnose plant diseases instantly. Unlike basic image classifiers, this system combines **three types of data** (image + text + weather) to give highly personalized, context-aware treatment advice.

### The Problem
- Farmers lose 20-40% of crops due to plant diseases every year
- Expert agronomists are expensive and not always accessible
- Basic AI tools give generic advice without considering local conditions

### The Solution
An AI system that:
1. **Sees** your plant through Llama Vision
2. **Understands** your question in natural language
3. **Checks** your local weather conditions
4. **Gives** personalized, weather-aware treatment advice

---

## 🚀 Live Demo

👉 **[Try it here: huggingface.co/spaces/Apoorv4503/plant-doctor](https://huggingface.co/spaces/Apoorv4503/plant-doctor)**

### How to Use
1. Upload a photo of your plant leaf
2. Type your question (optional): *"Why are my leaves turning yellow?"*
3. Enter your city for weather-aware advice
4. Click **Submit** and get instant AI diagnosis!

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 **Disease Detection** | Identifies plant diseases with 90%+ confidence using Llama Vision |
| 🌦️ **Weather Integration** | Fetches real-time weather data to give location-aware advice |
| 💬 **Natural Language** | Ask questions in plain English about your plant |
| 🤖 **AI Treatment Advice** | Groq LLM generates detailed treatment steps and prevention tips |
| ⚡ **Fast Response** | Results in under 5 seconds |
| 🌐 **Web Interface** | Clean, easy-to-use Gradio UI |

---

## 🏗️ Architecture

```
User Input
    │
    ├── 📸 Leaf Image
    ├── 💬 Text Question  
    └── 📍 City Name
          │
          ▼
┌─────────────────────────────────┐
│         Multimodal AI Pipeline  │
│                                 │
│  📸 Image ──► Llama Vision ──►  |
│                    │            │
│  🌦️ Weather API ──►│            │
│                    ▼            │
│              Groq LLM           │
│                    │            │
└────────────────────┼────────────┘
                     │
                     ▼
            Smart Recommendation
            ┌─────────────────┐
            │ Disease Name    │
            │ Confidence %    │
            │ Weather Impact  │
            │ Treatment Steps │
            │ Prevention Tips │
            └─────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Vision AI** | Llama 4 Scout (via Groq) | Plant disease detection from images |
| **Language AI** | Llama 3.3 70B (via Groq) | Treatment advice generation |
| **Weather** | OpenWeatherMap API | Real-time weather data |
| **UI** | Gradio | Web interface |
| **Language** | Python 3.x | Backend logic |
| **Deployment** | Hugging Face Spaces | Cloud hosting |

---

## 📁 Project Structure

```
plant-doctor/
│
├── app.py          # Main application & Gradio UI
├── model.py        # Llama Vision disease detection
├── llm.py          # Groq LLM treatment advice
├── weather.py      # OpenWeatherMap integration
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

### Step 1 — Disease Detection (model.py)
```python
# Llama Vision analyzes the leaf image
# Returns: disease name + confidence score
disease, confidence = identify_disease(image_path)
# Example output: "Septoria leaf spot", 90.0%
```

### Step 2 — Weather Fetch (weather.py)
```python
# Real-time weather from OpenWeatherMap
weather = get_weather("Noida")
# Returns: temperature, humidity, condition, wind speed
```

### Step 3 — AI Advice (llm.py)
```python
# Groq LLM combines everything
advice = get_treatment_advice(disease, confidence, question, weather)
# Returns: personalized, weather-aware treatment plan
```

---

## 🏃 Run Locally

### Prerequisites
- Python 3.x
- Groq API key (free at console.groq.com)
- OpenWeatherMap API key (free at openweathermap.org)

### Installation

```bash
# Clone the repository
git clone https://github.com/Apoorv4503/Plant-Doctor.git
cd Plant-Doctor

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file:
```
GROQ_API_KEY="your_groq_api_key_here"
WEATHER_API_KEY="your_openweather_api_key_here"
```

### Run

```bash
python app.py
```

Open **http://127.0.0.1:7860** in your browser!

---

## 📊 Sample Output

**Input:**
- Image: Tomato leaf with brown spots
- Question: "Why are my leaves getting spots?"
- City: Noida

**Output:**
```
🌿 Disease Detected: Septoria leaf spot
📊 Confidence: 90.0%

🌡️ Temperature: 42.78°C
💧 Humidity: 19%
🌤️ Condition: Clear sky

🤖 AI Treatment Advice:
Disease Description: Septoria leaf spot is a fungal disease
that causes small, circular spots on leaves...

Severity Level: High (90% confidence)

Weather Impact: Current high temperature may stress the plant,
making it more susceptible. Low humidity slows spread but
sudden rain could rapidly increase spore dispersal...

Treatment Steps:
1. Remove infected leaves immediately
2. Apply broad-spectrum fungicide
3. Improve air circulation
4. Maintain plant hygiene

Prevention Tips:
1. Avoid overhead watering
2. Disinfect gardening tools regularly
3. Monitor plants weekly for early signs
```

---

## 🔮 Future Improvements

- [ ] Multi-language support (Hindi, Spanish, French)
- [ ] Crop calendar integration
- [ ] Disease history tracking
- [ ] Mobile app (React Native)
- [ ] Soil data integration
- [ ] Satellite imagery analysis

---

## 🧠 What I Learned

- Multimodal AI pipeline design
- Vision LLM integration (Llama Vision via Groq)
- REST API integration (OpenWeatherMap)
- Prompt engineering for structured outputs
- Gradio UI development
- Hugging Face Spaces deployment
- Git version control best practices
- Environment variable security

---

## 👨‍💻 Author

**Apoorv**
- GitHub: [@Apoorv4503](https://github.com/Apoorv4503)
- Hugging Face: [@Apoorv4503](https://huggingface.co/Apoorv4503)

---

## 📄 License

This project is licensed under the MIT License.

---

