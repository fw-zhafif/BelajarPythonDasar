i = 1
total = 0
daftar_barang = []

while True:
    nama_barang = input(f"masukkan nama barang dengan nomor seri ke-{i}: ")
    input_hg = input(f"harga {nama_barang}? = Rp.")

    harga = int(input_hg)
    total += harga
    daftar_barang.append((nama_barang,harga))

    print(f"barang dengan nomor seri ke-{i}: {nama_barang} berharga Rp {harga}")

    i += 1

    while True:
        stop = input("masih ada barang yang ingin di scan ? 'Y/T' (ketik ya untuk lanjut, tidak jika sudah selesai): ").strip().lower()
        if stop == 'ya' or stop == 'tidak':
            break
        else:
            print("Input tidak valid! Hanya boleh mengetik 'ya' atau 'tidak'.")

    if stop == 'tidak':
        break

print("\n=== Rincian Belanjaan Anda ===")
for nomor, (nama, hrg) in enumerate(daftar_barang, start=1):
    print(f"{nomor}. {nama} : Rp {hrg}")

print(f"Total seluruh belanjaan anda adalah: Rp {total}")

if total >= 100:
    print("Terimakasih sudah berbelanja kang sultan baik hati ganteng")
elif total >= 50:
    print("Terimakasih sudah berbelanja pak juragan toke sawit ")
else:
    print("Terimakasih sudah berbelanja wahai rakyat yang biasa aja")
        