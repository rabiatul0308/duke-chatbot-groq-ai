"""Script untuk memeriksa daftar model Gemini yang aktif."""

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

try:
    client = genai.Client(api_key=api_key)
    print("Daftar model yang tersedia untuk akun Anda:\n")

    # Mengambil dan menampilkan semua model aktif dari server Google
    for model in client.models.list():
        print(f"- {model.name}")

except Exception as e:
    print("Gagal mengambil daftar model:", e)
