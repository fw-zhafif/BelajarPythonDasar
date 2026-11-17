BATAS_PENGHASILAN_KELUARGA = 4_000_000   # penghasilan gabungan orang tua / bulan
BATAS_PENGHASILAN_PER_KAPITA = 750_000   # penghasilan per anggota keluarga / bulan
BATAS_TAHUN_LULUS = 2                    # maksimal lulus 2 tahun terakhir

# --- Input ---
tahun_lulus_lalu = int(input("Berapa tahun lalu lulus SMA/SMK? "))
status = input("Punya KIP / terdaftar DTKS? (y/n): ").strip().lower() == "y"
penghasilan = int(input("Penghasilan gabungan orang tua per bulan (Rp): "))
anggota = int(input("Jumlah anggota keluarga: "))

# --- Pengecekan ---
if anggota < 1:
    # dicek paling awal supaya tidak terjadi pembagian dengan nol
    hasil = "DATA TIDAK VALID: jumlah anggota keluarga minimal 1."
else:
    penghasilan_per_kapita = penghasilan / anggota

    if tahun_lulus_lalu > BATAS_TAHUN_LULUS:
        hasil = "TIDAK LAYAK: lulus lebih dari 2 tahun lalu."
    elif status:
        hasil = "LAYAK: terdaftar penerima KIP / DTKS (jalur prioritas)."
    elif penghasilan <= BATAS_PENGHASILAN_KELUARGA:
        hasil = "LAYAK: penghasilan keluarga di bawah batas."
    elif penghasilan_per_kapita <= BATAS_PENGHASILAN_PER_KAPITA:
        hasil = "LAYAK: penghasilan per kapita di bawah batas."
    else:
        hasil = "TIDAK LAYAK: penghasilan melebihi batas dan tidak terdaftar DTKS/KIP."

# --- Output ---
print(hasil)