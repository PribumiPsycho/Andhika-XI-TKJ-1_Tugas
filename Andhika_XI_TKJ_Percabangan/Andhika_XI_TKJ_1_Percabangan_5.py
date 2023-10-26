#nama: M ANDHIKA TANGGUH P

#Kelas: XI TKJ 1
#Absen: 17
#Soal: Sebagai seorang guru, Anda harus menentukan nilai akhir siswa berdasarkan nilai tugas dan ujian.

def tentukan_hasil(tugas, ujian):
    if tugas > 70 and ujian > 60:
        hasil = "Lulus"
    else:
        hasil = "Gagal"
    
    return hasil

def main():
    nilai_tugas = float(input("Masukkan nilai tugas (skala 0-100): "))
    nilai_ujian = float(input("Masukkan nilai ujian (skala 0-100): "))
    
    hasil_akhir = tentukan_hasil(nilai_tugas, nilai_ujian)

    print(f"Hasil akhir: {hasil_akhir}")

if __name__ == "__main__":
    main()
