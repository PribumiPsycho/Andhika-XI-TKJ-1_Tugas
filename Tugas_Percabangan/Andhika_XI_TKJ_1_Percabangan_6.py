#nama: M ANDHIKA TANGGUH P
#Kelas: XI TKJ 1
#Absen: 17
#Soal:Sebagai seorang analis data, Anda harus mengkategorikan produk berdasarkan penjualan bulanan.

def kategorikan_produk(penjualan):
    if penjualan > 1000:
        kategori = "Produk Terlaris"
    elif 500 <= penjualan <= 1000:
        kategori = "Produk Populer"
    else:
        kategori = "Produk Biasa"
    
    return kategori

def main():
    try:
        penjualan = int(input("Masukkan jumlah penjualan bulanan produk: "))

        if penjualan < 0:
            raise ValueError("Jumlah penjualan tidak boleh kurang dari 0.")

        kategori_produk = kategorikan_produk(penjualan)

        print(f"Kategori produk: {kategori_produk}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
