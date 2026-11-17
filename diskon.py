hargaAwal = float(input("Harga awal: "))
hargaTotal = float(input("Harga total: "))
hari = input("Hari (pisahkan koma, kosongkan jika tidak ada): ").lower().split(",")
hari = [h.strip() for h in hari]

# diskon pertama + kedua
diskon_pertama = hargaAwal * 0.80
diskon_kedua = diskon_pertama * 0.90
print("Setelah diskon 1 + 2:", diskon_kedua)

# nested if: cek lebaran dulu, baru di dalamnya cek tahunbaru
if "lebaran" in hari:
    if "tahunbaru" in hari:
        diskontotal = diskon_kedua * 0.60 * 0.80   # lebaran + tahunbaru
    else:
        diskontotal = diskon_kedua * 0.60          # lebaran saja
elif "tahunbaru" in hari:
    diskontotal = diskon_kedua * 0.80              # tahunbaru saja
else:
    diskontotal = diskon_kedua                     # tidak ada hari spesial

print("Harga akhir:", diskontotal)


