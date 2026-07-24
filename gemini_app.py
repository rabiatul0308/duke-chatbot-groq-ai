"""Aplikasi pengujian koneksi menggunakan Google Gemini API terbaru."""

import os
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError

# 1. Muat variabel dari file .env
load_dotenv()

# 2. Ambil kunci dari environment
api_key = os.environ.get("GEMINI_API_KEY")

print("Sedang menghubungkan ke Google Gemini... Silakan tunggu.")

try:
    # 3. Inisialisasi klien Gemini SDK Baru
    client = genai.Client(api_key=api_key)

    # 4. Gunakan alias model paling mutakhir & stabil
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents="Halo Gemini, katakan 'Sistem Siap!' jika terkoneksi.",
    )

    # 5. Tampilkan hasil
    print("\n==============================")
    print("🎉 KONEKSI GEMINI BERHASIL!")
    print("==============================")
    print("Respons AI:", response.text)
    print("==============================\n")

except APIError as e:
    print("\n❌ GAGAL TERHUBUNG!")
    print("Pesan Error Gemini:", e)
