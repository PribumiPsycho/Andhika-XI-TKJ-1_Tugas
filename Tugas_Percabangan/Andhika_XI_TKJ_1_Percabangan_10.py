import tkinter as tk
from tkinter import messagebox

class TaskApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplikasi Daftar Tugas")
        self.master.geometry("400x400")

        self.tasks = []

        self.label = tk.Label(self.master, text="Daftar Tugas", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.listbox = tk.Listbox(self.master, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        self.refresh_listbox()

        self.btn_info = tk.Button(self.master, text="Info Jadwal", command=self.show_info)
        self.btn_info.pack(pady=5)

        self.btn_add = tk.Button(self.master, text="Tambah Jadwal", command=self.add_task)
        self.btn_add.pack(pady=5)

        self.btn_edit = tk.Button(self.master, text="Edit Jadwal", command=self.edit_task)
        self.btn_edit.pack(pady=5)

        self.btn_delete = tk.Button(self.master, text="Hapus Jadwal", command=self.delete_task)
        self.btn_delete.pack(pady=5)

        self.btn_update = tk.Button(self.master, text="Update Jadwal", command=self.update_task)
        self.btn_update.pack(pady=5)

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

    def show_info(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            selected_task = self.tasks[selected_task_index[0]]
            messagebox.showinfo("Info Jadwal", f"Jadwal untuk {selected_task}")

    def add_task(self):
        task = simpledialog.askstring("Tambah Jadwal", "Masukkan Jadwal Baru:")
        if task:
            self.tasks.append(task)
            self.refresh_listbox()

    def edit_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            selected_task = self.tasks[selected_task_index[0]]
            new_task = simpledialog.askstring("Edit Jadwal", "Edit Jadwal:", initialvalue=selected_task)
            if new_task:
                self.tasks[selected_task_index[0]] = new_task
                self.refresh_listbox()

    def delete_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            confirmation = messagebox.askyesno("Hapus Jadwal", "Apakah Anda yakin ingin menghapus jadwal ini?")
            if confirmation:
                del self.tasks[selected_task_index[0]]
                self.refresh_listbox()

    def update_task(self):
        self.refresh_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
