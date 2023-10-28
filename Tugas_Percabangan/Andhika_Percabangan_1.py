#nama: M ANDHIKA TANGGUH P
#Kelas: XI TKJ 1
#Absen: 17
#Soal: Deskripsi Pekerjaan: Di sebuah toko online, Anda bertanggung jawab untuk menghitung diskon berdasarkan jumlah total belanjaan pelanggan. 

total_belanja = float(input("Masukkan total belanjaan pelanggan: "))

if total_belanja > 500000:
    diskon = 0.1
else:
    if 300000 <= total_belanja <= 500000:
        diskon = 0.05
    else:
        diskon = 0

total_setelah_diskon = total_belanja - (total_belanja * diskon)

print(f"Total belanjaan: {total_belanja}")

if diskon > 0:
    print(f"Diskon: {diskon * 100}%")
    print(f"Total setelah diskon: {total_setelah_diskon}")
else:
    print("Tidak ada diskon.")
