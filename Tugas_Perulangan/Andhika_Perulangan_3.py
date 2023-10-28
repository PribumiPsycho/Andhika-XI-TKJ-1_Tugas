#nama: M ANDHIKA TANGGUH P
#Kelas: XI TKJ 1
#Absen: 17
#Soal: Seorang pedagang memiliki 100 buah apel. Setiap harinya, ia menjual 10% dari jumlah apel yang tersisa. Buatlah program yang menghitung berapa hari yang dibutuhkan agar sisa apel kurang dari 20 buah.

jumlah_apel = 100
hari = 0

while jumlah_apel >= 20:
    hari += 1
    penjualan = 0.10 * jumlah_apel
    jumlah_apel -= penjualan

print("Dibutuhkan", hari, "hari agar sisa apel kurang dari 20 buah.")
