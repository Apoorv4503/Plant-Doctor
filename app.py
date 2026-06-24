import gradio as gr
from model import identify_disease
from llm import get_treatment_advice

def analyze_plant(image, question):
    """
    Takes image + optional question
    Returns disease + AI treatment advice
    """
    # Save uploaded image
    image_path = "temp_leaf.jpg"
    image.save(image_path)
    
    # Get disease from vision model
    disease, confidence = identify_disease(image_path)
    
    # Get smart advice from Groq
    advice = get_treatment_advice(disease, confidence)
    
    # Format diagnosis result
    diagnosis = f"""
🌿 Disease Detected: {disease}
📊 Confidence: {confidence}%
    """
    
    return diagnosis, advice

# Build updated Gradio UI
app = gr.Interface(
    fn=analyze_plant,
    inputs=[
        gr.Image(type="pil", label="Upload Leaf Image"),
        gr.Textbox(label="Ask a question (optional)", 
                   placeholder="e.g. Why are my leaves turning yellow?")
    ],
    outputs=[
        gr.Textbox(label="Diagnosis Result"),
        gr.Textbox(label="AI Treatment Advice")
    ],
    title="🌿 Plant Doctor - Phase 2",
    description="Upload a leaf image and get AI-powered disease diagnosis + treatment advice"
)

if __name__ == "__main__":
    app.launch()