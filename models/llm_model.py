from transformers import pipeline
 
# Load on startup
llm = pipeline("text-generation", model="gpt2")
 
def get_llm_response(prompt: str):
    return llm(prompt, max_length=100)[0]['generated_text']