#nama: M ANDHIKA TANGGUH P
#Kelas: XI TKJ 1
#Absen: 17
#Soal: Deskripsi Pekerjaan: Di sebuah toko online, Anda bertanggung jawab untuk menghitung diskon berdasarkan jumlah total belanjaan pelanggan. 

belanja = float(input("Masukkan total belanjaan pelanggan: "))

if belanja > 500000:
    diskon = 0.1
else:
    if 300000 <= belanja <= 500000:
        diskon = 0.05
    else:
        diskon = 0

total_setelah_diskon = belanja - (belanja * diskon)

print(f"Total belanjaan: {belanja}")

if diskon > 0:
    print(f"Diskon: {diskon * 100}%")
    print(f"Total setelah diskon: {total_setelah_diskon}")
else:
    print("Tidak ada diskon.")
