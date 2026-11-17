mahasiswa = {   
        "NO" : [1,2,3,4,5,],
        "NIM" : [11234,11345,12346,17513,212115],
        "NAME" : ["budi","irwan","bobi","siva","selvi"],
        "NILAI" : [80,70,50,85,65],
        "STATUS" : []
    }

for i in mahasiswa["NILAI"]:
    if i >= 80:
        mahasiswa['STATUS'].append("A")

    elif i >= 70:
        mahasiswa['STATUS'].append("B")

    elif i >= 60:
        mahasiswa['STATUS'].append("C")

    else:
        mahasiswa['STATUS'].append("D")

print(mahasiswa["NAME"], mahasiswa["STATUS"])