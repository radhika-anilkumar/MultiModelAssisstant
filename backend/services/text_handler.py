from ollama import Client
 
client = Client(host='http://localhost:11434')  # default Ollama endpoint
 
def get_llm_response(prompt: str) -> str:
    response = client.chat(model="llama2", messages=[
        {"role": "user", "content": prompt}
    ])
    return response['message']['content']