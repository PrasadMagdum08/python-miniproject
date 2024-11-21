import tkinter as tk
from tkinter import filedialog
from frame2 import *


class WelcomeFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='white')



        label = tk.Label(self, text="Welcome to Video-Audio Converter", font=("Arial", 28, 'bold'))
        label.pack(side='top', pady=150)

        select_button = tk.Button(self, text="Select Video File", font=("Arial", 20, 'bold'), bg='red', fg='white',border=0, command=self.select_video)
        select_button.pack()

    def select_video(self):

        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov;*.mkv")])
        if file_path:
            self.controller.selected_video_path = file_path
            self.controller.show_frame(ConvertFrame)