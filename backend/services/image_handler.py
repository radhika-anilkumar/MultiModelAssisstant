import io
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import pytesseract
from ollama import Client
 
client = Client(host='http://localhost:11434')
 
# Load BLIP model for image captioning
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
 
def handle_image_query(file_bytes: bytes) -> str:
    # Convert image bytes to PIL image
    image = Image.open(io.BytesIO(file_bytes)).convert('RGB')
 
    # Try OCR first
    extracted_text = pytesseract.image_to_string(image).strip()
 
    if not extracted_text:  # No text detected
        # Generate a caption instead
        inputs = processor(images=image, return_tensors="pt")
        output_ids = blip_model.generate(**inputs)
        extracted_text = processor.decode(output_ids[0], skip_special_tokens=True)
        query_text = f"Describe this image: {extracted_text}"
    else:
        query_text = f"Summarize this text: {extracted_text}"
 
    # Send text/caption to LLM
    response = client.chat(model="llama2", messages=[
        {"role": "user", "content": query_text}
    ])
    return response['message']['content']