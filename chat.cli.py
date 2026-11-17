from google import genai
from google.genai.errors import APIError

client = genai.Client()
# Menggunakan chat session non-streaming
chat = client.chats.create(model="gemini-3.8-flash")

print("=" * 45)
print("  Gemini Interactive CLI (Ketik 'exit' untuk keluar)")
print("=" * 45 + "\n")

while True:
    try:
        user_input = input("Kamu > ").strip()
        
        if user_input.lower() in ['exit', 'quit', 'q']:
            print("Sampai jumpa!")
            break
            
        if not user_input:
            continue

        # Indikator loading visual sementara
        print("Gemini > Memproses...", end="\r", flush=True)

        # Mengirim pesan non-streaming (dapat respon utuh sekaligus)
        response = chat.send_message(user_input)
        
        # Timpa teks 'Memproses...' dengan jawaban dari Gemini
        print(f"Gemini > {response.text}\n")

    except APIError as e:
        print(f"\n[Error API]: {e}\n")
    except KeyboardInterrupt:
        print("\nSesi dihentikan.")
        break