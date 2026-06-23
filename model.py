from transformers import pipeline
from PIL import Image

# Plant-specific model trained on PlantVillage dataset
classifier = pipeline(
    "image-classification",
    model="nateraw/vit-base-beans"
)

def identify_disease(image_path):
    image = Image.open(image_path).convert("RGB")
    results = classifier(image)
    top_result = results[0]
    disease = top_result["label"]
    confidence = round(top_result["score"] * 100, 2)
    return disease, confidence