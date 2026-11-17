total_belanja = float(input("Masukkan total belanja: Rp"))

member = input("Apakah Anda member? (ya/tidak): ")
while member != "ya" and member != "tidak":
    print("Jawaban tidak valid, hanya boleh 'ya' atau 'tidak'.")
    member = input("Apakah Anda member? (ya/tidak): ")

tanggal_kembar = input("Apakah hari ini tanggal kembar? (ya/tidak): ")
while tanggal_kembar != "ya" and tanggal_kembar != "tidak":
    print("Jawaban tidak valid, hanya boleh 'ya' atau 'tidak'.")
    tanggal_kembar = input("Apakah hari ini tanggal kembar? (ya/tidak): ")

diskon = 0


if member == "ya" and tanggal_kembar == "ya":
    diskon = 0.30
elif member == "ya":
    diskon = 0.20
elif tanggal_kembar == "ya":
    diskon = 0.10
else:
    diskon = 0


potongan = total_belanja * diskon
total_bayar = total_belanja - potongan

print("Total belanja: Rp", total_belanja)
print("Diskon: ", diskon * 100, "%")
print("Potongan harga: Rp", potongan)
print("Total yang harus dibayar: Rp", total_bayar)