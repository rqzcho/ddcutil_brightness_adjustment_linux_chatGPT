# Import tkinter suite needed for the GUI generation
from tkinter import messagebox
from tkinter import Label, BooleanVar, Checkbutton, LabelFrame
from tkinter import Scale
from tkinter import Tk
import subprocess
import os
# Import the time module for adding delays.
import time

# Function to apply the brightness settings to the selected monitors.
def apply():
    from main import brightness_scale
    brightness_var = brightness_scale.get()
    monitor_list = get_available_monitors()
    monitor_vars = []
    monitor_frame = LabelFrame(root, text="Monitors")
    monitor_frame.pack(fill="both", expand="yes", padx=10, pady=10)
    monitor_counter = 0  # counter for monitor_vars index
    for monitor in monitor_list:
        var = BooleanVar()
        var.set(True)
        monitor_vars.append(var)
        label = Label(monitor_frame, text=monitor, anchor="w")
        label.grid(row=monitor_counter, column=0, sticky="w")
        checkbox = Checkbutton(monitor_frame, variable=monitor_vars[monitor_counter])
        checkbox.grid(row=monitor_counter, column=1)
        monitor_counter += 1
    for i, monitor in enumerate(monitor_list):
        if monitor_vars[i].get():
            parts = monitor.split()
            display_number = parts[1]
            cmd = f"ddcutil setvcp 10 {brightness_var} -d {display_number}"
            for _ in range(5):
                subprocess.run(cmd, shell=True)
    messagebox.showinfo("Success", "Brightness adjusted successfully.")

# Function to return a dictionary of available monitors.
def get_available_monitors() -> dict:
    time.sleep(5) # Add a 10 second delay
    monitor_dict = {}
    try:
        output = subprocess.check_output("ddcutil detect", shell=True)
        lines = output.decode("utf-8").split("\n")
        for line in lines:
            if "Display" in line:
                parts = line.split()
                display = int(parts[1])
                for subline in lines:
                    if "Model:" in subline:
                        model = subline.split("Model: ")[1]
                        monitor_dict[f"Monitor {display} - {model}"] = display
                        break
    except:
        pass
    if not monitor_dict:
        monitor_dict["No Monitors Detected"] = None
    return monitor_dict

# Function to adjust brightness of a single monitor.
def adjust_brightness(monitor, value):
    try:
        os.system(f"ddcutil setvcp 10 {value} -d {monitor}")
        return True
    except:
        return False

# Function to adjust brightness for all monitors in the monitor_dict.
def adjust_brightness_all(monitor_dict, value, problem_checkbox):
    problem = False
    for monitor in monitor_dict:
        if not adjust_brightness(monitor_dict[monitor], value):
            problem = True
    if problem and problem_checkbox:
        for i in range(5):
            if messagebox.askyesno("Adjustment problem", "There was a problem adjusting one or more monitors. Would you like to try again?"):
                adjust_brightness_all(monitor_dict, value, False)
    return not problem

# Function to adjust brightness for a single monitor using ddcutil command.
def adjust_brightness_single(brightness, display):
    try:
        cmd = f"ddcutil setvcp 10 {brightness} -d {display}"
        subprocess.check_output(cmd, shell=True)
    except:
        messagebox.showerror("Error", "Could not adjust brightness.")
