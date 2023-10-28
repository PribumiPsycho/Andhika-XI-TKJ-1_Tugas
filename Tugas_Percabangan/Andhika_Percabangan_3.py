#nama: M ANDHIKA TANGGUH P
#Kelas: XI TKJ 1
#Absen: 17
#Soal: Sebagai seorang sistem administrator, Anda bertanggung jawab untuk memeriksa apakah suatu file di server sudah ada atau belum sebelum menggantinya.

nama_file = "data.txt"
daftar_file_di_server = ["file1.txt", "file2.txt", "data.txt", "file3.txt"]

if nama_file in daftar_file_di_server:
    print("File sudah ada")
else:
    print("File belum ada")
