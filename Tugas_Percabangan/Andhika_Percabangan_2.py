#nama: M ANDHIKA TANGGUH P
#Kelas: XI TKJ 1
#Absen: 17
#Soal: Sebagai seorang manajer proyek, Anda harus menentukan apakah suatu proyek akan selesai tepat waktu atau terlambat.

from datetime import datetime

def main():
    estimasi_selesai_str = input("Masukkan estimasi waktu selesai (format: YYYY-MM-DD): ")
    target_selesai_str = input("Masukkan tanggal target selesai (format: YYYY-MM-DD): ")

    estimasi_selesai = datetime.strptime(estimasi_selesai_str, "%Y-%m-%d")
    target_selesai = datetime.strptime(target_selesai_str, "%Y-%m-%d")

    if estimasi_selesai >= target_selesai:
        status_proyek = "Tepat waktu"
    else:
        status_proyek = "Terlambat"

    print(f"Status proyek: {status_proyek}")

if __name__ == "__main__":
    main()
