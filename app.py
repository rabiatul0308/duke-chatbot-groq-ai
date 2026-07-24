"""Aplikasi utama untuk menguji koneksi API OpenAI."""

from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

# 1. Muat variabel dari file .env
load_dotenv()

# 2. Inisialisasi klien OpenAI
client = OpenAI()

print("Sedang menghubungkan ke OpenAI... Silakan tunggu.")

try:
    # 3. Kirim permintaan ke model GPT-4o-mini
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": "Katakan 'Sistem Siap!' jika Anda menerima pesan ini.",
            }
        ],
    )

    # 4. Tampilkan hasil jika sukses
    print("\n==============================")
    print("🎉 KONEKSI BERHASIL!")
    print("==============================")
    print("Respons AI:", response.choices.message.content)
    print("==============================\n")

except OpenAIError as e:
    # 5. Tangkap error spesifik dari OpenAI jika ada masalah
    print("\n❌ GAGAL TERHUBUNG!")
    print("Pesan Error:", e)
