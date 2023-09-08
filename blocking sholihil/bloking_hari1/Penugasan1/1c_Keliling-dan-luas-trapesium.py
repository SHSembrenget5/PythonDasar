print('##  Program Python Menghitung Luas dan Keliling Trapesium  ##')
print('================================================')
print()
  
sisi1 = float(input('Input panjang sisi 1: '))
sisi2 = float(input('Input panjang sisi 2: '))
sisi3 = float(input('Input panjang sisi 3: '))
sisi4 = float(input('Input panjang sisi 4: '))
tinggi = float(input('Input tinggi : '))
 
luas = 0.5 * (sisi2 + sisi4) * tinggi;
keliling = sisi1 + sisi2 + sisi3 + sisi4;
 
print('Luas trapesium = ',round(luas,2))
print('Keliling = ', keliling)