import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import simpledialog
from datetime import datetime

class AplikasiKalender:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplikasi Kalender")

        # Buat database SQLite untuk menyimpan jadwal
        self.conn = sqlite3.connect('kalender.db')
        self.create_table()

        self.label = tk.Label(master, text="Jadwal Anda")
        self.label.pack()

        self.listbox = tk.Listbox(master)
        self.listbox.pack()

        self.button_info = tk.Button(master, text="Info Jadwal", command=self.info_jadwal)
        self.button_info.pack()

        self.button_tambah = tk.Button(master, text="Tambah Jadwal", command=self.tambah_jadwal)
        self.button_tambah.pack()

        self.button_edit = tk.Button(master, text="Edit Jadwal", command=self.edit_jadwal)
        self.button_edit.pack()

        self.button_hapus = tk.Button(master, text="Hapus Jadwal", command=self.hapus_jadwal)
        self.button_hapus.pack()

        self.update_listbox()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS jadwal 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           judul TEXT, 
                           waktu TEXT)''')
        self.conn.commit()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM jadwal")
        jadwal_list = cursor.fetchall()
        for jadwal in jadwal_list:
            self.listbox.insert(tk.END, f"{jadwal[1]} - {jadwal[2]}")

    def info_jadwal(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM jadwal")
            jadwal_list = cursor.fetchall()
            info_jadwal = f"Judul: {jadwal_list[selected_index[0]][1]}\nWaktu: {jadwal_list[selected_index[0]][2]}"
            messagebox.showinfo("Info Jadwal", info_jadwal)
        else:
            messagebox.showwarning("Peringatan", "Pilih jadwal terlebih dahulu!")

    def tambah_jadwal(self):
        judul_jadwal = simpledialog.askstring("Tambah Jadwal", "Masukkan judul jadwal:")
        waktu_jadwal = simpledialog.askstring("Tambah Jadwal", "Masukkan waktu jadwal (Format: YYYY-MM-DD HH:MM):")

        try:
            datetime.strptime(waktu_jadwal, "%Y-%m-%d %H:%M")
        except ValueError:
            messagebox.showerror("Error", "Format waktu tidak valid. Gunakan format YYYY-MM-DD HH:MM")
            return

        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO jadwal (judul, waktu) VALUES (?, ?)", (judul_jadwal, waktu_jadwal))
        self.conn.commit()
        self.update_listbox()

    def edit_jadwal(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            judul_baru = simpledialog.askstring("Edit Jadwal", "Edit judul jadwal:")
            waktu_baru = simpledialog.askstring("Edit Jadwal", "Edit waktu jadwal (Format: YYYY-MM-DD HH:MM):")

            try:
                datetime.strptime(waktu_baru, "%Y-%m-%d %H:%M")
            except ValueError:
                messagebox.showerror("Error", "Format waktu tidak valid. Gunakan format YYYY-MM-DD HH:MM")
                return

            cursor = self.conn.cursor()
            cursor.execute("UPDATE jadwal SET judul=?, waktu=? WHERE id=?", (judul_baru, waktu_baru, selected_index[0] + 1))
            self.conn.commit()
            self.update_listbox()
        else:
            messagebox.showwarning("Peringatan", "Pilih jadwal terlebih dahulu!")

    def hapus_jadwal(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus jadwal ini?")
            if konfirmasi:
                cursor = self.conn.cursor()
                cursor.execute("DELETE FROM jadwal WHERE id=?", (selected_index[0] + 1,))
                self.conn.commit()
                self.update_listbox()
        else:
            messagebox.showwarning("Peringatan", "Pilih jadwal terlebih dahulu!")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiKalender(root)
    root.mainloop()
