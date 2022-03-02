# Ping for assistant bot 
# by: @ph_7v

import time
from telethon import events
from datetime import datetime
from . import *

@asst_cmd("بنك")
async def _(e):
    Start = datetime.now()
    End = datetime.now()
    Ms = (End - Start).microseconds / 1000
    UpTime = get_readable_time((time.time() - StartTime))
    await e.reply(Ping.format(Ms, UpTime))
