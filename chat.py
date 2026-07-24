import os
from env import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
riwayat_chat = [
    {"role": "system", "content": "You are a helpful assistant that provides information and answers questions. Pretend you are a Duke of a grand estate, and respond in a formal and courteous manner."}
]

print ("Welcome to the Duke's Chat! Please enter your prompt below. Type 'stop' to exit.")


while True:
    user_prompt = input("Enter your prompt: ").strip()

   
    riwayat_chat.append({"role": "assistant", "content": "I am at your service, dear interlocutor. How may I assist you today?"})

    if user_prompt.lower() == "stop":
        print("Farewell, dear interlocutor. May your endeavors be prosperous.")
        break

    if not user_prompt:
        continue

    riwayat_chat.append({"role": "user", "content": user_prompt})

    try:
       response = client.chat.completions.create(
               model="llama-3.3-70b-versatile",
            messages=riwayat_chat,
            temperature=0.7,
            max_tokens=100,
            
 )

response_content = response.choices[0].message.content
riwayat_chat.append({"role": "assistant", "content": response_content})

except Exception as e:
        print(f"An error occurred: {e}")