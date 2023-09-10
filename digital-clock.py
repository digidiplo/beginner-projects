import time
from datetime import datetime, timezone, timedelta
import tkinter as tk

class Clock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tutti-Fruit Digital Clock")
        self.root.geometry("300x300")
        self.root.resizable(True, True)
        self.root.configure(bg="#EDCF8E")

        # Clock label
        self.label = tk.Label(self.root, font=('Arial', 40, 'bold'), background='#EDCF8E', foreground='#BA7BA1')
        self.label.pack(anchor='center')

        # Date label
        self.date_label = tk.Label(self.root, font=('Arial', 20), background='#EDCF8E', foreground='#BA7BA1')
        self.date_label.pack(anchor='s')

        # Time zone dropdown
        self.time_zone_var = tk.StringVar(self.root)
        self.time_zone_var.set("UTC")  # Default value
        self.time_zones = ["UTC", "Europe/London", "Asia/Tokyo"]  # Sample time zones
        self.time_zone_dropdown = tk.OptionMenu(self.root, self.time_zone_var, *self.time_zones)
        self.time_zone_dropdown.config(bg='#EDCF8E', fg='#BA7BA1')
        self.time_zone_dropdown.pack(anchor='n')

    def update_time(self):
        # Update the time
        current_time = time.localtime()
        formatted_time = f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}"
        self.label.config(text=formatted_time)

        # Update the date
        self.update_date()

        # Update the time zone and display
        current_time = self.time_zone()
        formatted_time = f"{current_time.hour}:{current_time.minute}:{current_time.second}"
        self.label.config(text=formatted_time)

        self.root.after(1000, self.update_time)


    def update_date(self):
        current_date = time.strftime("%Y-%m-%d %A")
        self.date_label.config(text=current_date)

    def time_zone(self):
        selected_zone = self.time_zone_var.get()
        if selected_zone == "UTC":
            offset = timezone.utc
        elif selected_zone == "Europe/London":
            offset = timezone(timedelta(hours=1))
        elif selected_zone == "Asia/Tokyo":
            offset = timezone(timedelta(hours=9))

        current_time = datetime.now(offset)
        return current_time


# Create an instance of your Clock class
clock_app = Clock()
clock_app.update_time()  # This will kickstart the time, date, and time zone updates

# Start the Tkinter event loop
clock_app.root.mainloop()
