import tkinter as tk
from tkinter import messagebox, ttk
import threading
from moviepy.editor import VideoFileClip

class ProgressFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="lightyellow")

       
        self.progress_label = tk.Label(self, text="Converting...", font=("Arial", 16), bg="lightyellow")
        self.progress_label.pack(pady=20)

        self.progress = ttk.Progressbar(self, mode="indeterminate", length=300)
        self.progress.pack(pady=20)

        self.status_label = tk.Label(self, text="", font=("Arial", 12), bg="lightyellow")
        self.status_label.pack()

    def tkraise(self):
 
        super().tkraise()
        self.start_conversion()

    def start_conversion(self):
     
        self.progress.start()
        thread = threading.Thread(target=self.convert_to_audio)
        thread.start()

    def convert_to_audio(self):
   
        video_path = self.controller.selected_video_path
        save_path = self.controller.save_path

        try:
            clip = VideoFileClip(video_path)
            clip.audio.write_audiofile(save_path)
            clip.close()
            self.progress.stop()
            self.progress_label.config(text="Conversion Complete!")
            self.status_label.config(text=f"Audio saved at: {save_path}")
        except Exception as e:
            self.progress.stop()
            messagebox.showerror("Error", f"Could not convert video to audio.\n{e}")