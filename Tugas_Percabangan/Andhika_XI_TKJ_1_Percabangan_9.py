#nama: M ANDHIKA TANGGUH P
#Kelas: XI TKJ 1
#Absen: 17
#Soal:Sebagai seorang manajer proyek, Anda perlu menentukan apakah suatu proyek akan diluncurkan atau ditunda berdasarkan status persiapan.

def cek_status_persiapan(status_persiapan):
    if status_persiapan == "Siap":
        print("Proyek diluncurkan.")
    elif status_persiapan == "Tunda":
        print("Proyek ditunda.")
    else:
        print("Status persiapan tidak valid.")

def main():
    status_persiapan = input("Masukkan status persiapan proyek (Siap/Tunda): ")
    cek_status_persiapan(status_persiapan)

if __name__ == "__main__":
    main()
