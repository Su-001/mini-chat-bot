import os
from datetime import datetime
from mistralai import Mistral
from database import save_chat_to_db


api_key = os.environ["MISTRAL_API_KEY"]
print("Loaded API key:", api_key)  # TEMP

if not api_key:
    raise RuntimeError("MISTRAL_API_KEY is not set in the environment.")

model = "mistral-small"

client = Mistral(api_key=api_key)
User = input("Enter your name: ")
content = input(f"Hi {User}, How can I help you? \n")


chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": content
        
        },

    ]
    
)

response = chat_response.choices[0].message.content
print(response)

save_chat_to_db(User, content, response)