import gradio as gr
from model import identify_disease
from llm import get_treatment_advice
from weather import get_weather

def analyze_plant(image, question, city):
    """
    Takes image + question + city
    Returns disease + weather-aware AI advice
    """
    # Save uploaded image
    image_path = "temp_leaf.jpg"
    image.save(image_path)
    
    # Get disease from vision model
    disease, confidence = identify_disease(image_path)
    
    # Get weather data
    weather = get_weather(city if city else "Noida")
    
    # Get smart advice from Groq with weather context
    advice = get_treatment_advice(disease, confidence, question, weather)
    
    # Format diagnosis
    diagnosis = f"""
🌿 Disease Detected: {disease}
📊 Confidence: {confidence}%
    """
    
    # Format weather
    weather_display = f"""
🌡️ Temperature: {weather['temperature']}°C
💧 Humidity: {weather['humidity']}%
🌤️ Condition: {weather['condition']}
💨 Wind Speed: {weather['wind_speed']} m/s
    """
    
    return diagnosis, weather_display, advice

# Build Phase 3 UI
app = gr.Interface(
    fn=analyze_plant,
    inputs=[
        gr.Image(type="pil", label="📸 Upload Leaf Image"),
        gr.Textbox(
            label="💬 Ask a question (optional)",
            placeholder="e.g. Why are my leaves turning yellow?"
        ),
        gr.Textbox(
            label="📍 Your City",
            placeholder="e.g. Noida, Delhi, Mumbai, London",
            value="Noida"
        )
    ],
    outputs=[
        gr.Textbox(label="🌿 Diagnosis Result"),
        gr.Textbox(label="🌦️ Current Weather"),
        gr.Textbox(label="🤖 AI Treatment Advice")
    ],
    title="🌿 Multimodal Plant Doctor",
    description="Upload a leaf image, ask a question, and get weather-aware AI plant disease diagnosis!"
)

if __name__ == "__main__":
    app.launch()