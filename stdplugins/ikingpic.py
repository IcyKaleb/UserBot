"""
Time In Profile Pic.....
Command: `.autopic`

:::::Credit Time::::::
1) Coded By: @s_n_a_p_s
2) Ported By: @r4v4n4 (Legend)
3) End Game Help By: @spechide


#curse: who ever edits this credit section will goto hell

⚠️DISCLAIMER⚠️

USING THIS PLUGIN CAN RESULT IN ACCOUNT BAN. WE DONT CARE ABOUT BAN, SO WE ARR USING THIS.
"""
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from uniborg.util import admin_cmd
import asyncio
import shutil 

FONT_FILE_TO_USE = "Fonts/DS-DIGII.ttf"

@borg.on(admin_cmd(pattern="autopoc ?(.*)", allow_sudo=True))
async def autopic(event):
    hmm = await event.reply("Initiating Autopic... ")
    downloaded_file_name = "./ravana/original_pic.png"
    downloader = SmartDL(Config.ZIKING_PIC, downloaded_file_name, progress_bar=True)
    downloader.start(blocking=False)
    photo = "photo_pfp.png"
    while not downloader.isFinished():
        place_holder = None
    counter = -30
    await hmm.edit("Autopic Activated Successfully")
    while True:
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        #file_test = im.rotate(counter, expand=False).save(photo, "PNG")
        current_time = datetime.now().strftime("\n%H:%M")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 200)
        cfnt = ImageFont.truetype(FONT_FILE_TO_USE, 20)
        drawn_text.text((20, 250), current_time, font=fnt, fill=(106, 169, 226))
        drawn_text.text((20,20), "℅H:%M\nFight your demon, not me.", font=cfnt, fill=(220,220,220))
        drawn_text.text((20,20), "Hi", font=cfnt, fill=(220,220,220))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            counter -= 30
            await asyncio.sleep(60)
        except:
            return
