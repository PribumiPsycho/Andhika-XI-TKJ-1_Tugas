#nama: M ANDHIKA TANGGUH P
#Kelas: XI TKJ 1
#Absen: 17
#Soal: Deskripsi Pekerjaan: Di sebuah toko online, Anda bertanggung jawab untuk menghitung diskon berdasarkan jumlah total belanjaan pelanggan. 

def hitung_diskon(total_belanja):
    if total_belanja > 500000:
        diskon = 0.1 * total_belanja
    elif 300000 <= total_belanja <= 500000:
        diskon = 0.05 * total_belanja
    else:
        diskon = 0
    
    return diskon

def main():
    try:
        total_belanja = float(input("Masukkan total belanja pelanggan: "))
        
        if total_belanja < 0:
            print("Total belanja tidak boleh negatif.")
            return
        
        diskon = hitung_diskon(total_belanja)
        
        if diskon > 0:
            print(f"Diskon yang diberikan: Rp {diskon:,.2f}")
            total_setelah_diskon = total_belanja - diskon
            print(f"Total setelah diskon: Rp {total_setelah_diskon:,.2f}")
        else:
            print("Tidak ada diskon untuk total belanja di bawah Rp 300.000.")

    except ValueError:
        print("Masukkan tidak valid. Pastikan Anda memasukkan angka sebagai total belanja.")

if __name__ == "__main__":
    main()
