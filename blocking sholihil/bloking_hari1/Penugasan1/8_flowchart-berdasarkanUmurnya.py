umur = int(input("Masukkan umur Anda: "))

if umur <= 10:
    print("Anak-anak")
elif umur <= 18:
    print("Remaja")
elif umur <= 35:
    print("Dewasa")
elif umur <= 65:
    print("Parubayah")
else:
    print("Tua")
