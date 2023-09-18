import tkinter as tk
import time
import winsound

def set_alarm():
    alarm_time = entry.get()
    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
    except ValueError:
        result_label.config(text="Invalid time format (HH:MM)")
        return

    while True:
        current_time = time.localtime()
        current_hour, current_minute = current_time.tm_hour, current_time.tm_min

        current_time_str = time.strftime("%H:%M:%S")
        clock_label.config(text=current_time_str)

        if (current_hour, current_minute) == (alarm_hour, alarm_minute):
            result_label.config(text="Time to wake up!")
            winsound.Beep(1000, 1000)  # Frequency: 1000 Hz, Duration: 1000 ms
            break

        root.update()
        time.sleep(1)  # Check every second

root = tk.Tk()
root.title("Alarm Clock")

label = tk.Label(root, text="Enter the alarm time (HH:MM):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack(pady=10)

clock_label = tk.Label(root, text="", font=("Helvetica", 48))
clock_label.pack(pady=20)

result_label = tk.Label(root, text="")
result_label.pack()

def update_clock():
    current_time_str = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time_str)
    root.after(1000, update_clock)

update_clock()  # Update the clock every second

root.mainloop()
