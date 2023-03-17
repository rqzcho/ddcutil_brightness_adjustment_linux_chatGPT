import tkinter as tk
from gui import create_gui
from monitor import adjust_brightness_all, adjust_brightness_single, get_available_monitors

if __name__ == "__main__":
    root = tk.Tk()
    create_gui(root, get_available_monitors, adjust_brightness_single, adjust_brightness_all)

root.mainloop()