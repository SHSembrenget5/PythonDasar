# Input
nama = input("Masukkan nama: ")
gaji_pokok = float(input("Masukkan gaji pokok: "))

# Proses
tunjangan = 0.2 * gaji_pokok
pajak = 0.15 * (gaji_pokok + tunjangan)
gaji_bersih = gaji_pokok + tunjangan - pajak

# Output
print("Nama:", nama)
print("Gaji Bersih:", gaji_bersih)
