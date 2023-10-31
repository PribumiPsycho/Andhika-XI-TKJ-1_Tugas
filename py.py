import tkinter as tk
from tkinter import messagebox, simpledialog

class JadwalPiketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Jadwal Piket")

        # Inisialisasi jadwal piket
        self.jadwal_piket = {}

        # Label
        self.label = tk.Label(root, text="Jadwal Piket:")
        self.label.pack(pady=10)

        # Listbox untuk menampilkan jadwal piket
        self.jadwal_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.jadwal_listbox.pack(pady=10)

        # Tombol Tambah Piket
        self.tambah_button = tk.Button(root, text="Tambah Piket", command=self.tambah_piket)
        self.tambah_button.pack()

        # Tombol Lihat Jadwal
        self.lihat_button = tk.Button(root, text="Lihat Jadwal", command=self.lihat_jadwal)
        self.lihat_button.pack()

    def tambah_piket(self):
        hari = simpledialog.askstring("Tambah Piket", "Masukkan Hari:")
        if not hari:
            return

        petugas = simpledialog.askstring("Tambah Piket", f"Masukkan Nama Petugas untuk {hari}:")
        if not petugas:
            return

        if hari not in self.jadwal_piket:
            self.jadwal_piket[hari] = [petugas]
        else:
            self.jadwal_piket[hari].append(petugas)

        self.update_jadwal_listbox()

    def lihat_jadwal(self):
        self.update_jadwal_listbox()

    def update_jadwal_listbox(self):
        self.jadwal_listbox.delete(0, tk.END)
        for hari, petugas in self.jadwal_piket.items():
            self.jadwal_listbox.insert(tk.END, f"{hari}: {', '.join(petugas)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = JadwalPiketApp(root)
    root.mainloop()
