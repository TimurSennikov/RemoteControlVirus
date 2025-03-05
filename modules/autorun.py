from win32com.client import Dispatch
import os

AUTORUN_NAME = "funnyvirus.lnk"

scut_p = os.path.join(os.getenv("APPDATA"), os.path.join("Microsoft", "Windows", "Start Menu", "Programs", "Startup"))

def is_in_autorun():
    return AUTORUN_NAME in os.listdir(scut_p)

def autorun_add():
    if not AUTORUN_NAME in os.listdir(scut_p):
        shell = Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(os.path.join(scut_p, AUTORUN_NAME))
        shortcut.TargetPath = os.path.abspath(os.path.join(".", os.path.basename(__file__)))
        shortcut.WorkingDirectory = os.path.abspath(".")
        shortcut.save()