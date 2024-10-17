import math

# Menghitung perkalian dua bilangan tanpa operator *
arr = [7, 5]
d = math.prod(arr)
print(d)

# Menghitung pemangkatan dua bilangan tanpa operator **
c = pow(4, 8)
print (c)

# Memeriksa apakah suatu bilangan adalah prima
def cek_prima (angka):
    if angka > 1:
        for i in range (2,
int(angka ** 0.5)+1):
            if angka %i == 0:
                return False
            return True
        return False
angka = int(input("Masukkan sebuah angka: "))
if cek_prima(angka):
    print(f"{angka} merupakan bilangan prima.")
else:
    print(f"{angka} bukan bilangan prima.")