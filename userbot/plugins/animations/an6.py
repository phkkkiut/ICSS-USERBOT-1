# animation code for PeLe - Userbot

import asyncio


@icssbot.on(admin_cmd(pattern="unoob$"))
@icssbot.on(sudo_cmd(pattern="unoob$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(9)
    event = await eor(event, "unnoob")
    animation_chars = [
        "EvErYbOdY",
        "iZ",
        "BiGGeSt",
        "NoOoB",
        "uNtiL",
        "YoU",
        "aRriVe",
        "😈",
        "EvErYbOdY iZ BiGGeSt NoOoB uNtiL YoU aRriVe 😈",
    ]
    for i in animation_ttl:
        await event.edit(animation_chars[i % 9])
        await asyncio.sleep(animation_interval)


@icssbot.on(admin_cmd(pattern="menoob$"))
@icssbot.on(sudo_cmd(pattern="menoob$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(9)
    event = await eor(event, "menoob")
    animation_chars = [
        "EvErYbOdY",
        "iZ",
        "BiGGeSt",
        "NoOoB",
        "uNtiL",
        "i",
        "aRriVe",
        "😈",
        "EvErYbOdY iZ BiGGeSt NoOoB uNtiL i aRriVe 😈",
    ]
    for i in animation_ttl:
        await event.edit(animation_chars[i % 9])
        await asyncio.sleep(animation_interval)


@icssbot.on(admin_cmd(pattern="upro$"))
@icssbot.on(sudo_cmd(pattern="upro$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(8)
    event = await eor(event, "upro")
    animation_chars = [
        "EvErYbOdY",
        "iZ",
        "PeRu",
        "uNtiL",
        "YoU",
        "aRriVe",
        "😈",
        "EvErYbOdY iZ PeRu uNtiL YoU aRriVe 😈",
    ]
    for i in animation_ttl:
        await event.edit(animation_chars[i % 8])
        await asyncio.sleep(animation_interval)


@icssbot.on(admin_cmd(pattern="mepro$"))
@icssbot.on(sudo_cmd(pattern="mepro$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(8)
    event = await eor(event, "mepro")
    animation_chars = [
        "EvErYbOdY",
        "iZ",
        "PeRu",
        "uNtiL",
        "i",
        "aRriVe",
        "😈",
        "EvErYbOdY iZ PeRu uNtiL i aRriVe 😈",
    ]
    for i in animation_ttl:
        await event.edit(animation_chars[i % 8])
        await asyncio.sleep(animation_interval)


@icssbot.on(admin_cmd(pattern=f"quickheal$", outgoing=True))
@icssbot.on(sudo_cmd(pattern=f"quickheal$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 5
    animation_ttl = range(11)
    event = await edit_or_reply(event, "quickheal")
    animation_chars = [
        "`Downloading File..`",
        "`File Downloaded....`",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\nResult: No Virus Found...`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@icssbot.on(admin_cmd(pattern=f"sqh$", outgoing=True))
@icssbot.on(sudo_cmd(pattern=f"sqh$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(11)
    event = await eor(event, "sqh")
    animation_chars = [
        "`Downloading File..`",
        "`File Downloaded....`",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\nResult: No Virus Found...`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@icssbot.on(admin_cmd(pattern=f"vquickheal$", outgoing=True))
@icssbot.on(sudo_cmd(pattern=f"vquickheal$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 5
    animation_ttl = range(11)
    event = await eor(event, "vquickheal")
    animation_chars = [
        "`Downloading File..`",
        "`File Downloaded....`",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\nResult:⚠️Virus Found⚠️\nMore Info: Torzan, Spyware, Adware`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@icssbot.on(admin_cmd(pattern=f"macos$", outgoing=True))
@icssbot.on(sudo_cmd(pattern=f"macos$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(11)
    event = await eor(event, "macos")
    animation_chars = [
        "`Connecting To Hackintosh...`",
        "`Initiating Hackintosh Login.`",
        "`Loading Hackintosh... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Hackintosh... 3%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Hackintosh... 9%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Hackintosh... 23%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Hackintosh... 39%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Hackintosh... 69%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Hackintosh... 89%\n█████████████████████▒▒▒▒ `",
        "`Loading Hackintosh... 100%\n█████████████████████████ `",
        "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Hackintosh`\n\n**My PC Specs:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@icssbot.on(admin_cmd(pattern=f"windows$", outgoing=True))
@icssbot.on(sudo_cmd(pattern=f"windows$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(11)
    event = await eor(event, "windows")
    animation_chars = [
        "`Connecting To Windows 10...`",
        "`Initiating Windows 10 Login.`",
        "`Loading Windows 10... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Windows 10... 3%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Windows 10... 9%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Windows 10... 23%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Windows 10... 39%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Windows 10... 69%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Windows 10... 89%\n█████████████████████▒▒▒▒ `",
        "`Loading Windows 10... 100%\n█████████████████████████ `",
        "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Windows 10`\n\n**My PC Specs:**\n\n **CPU:** __
