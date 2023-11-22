import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
from datetime import datetime

class SchedulingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplikasi Penjadwalan")

        # Frame Utama
        self.frame_utama = tk.Frame(master)
        self.frame_utama.pack()

        self.conn = sqlite3.connect('penjadwalan.db')
        self.create_table()

        self.label = tk.Label(self.frame_utama, text="Rencana Anda")
        self.label.pack()

        self.listbox = tk.Listbox(self.frame_utama, width=50, height=10)
        self.listbox.pack(pady=10)

        # Frame Tombol
        self.frame_tombol = tk.Frame(self.frame_utama)
        self.frame_tombol.pack()

        self.button_info = tk.Button(self.frame_tombol, text="Info Rencana", command=self.info_rencana)
        self.button_info.pack(side=tk.LEFT, padx=5)

        self.button_tambah = tk.Button(self.frame_tombol, text="Tambah Rencana", command=self.tambah_rencana)
        self.button_tambah.pack(side=tk.LEFT, padx=5)

        self.button_edit = tk.Button(self.frame_tombol, text="Edit Rencana", command=self.edit_rencana)
        self.button_edit.pack(side=tk.LEFT, padx=5)

        self.button_hapus = tk.Button(self.frame_tombol, text="Hapus Rencana", command=self.hapus_rencana)
        self.button_hapus.pack(side=tk.LEFT, padx=5)

        self.update_listbox()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS rencana 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           judul TEXT, 
                           waktu TEXT)''')
        self.conn.commit()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM rencana")
        rencana_list = cursor.fetchall()
        for rencana in rencana_list:
            self.listbox.insert(tk.END, f"{rencana[1]} - {rencana[2]}")

    def info_rencana(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM rencana")
            rencana_list = cursor.fetchall()
            info_rencana = f"Judul: {rencana_list[selected_index[0]][1]}\nWaktu: {rencana_list[selected_index[0]][2]}"
            messagebox.showinfo("Info Rencana", info_rencana)
        else:
            messagebox.showwarning("Peringatan", "Pilih rencana terlebih dahulu!")

    def tambah_rencana(self):
        judul_rencana = simpledialog.askstring("Tambah Rencana", "Masukkan judul rencana:")
        waktu_rencana = simpledialog.askstring("Tambah Rencana", "Masukkan waktu rencana (Format: YYYY-MM-DD HH:MM):")

        try:
            datetime.strptime(waktu_rencana, "%Y-%m-%d %H:%M")
        except ValueError:
            messagebox.showerror("Error", "Format waktu tidak valid. Gunakan format YYYY-MM-DD HH:MM")
            return

        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO rencana (judul, waktu) VALUES (?, ?)", (judul_rencana, waktu_rencana))
        self.conn.commit()
        self.update_listbox()

    def edit_rencana(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            judul_lama, waktu_lama = self.listbox.get(selected_index)
            judul_baru = simpledialog.askstring("Edit Rencana", "Edit judul rencana:", initialvalue=judul_lama)
            waktu_baru = simpledialog.askstring("Edit Rencana", "Edit waktu rencana (Format: YYYY-MM-DD HH:MM):", initialvalue=waktu_lama)

            try:
                datetime.strptime(waktu_baru, "%Y-%m-%d %H:%M")
            except ValueError:
                messagebox.showerror("Error", "Format waktu tidak valid. Gunakan format YYYY-MM-DD HH:MM")
                return

            cursor = self.conn.cursor()
            cursor.execute("UPDATE rencana SET judul=?, waktu=? WHERE judul=? AND waktu=?", (judul_baru, waktu_baru, judul_lama, waktu_lama))
            self.conn.commit()
            self.update_listbox()
        else:
            messagebox.showwarning("Peringatan", "Pilih rencana terlebih dahulu!")

    def hapus_rencana(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            judul_lama, waktu_lama = self.listbox.get(selected_index)
            konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus rencana '{judul_lama} - {waktu_lama}'?")
            if konfirmasi:
                cursor = self.conn.cursor()
                cursor.execute("DELETE FROM rencana WHERE judul=? AND waktu=?", (judul_lama, waktu_lama))
                self.conn.commit()
                self.update_listbox()
        else:
            messagebox.showwarning("Peringatan", "Pilih rencana terlebih dahulu!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulingApp(root)
    root.mainloop()
