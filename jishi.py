import tkinter as tk
from tkinter import messagebox
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")

        self.time_left = 0
        self.is_running = False

        self.label = tk.Label(root, text="Enter time (in seconds):")
        self.label.pack()

        self.time_entry = tk.Entry(root)
        self.time_entry.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_timer, state=tk.DISABLED)
        self.pause_button.pack()

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer, state=tk.DISABLED)
        self.reset_button.pack()

        self.time_label = tk.Label(root, text="00:00")
        self.time_label.pack()

    def start_timer(self):
        if not self.is_running:
            try:
                self.time_left = int(self.time_entry.get())
                if self.time_left <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a positive integer.")
                return

            self.is_running = True
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.NORMAL)
            self.countdown()

    def countdown(self):
        if self.time_left <= 0:
            self.is_running = False
            self.start_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.DISABLED)
            messagebox.showinfo("Time's Up!", "Time is up!")
        else:
            mins, secs = divmod(self.time_left, 60)
           
