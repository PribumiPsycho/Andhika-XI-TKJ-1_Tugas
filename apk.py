import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import DateEntry

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calendar App")

        self.event_list = []

        self.label = tk.Label(root, text="Event Date:")
        self.label.pack(pady=10)

        self.cal = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.cal.pack(pady=10)

        self.label2 = tk.Label(root, text="Event Title:")
        self.label2.pack(pady=10)

        self.event_entry = tk.Entry(root)
        self.event_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Event", command=self.add_event)
        self.add_button.pack(pady=20)

        self.view_button = tk.Button(root, text="View Events", command=self.view_events)
        self.view_button.pack(pady=20)

    def add_event(self):
        date = self.cal.get()
        event_title = self.event_entry.get()

        if date and event_title:
            event_date = datetime.strptime(date, "%m/%d/%y").date()
            self.event_list.append((event_date, event_title))
            messagebox.showinfo("Success", "Event added successfully!")
        else:
            messagebox.showwarning("Warning", "Please enter both date and event title.")

    def view_events(self):
        if not self.event_list:
            messagebox.showinfo("No Events", "No events to display.")
            return

        event_text = "Events:\n"
        for event in self.event_list:
            event_text += f"{event[0]}: {event[1]}\n"

        messagebox.showinfo("Event List", event_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
