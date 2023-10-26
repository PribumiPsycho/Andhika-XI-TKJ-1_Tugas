#nama: M ANDHIKA TANGGUH P
#Kelas: XI TKJ 1
#Absen: 17
#Soal: Sebagai seorang manajer proyek, Anda harus menentukan apakah suatu proyek akan selesai tepat waktu atau terlambat.

from datetime import datetime

def cek_tepat_waktu(estimasi_selesai, target_selesai):
    if estimasi_selesai <= target_selesai:
        status = "Tepat waktu"
    else:
        status = "Terlambat"
    
    return status

def main():
    try:
        estimasi_selesai_str = input("Masukkan estimasi waktu selesai (format: YYYY-MM-DD): ")
        target_selesai_str = input("Masukkan tanggal target selesai (format: YYYY-MM-DD): ")

        estimasi_selesai = datetime.strptime(estimasi_selesai_str, "%Y-%m-%d")
        target_selesai = datetime.strptime(target_selesai_str, "%Y-%m-%d")

        status_proyek = cek_tepat_waktu(estimasi_selesai, target_selesai)

        print(f"Status proyek: {status_proyek}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
