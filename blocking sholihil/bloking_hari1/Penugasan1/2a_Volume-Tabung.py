print("Program Python Hitung Volume Tabung")

pi    = 22/7
jari   = float(input("Masukan Jari-jarinya  : "))
tinggi = float(input("Masukan Tinggginya    : "))
volume = pi*jari*jari*tinggi

print("-----------------Hasilnya-----------------")
print("Volume Tabung         =","{:.2f}".format(volume))