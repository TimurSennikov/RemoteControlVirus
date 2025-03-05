import ctypes

from .tools import *

def set_wallpaper(img):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img, 3)