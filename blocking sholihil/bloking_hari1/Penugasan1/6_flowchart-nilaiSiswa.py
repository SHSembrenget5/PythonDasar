nilai_siswa = int(input("Masukkan nilai siswa: "))

if nilai_siswa >= 75:
    print("Tuntas")
else:
    mengulang = input("Apakah siswa perlu mengulang? (Ya/Tidak): ")
    if mengulang.lower() == "ya":
        print("Mengulang")
    else:
        print("Tidak tuntas")
