#nama: M ANDHIKA TANGGUH P
#Kelas: XI TKJ 1
#Absen: 17
#Soal: Sebagai seorang administrator sistem, Anda perlu memutuskan apakah suatu sistem perlu di-restart setelah pembaruan perangkat lunak.

def cek_pembaruan(memerlukan_restart):
    if memerlukan_restart:
        print("Sistem perlu di-restart.")
    else:
        print("Sistem tidak perlu di-restart.")

def main():
    perlu_di_restart = input("Apakah pembaruan memerlukan restart? (ya/tidak): ").lower()
    
    if perlu_di_restart == "ya":
        cek_pembaruan(True)
    elif perlu_di_restart == "tidak":
        cek_pembaruan(False)
    else:
        print("Masukan tidak valid. Harap masukkan 'ya' atau 'tidak'.")

if __name__ == "__main__":
    main()
