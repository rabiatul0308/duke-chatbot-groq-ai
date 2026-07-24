import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

riwayat_chat = [
    {
        "role": "system",
        "content": (
            "You are a helpful assistant that provides information and answers"
            " questions. Pretend you are a Duke of a grand estate, and respond"
            " in a formal and courteous manner."
        ),
    }
]

print(
    "Welcome to the Duke's Chat! Please enter your prompt below.\n"
    "Type 'stop' to exit, or 'clear' to clean the screen.\n"
)

while True:
    user_prompt = input("Enter your prompt: ").strip()

    # Perintah keluar
    if user_prompt.lower() == "stop":
        print(
            "Farewell, dear interlocutor. May your endeavors be prosperous."
        )
        break

    # Perintah bersihin layar terminal (opsional dari user)
    if user_prompt.lower() == "clear":
        os.system("cls" if os.name == "nt" else "clear")
        continue

    # Skip jika input kosong
    if not user_prompt:
        continue

    # Masukkan input user ke riwayat
    riwayat_chat.append({"role": "user", "content": user_prompt})

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=riwayat_chat,
            temperature=0.7,
            max_tokens=100,
        )

        response_content = response.choices[0].message.content
        print(f"\nDuke: {response_content}\n")

        # Simpan respons ke riwayat
        riwayat_chat.append(
            {"role": "assistant", "content": response_content}
        )

    except Exception as e:
        print(f"An error occurred: {e}")