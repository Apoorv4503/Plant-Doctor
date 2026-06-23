import gradio as gr
from model import identify_disease

def analyze_plant(image):
    """
    Main function - takes image, returns result
    """
    # Save the uploaded image temporarily
    image_path = "temp_leaf.jpg"
    image.save(image_path)
    
    # Get disease prediction
    disease, confidence = identify_disease(image_path)
    
    # Format the result nicely
    result = f"""
    🌿 Disease Detected: {disease}
    📊 Confidence: {confidence}%
    """
    
    return result

# Build the Gradio UI
app = gr.Interface(
    fn=analyze_plant,
    inputs=gr.Image(type="pil", label="Upload Leaf Image"),
    outputs=gr.Textbox(label="Diagnosis Result"),
    title="🌿 Plant Doctor - Phase 1",
    description="Upload a leaf image to detect plant disease"
)

# Run the app
if __name__ == "__main__":
    app.launch()