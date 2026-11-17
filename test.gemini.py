import time
from google import genai
from google.genai.errors import ServerError

client = genai.Client()

# Menggunakan model resmi terbaru: gemini-3.8-flash
model_name = "gemini-3.8-flash"
prompt = "Halo Gemini! Tolong jawab pesan ini dalam 1 kalimat pendek."

print(f"Mengirim permintaan ke {model_name}...")

# Mekanisme retry otomatis jika server sedang 503 UNAVAILABLE
for attempt in range(1, 4):
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        print("\n--- Berhasil Diterima ---")
        print(response.text)
        break
    except ServerError as e:
        print(f"Percobaan {attempt} gagal (Server busy/503). Meminta ulang dalam 3 detik...")
        time.sleep(3)
    except Exception as e:
        print(f"Error lain terjadi: {e}")
        break