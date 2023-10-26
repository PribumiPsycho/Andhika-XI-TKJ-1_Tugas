#nama: M ANDHIKA TANGGUH P
#Kelas: XI TKJ 1
#Absen: 17
#Soal: Sebagai seorang pengembang perangkat lunak, Anda perlu membuat program sederhana yang menghitung bonus tahunan karyawan berdasarkan performa mereka.

def hitung_bonus(performa, gaji_tahunan):
    bonus = (
        0.2 * gaji_tahunan if performa == 5 else
        0.1 * gaji_tahunan if performa == 4 else
        0.05 * gaji_tahunan if performa == 3 else
        0.02 * gaji_tahunan if performa == 2 else
        0
    )
    return bonus

def main():
    try:
        performa = int(input("Masukkan nilai performa karyawan (1-5): "))
        gaji_tahunan = float(input("Masukkan gaji tahunan karyawan: "))

        if not (1 <= performa <= 5) or gaji_tahunan < 0:
            raise ValueError("Masukan tidak valid.")

        bonus = hitung_bonus(performa, gaji_tahunan)

        print(f"Bonus tahunan: {bonus}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
