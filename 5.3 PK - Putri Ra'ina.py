print("Program penghitung IPS mahasiswa")

# Fungsi untuk menghitung IPS
def hitung_ips(jumlah_mata_kuliah, total_nilai):
    ips = total_nilai / jumlah_mata_kuliah if jumlah_mata_kuliah > 0 else 0
    return ips

# Fungsi utama
def main():
    # Input jumlah mata kuliah
    jumlah_mata_kuliah = int(input("Berapa jumlah mata kuliah? "))
    
    total_nilai = 0
    
    # Input nilai untuk setiap mata kuliah
    for i in range(jumlah_mata_kuliah):
        nilai = input(f"Nilai MK {i + 1}: ").upper()
        
        # Kontrol percabangan untuk menentukan nilai
        if nilai == 'A':
            nilai_angka = 4
        elif nilai == 'B':
            nilai_angka = 3
        elif nilai == 'C':
            nilai_angka = 2
        elif nilai == 'D':
            nilai_angka = 1
        else:
            print("Nilai tidak valid, dianggap 0.")
            nilai_angka = 0
        
        total_nilai += nilai_angka
    
    # Hitung IPS
    ips = hitung_ips(jumlah_mata_kuliah, total_nilai)
    
    # Output hasil IPS
    print(f"Nilai IPS anda semester ini {ips:.2f}")
    
# Menjalankan program
if __name__ == "__main__":
    main()