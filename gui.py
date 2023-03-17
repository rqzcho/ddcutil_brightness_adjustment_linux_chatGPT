import tkinter as tk

def create_gui(root, get_available_monitors, adjust_brightness_single, adjust_brightness_all):
    # initialize GUI
    root.title("Brightness Control")
    root.geometry("400x300")
    
    # initialize monitor checkboxes
    monitor_list = get_available_monitors()
    monitor_vars = []
    for monitor in monitor_list:
        var = tk.BooleanVar()
        var.set(True)
        monitor_vars.append(var)
    monitor_frame = tk.LabelFrame(root, text="Monitors")
    monitor_frame.pack(fill="both", expand="yes", padx=10, pady=10)
    for i, monitor in enumerate(monitor_list):
        label = tk.Label(monitor_frame, text=monitor, anchor="w")
        label.grid(row=i, column=0, sticky="w")
        checkbox = tk.Checkbutton(monitor_frame, variable=monitor_vars[i])
        checkbox.grid(row=i, column=1)

    # initialize brightness slider
    brightness_slider = tk.Scale(
        root, from_=0, to=100, orient="horizontal", label="Brightness", length=300
    )
    brightness_slider.pack(pady=10)

    # initialize apply button
    apply_button = tk.Button(
        root, text="Apply", command=lambda: adjust_brightness_all(monitor_vars, brightness_slider.get())
    )
    apply_button.pack(pady=10)

