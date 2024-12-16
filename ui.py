import customtkinter as ctk
from tkinter import filedialog

class UI:
    def __init__(self):
        self.master = ctk.CTk()
        self.master.title("TimelapseXtractor")
        self.master.geometry("500x400")

        # Variables
        self.video_path = None

        # Upload button
        self.upload_button = ctk.CTkButton(self.master, text="Upload Video", command=self.upload_video)
        self.upload_button.pack(pady=20)

        # Label to show the selected video
        self.video_label = ctk.CTkLabel(self.master, text="No video selected", wraplength=400)
        self.video_label.pack(pady=10)

        # Entry for interval
        self.interval_label = ctk.CTkLabel(self.master, text="Enter interval (seconds):")
        self.interval_label.pack(pady=5)

        self.interval_entry = ctk.CTkEntry(self.master, placeholder_text="e.g., 5")
        self.interval_entry.pack(pady=10)

        # Start button
        self.start_button = ctk.CTkButton(self.master, text="Start")
        self.start_button.pack(pady=20)

        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(self.master)
        self.progress_bar.pack(pady=10, fill="x", padx=20)
        self.progress_bar.set(0)  # Initialize progress bar at 0
        self.progress_bar_label = ctk.CTkLabel(self.master, text="0%")
        self.progress_bar_label.pack(fill="x")

    def upload_video(self):
        self.video_path = filedialog.askopenfilename(
            title="Select a Video File",
            filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv"), ("All Files", "*.*")]
        )
        if self.video_path:
            self.video_label.configure(text=f"Selected: {self.video_path.split('/')[-1]}")
        else:
            self.video_label.configure(text="No video selected")


