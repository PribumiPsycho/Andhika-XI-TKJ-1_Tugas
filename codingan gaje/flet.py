import tkinter as tk
from tkinter import Calendar

def show_calendar():
    top = tk.Toplevel(root)
    cal = Calendar(top, selectmode='day', year=2023, month=11, day=22)
    cal.pack(padx=10, pady=10)

    def get_date():
        selected_date = cal.get_date()
        entry_date.delete(0, tk.END)
        entry_date.insert(0, selected_date)
        top.destroy()

    btn_select_date = tk.Button(top, text="Select Date", command=get_date)
    btn_select_date.pack(pady=10)

root = tk.Tk()
root.title("Jadwal App")

# Fungsi untuk menambahkan jadwal
def add_schedule():
    event = entry_event.get()
    date = entry_date.get()

    if event and date:
        schedule_text = f"Event: {event}, Date: {date}"
        listbox_schedule.insert(tk.END, schedule_text)
        entry_event.delete(0, tk.END)
        entry_date.delete(0, tk.END)

# Membuat antarmuka grafis
label_event = tk.Label(root, text="Event:")
label_event.pack(pady=5)
entry_event = tk.Entry(root)
entry_event.pack(pady=5)

label_date = tk.Label(root, text="Date:")
label_date.pack(pady=5)
entry_date = tk.Entry(root)
entry_date.pack(pady=5)

btn_show_calendar = tk.Button(root, text="Show Calendar", command=show_calendar)
btn_show_calendar.pack(pady=10)

btn_add_schedule = tk.Button(root, text="Add Schedule", command=add_schedule)
btn_add_schedule.pack(pady=10)

listbox_schedule = tk.Listbox(root)
listbox_schedule.pack(pady=10)

root.mainloop()
