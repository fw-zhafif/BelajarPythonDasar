alpro = { "no" : [1, 2, 3, 4, 5, 6],
          "nama" : ['budi', 'ani', 'silvi', 'bobi', 'irma', 'romi'],
          "nilai" : { 'uts' : [42, 46, 73, 23, 56, 45],
                      'uas' : [34, 25, 52, 35, 64, 78],
                      'partisipasi' : [80, 75, 0, 50, 75, 90],
                      'total' : [] , # uts*30%, uas*30%, tugas*40%
                      'grade' : []
          }
}

#menampilkan/mengakses nilai uts untuk nama mahasiswa tertentu
print("\n== Nilai UTS ==")
for i in range(len(alpro['nama'])) :
    print('Nama:' , alpro['nama'][i], "| Nilai UTS:" , alpro['nilai']['uts'][i])

#menampilkan/mengakses nilai uas untuk nama mahasiswa tertentu
print("\n== Nilai UAS ==")
for i in range(len(alpro['nama'])) :
    print('Nama:' , alpro['nama'][i], "| Nilai UAS:" , alpro['nilai']['uas'][i])

#mengisi dan mencari nilai total
for i in range(len(alpro['nama'])) :
    nilai_uts = alpro['nilai']['uts'][i] 
    nilai_uas = alpro['nilai']['uas'][i]
    nilai_partisipasi = alpro['nilai']['partisipasi'][i]

    nilai_total = (nilai_uts * 0.3) + (nilai_uas * 0.3) + (nilai_partisipasi * 0.4)

#memasukan nilai total ke dalam list total
    alpro['nilai']['total'].append(nilai_total)

#print
print("\n== Nilai Total ==")
for i in range(len(alpro['nama'])) :
    print('Nama:' , alpro['nama'][i], "| Nilai total:" , alpro['nilai']['total'][i])

for i in range(len(alpro['nama'])) :
    if alpro['nilai']['total'][i] >= 80:
        alpro['nilai']['grade'].append("A") 
    elif alpro['nilai']['total'][i] >= 70:
        alpro['nilai']['grade'].append("B")
    elif alpro['nilai']['total'][i] >= 60:
        alpro['nilai']['grade'].append("C")
    elif alpro['nilai']['total'][i] >= 50:
        alpro['nilai']['grade'].append("D")
    else:
        alpro['nilai']['grade'].append("E")

print("\n== Nilai Grade ==")
for i in range(len(alpro['nama'])) :
    print('Nama:' , alpro['nama'][i], '| Grade:' ,alpro['nilai']['grade'][i])