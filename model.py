import os
import base64
from groq import Groq
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def identify_disease(image_path):
    """
    Uses Groq Vision (Llama) to identify plant disease
    No separate model needed!
    """
    # Convert image to base64
    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")
    
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_data}"
                    }
                },
                {
                    "type": "text",
                    "text": "You are a plant disease expert. Look at this plant leaf image and identify the disease. Respond in exactly this format:\nDisease: [disease name]\nConfidence: [percentage]%\nNothing else."
                }
            ]
        }],
        max_tokens=100
    )
    
    # Parse response
    result = response.choices[0].message.content
    lines = result.strip().split("\n")
    disease = lines[0].replace("Disease:", "").strip()
    confidence = lines[1].replace("Confidence:", "").replace("%", "").strip()
    
    return disease, float(confidence)