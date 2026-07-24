# PERBAIKAN: Impor pustaka pihak ketiga terlebih dahulu, lalu dotenv
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv

# Memuat variabel dari file .env ke dalam sistem
load_dotenv()

# Klien otomatis membaca OPENAI_API_KEY dari environment variable
client = OpenAI()

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Halo, tes koneksi proyek!"}]
    )
    print("Koneksi Sukses!")
    # Coba ambil konten dari struktur response yang umum
    try:
        content = response.choices[0].message.content
    except Exception:
        try:
            content = response.choices[0]["message"]["content"]
        except Exception:
            content = str(response)
    print("Respons:", content)
except OpenAIError as e:
    print("Error spesifik OpenAI terjadi:", e)
