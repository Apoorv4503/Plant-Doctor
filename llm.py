import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_treatment_advice(disease, confidence, question="", weather=None):
    """
    Takes disease + confidence + question + weather
    Returns smart personalized advice
    """
    
    weather_context = ""
    if weather:
        weather_context = f"""
    Current Weather Conditions:
    - City: {weather['city']}
    - Temperature: {weather['temperature']}°C
    - Humidity: {weather['humidity']}%
    - Condition: {weather['condition']}
    - Wind Speed: {weather['wind_speed']} m/s
    """
    
    user_question = f"\nFarmer's Question: {question}" if question else ""
    
    prompt = f"""
    You are an expert plant doctor. A plant has been diagnosed with:
    Disease: {disease}
    Confidence: {confidence}%
    {weather_context}
    {user_question}
    
    Please provide:
    1. Brief disease description (2 lines)
    2. Severity level (Low/Medium/High)
    3. How current weather affects this disease
    4. Treatment steps (3-4 steps)
    5. Prevention tips (2-3 tips)
    
    Keep it practical and weather-aware.
    """
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=600
    )
    
    return response.choices[0].message.content