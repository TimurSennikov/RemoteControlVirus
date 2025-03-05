import asyncio

from modules import *
from botapi import *

socketapi = SockThread()
socketapi.start()

autorun_add()
asyncio.run(run_bot_service())