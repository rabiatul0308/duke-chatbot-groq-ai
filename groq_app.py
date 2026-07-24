"""Aplikasi pengujian koneksi menggunakan Groq Cloud API."""

import os
from dotenv import load_dotenv
from groq import Groq

# 1. Memuat konfigurasi kunci dari berkas .env
load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")

print("Sedang menghubungkan ke Groq Cloud... Silakan tunggu.")

try:
    # 2. Inisialisasi klien resmi Groq
    client = Groq(api_key=api_key)

    # 3. Kirim pesan menggunakan model Llama yang stabil dan gratis
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": "Katakan 'Sistem Groq Siap!' jika Anda menerima pesan ini.",
            }
        ],
    )

    # 4. Cetak hasil respons sukses
    print("\n==============================")
    print("🎉 KONEKSI GROQ BERHASIL!")
    print("==============================")
    print("Respons AI:", completion.choices[0].message.content)
    print("==============================\n")

except Exception as e:
    print("\n❌ GAGAL TERHUBUNG!")
    print("Pesan Error:", e)
