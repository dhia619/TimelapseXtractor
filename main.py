import cv2
from ui import *
from tkinter import messagebox
from threading import Thread

class Application:
    def __init__(self):
        self.ui = UI()
        self.ui.start_button.configure(command=self.start_processing)
        self.ui.master.mainloop()

    def start_processing(self):
        try:
            interval = int(self.ui.interval_entry.get())
            if interval <= 0:
                raise ValueError("Interval must be greater than 0")
            if not self.ui.video_path:
                messagebox.showerror("Error", "No video file selected!")
                return

            # Start processing in a separate thread
            thread = Thread(target=self.process_video, args=(interval,))
            thread.daemon = True  # Ensures the thread will close when the main app exits
            thread.start()

        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def process_video(self, interval: int):

        video = cv2.VideoCapture(self.ui.video_path)
        fps = int(video.get(cv2.CAP_PROP_FPS))
        frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

        # Define VideoWriter
        output_video_path = f"{self.ui.video_path}_timelapse.avi"
        fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for AVI files
        out = cv2.VideoWriter(output_video_path, fourcc, fps // interval, (frame_width, frame_height))

        frame_number = 0
        while True:
            success, frame = video.read()
            if not success:
                break

            # Write frame at the defined interval
            if frame_number % (fps * interval) == 0:
                out.write(frame)

            # Update progress bar
            progress = frame_number / total_frames
            self.ui.progress_bar_label.configure(text = f"{round(progress*100)}%")
            self.ui.progress_bar.set(progress)
            self.ui.master.update_idletasks()
            frame_number += 1

        video.release()
        out.release()
        messagebox.showinfo("Success", f"Snapshots taken every {interval} seconds. Video saved as {output_video_path}")
        self.ui.progress_bar.set(0)
        self.ui.progress_bar_label.configure(text="0%")

# Run the app
if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    app = Application()