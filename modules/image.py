import PIL.Image
import customtkinter as ctk
import requests

import PIL
import io

class ImageWindow(ctk.CTk):
    def __init__(self, url):
        super().__init__()

        r = requests.get(url).content
        img = PIL.Image.open(io.BytesIO(r))

        self.image = ctk.CTkImage(img, None, [640, 480])
        self.l = ctk.CTkLabel(self, text="", image=self.image)

        self.l.pack()

        self.geometry("640x480")

def show_image_window(url):
    w = ImageWindow(url=url)
    w.mainloop()

def imsave(url):
    try:
        r = requests.get(url).content
        img = PIL.Image.open(io.BytesIO(r))
        img.save("wallpaper.png", "png")

        return True
    except Exception as e:
        return False