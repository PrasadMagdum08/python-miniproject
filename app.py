import tkinter as tk
from frame1 import *
from frame2 import *
from frame3 import *
from PIL import Image, ImageTk

class VideoToAudioApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Video to Audio Converter")
        self.geometry("720x600")

      
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

       
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.selected_video_path = None
        self.save_path = None
        self.video_thumbnail = None

 
        for F in (WelcomeFrame, ConvertFrame, ProgressFrame):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(WelcomeFrame)

    def show_frame(self, frame_class):
    
        frame = self.frames[frame_class]
        frame.tkraise()



if __name__ == "__main__":
    app = VideoToAudioApp()
    app.mainloop()
