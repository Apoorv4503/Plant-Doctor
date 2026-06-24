import os
from groq import Groq
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Connect to Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_treatment_advice(disease, confidence):
    """
    Takes disease name + confidence
    Returns smart treatment advice from Groq LLM
    """
    
    prompt = f"""
    You are an expert plant doctor. A plant has been diagnosed with:
    Disease: {disease}
    Confidence: {confidence}%
    
    Please provide:
    1. Brief disease description (2 lines)
    2. Severity level (Low/Medium/High)
    3. Treatment steps (3-4 steps)
    4. Prevention tips (2-3 tips)
    
    Keep it simple and practical for a farmer.
    """
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    
    return response.choices[0].message.content