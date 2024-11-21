import tkinter as tk
from tkinter import filedialog,  messagebox
from moviepy.editor import VideoFileClip
from PIL import Image, ImageTk
from frame3 import *
from frame1 import *

class ConvertFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="white")

        self.back_button = tk.Button(self, text="Back", font=("Arial", 12, 'bold'),bg='grey', fg='white', command=self.go_back)
        self.back_button.place(x=5, y=5)

        # Top label
        self.label = tk.Label(self, text="Want to Convert this Video to Audio?", font=("Arial", 25, 'bold'), bg="lightgreen")
        self.label.pack(side='top', pady=50)

        # Video preview area
        self.thumbnail_label = tk.Label(self, bg="lightgreen")
        self.thumbnail_label.pack(pady=40)

        # Convert button
        self.convert_button = tk.Button(self, text="Convert to Audio", font=("Arial", 18, 'bold'), bg='red', fg='white', command=self.select_save_location)
        self.convert_button.pack()

    def tkraise(self):
        
        super().tkraise()
        self.show_video_thumbnail()

    def show_video_thumbnail(self):
   
        video_path = self.controller.selected_video_path
        if video_path:
            try:
                clip = VideoFileClip(video_path)
                frame = clip.get_frame(1)  # Extract a frame at 1 second
                image = Image.fromarray(frame)
                image.thumbnail((300, 200))  # Resize the frame
                self.controller.video_thumbnail = ImageTk.PhotoImage(image)
                self.thumbnail_label.config(image=self.controller.video_thumbnail)
                clip.close()
            except Exception as e:
                messagebox.showerror("Error", f"Could not load video thumbnail.\n{e}")

    def select_save_location(self):
       
        save_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                 filetypes=[("MP3 Files", "*.mp3"), ("All Files", "*.*")])
        if save_path:
            self.controller.save_path = save_path
            self.controller.show_frame(ProgressFrame)

    def go_back(self):

        self.controller.show_frame(WelcomeFrame)