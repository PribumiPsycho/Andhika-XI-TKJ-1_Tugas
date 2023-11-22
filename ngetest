import calendar
import tkinter as tk
from tkinter import ttk

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App")

        self.year_var = tk.StringVar()
        self.month_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Frame untuk input tahun dan bulan
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.pack()

        # Label dan Combobox untuk tahun
        year_label = ttk.Label(input_frame, text="Year:")
        year_label.grid(row=0, column=0, padx=5, pady=5)
        year_combobox = ttk.Combobox(input_frame, textvariable=self.year_var, values=list(range(2022, 2030)))
        year_combobox.grid(row=0, column=1, padx=5, pady=5)
        year_combobox.set(2022)  # Tahun default

        # Label dan Combobox untuk bulan
        month_label = ttk.Label(input_frame, text="Month:")
        month_label.grid(row=0, column=2, padx=5, pady=5)
        month_combobox = ttk.Combobox(input_frame, textvariable=self.month_var, values=list(range(1, 13)))
        month_combobox.grid(row=0, column=3, padx=5, pady=5)
        month_combobox.set(1)  # Bulan default

        # Button untuk menampilkan kalender
        show_button = ttk.Button(input_frame, text="Show Calendar", command=self.show_calendar)
        show_button.grid(row=0, column=4, padx=5, pady=5)

        # Frame untuk menampilkan kalender
        cal_frame = ttk.Frame(self.root, padding="10")
        cal_frame.pack()

        # Menampilkan kalender default
        self.show_calendar()

    def show_calendar(self):
        selected_year = int(self.year_var.get())
        selected_month = int(self.month_var.get())

        # Membersihkan frame sebelum menampilkan kalender baru
        for widget in self.root.winfo_children():
            if widget.winfo_class() == "TFrame":
                widget.destroy()

        # Frame untuk menampilkan kalender
        cal_frame = ttk.Frame(self.root, padding="10")
        cal_frame.pack()

        cal_content = calendar.monthcalendar(selected_year, selected_month)
        for i in range(0, len(cal_content)):
            for j in range(0, 7):
                day = cal_content[i][j]
                if day == 0:
                    cal_label = tk.Label(cal_frame, text="   ")
                else:
                    cal_label = tk.Label(cal_frame, text=f" {day} ", relief="solid")

                cal_label.grid(row=i, column=j)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
