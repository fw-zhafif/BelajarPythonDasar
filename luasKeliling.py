import math

#input data
x = 5
y = 3 * x #Lebar untuk persegi panjang    

#perhitungan

#lingkaran
luas_lingkaran = math.pi * (x ** 2)
kel_lingkaran = 2 * math.pi * x

#segitiga
luas_segitiga = 0.5 * x * x
kel_segitiga = 3 * x

#persegi panjang
luas_persegi_panjang = x * y
kel_persegi_panjang = 2 * (x + y)

#bujur sangkar
luas_bujur_sangkar = x * x
kel_bujur_sangkar = 4 * x

#output
print("Program menghitung Luas Bangun Datar")
print(f"diketahui x = {x}")

print("A. Lingkaran")
print(f" Luas Lingkaran dengan jari-jari = x adalah {luas_lingkaran:.2f}")
print(f" Kelilingnya adalah {kel_lingkaran:.2f}")

print("B. Segitiga")
print(f" Luas Segitiga dengan panjang alas dan tinggi = x adalah {luas_segitiga:.2f}")
print(f" Kelilingnya adalah {kel_segitiga:.2f}")

print("C. Persegi Panjang")
print(f" Luas Persegi Panjang dengan panjang dan lebar = x dan y adalah {luas_persegi_panjang:.2f}")
print(f" Kelilingnya adalah {kel_persegi_panjang:.2f}")

print("D. Bujur Sangkar")
print(f" Luas Bujur Sangkar dengan sisi = x adalah {luas_bujur_sangkar:.2f}")
print(f" Kelilingnya adalah {kel_bujur_sangkar:.2f}")