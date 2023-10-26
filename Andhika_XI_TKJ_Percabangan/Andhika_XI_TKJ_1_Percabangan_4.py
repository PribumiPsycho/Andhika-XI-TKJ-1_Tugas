#nama: M ANDHIKA TANGGUH P
#Kelas: XI TKJ 1
#Absen: 17
#Soal: Sebagai seorang kasir di toko, Anda harus menghitung jumlah diskon berdasarkan total belanjaan pelanggan dan jenis anggota (anggota biasa atau anggota premium).

def hitung_diskon(total_belanja, status_anggota):
    if status_anggota == "premium":
        if total_belanja > 500000:
            diskon = 0.15
        else:
            diskon = 0.10
    elif status_anggota == "biasa":
        if total_belanja > 300000:
            diskon = 0.07
        else:
            diskon = 0
    else:
        print("Status anggota tidak valid.")
        diskon = 0
    
    return diskon

def main():
    total_belanja = float(input("Masukkan total belanjaan: "))
    status_anggota = input("Masukkan status anggota (premium/biasa): ").lower()

    diskon = hitung_diskon(total_belanja, status_anggota)
    total_setelah_diskon = total_belanja - (total_belanja * diskon)

    print(f"Total belanjaan: {total_belanja}")

    if diskon > 0:
        print(f"Diskon: {diskon * 100}%")
        print(f"Total setelah diskon: {total_setelah_diskon}")
    else:
        print("Tidak ada diskon.")

if __name__ == "__main__":
    main()
