#Made By @Nihinivi Keep Credits If You Are Goanna Kang This Lol
#And Thanks To The Creator Of Autopic This Script Was Made from Snippets From That Script
#Usage .gamerpfp  Im Not Responsible For Any Ban caused By This
import requests , re , random 
import urllib , os 
from telethon.tl import functions
from datetime import datetime
from uniborg.util import admin_cmd
import asyncio
from time import sleep

COLLECTION_STRING = [
  "hacker-background"
]

async def animepp():
    os.system("rm -rf donot.jpg")
    rnd = random.randint(0, len(COLLECTION_STRING) - 1)
    pack = COLLECTION_STRING[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile('/\w+/full.+.jpg')
    f = f.findall(pc)
    fy = "http://getwallpapers.com"+random.choice(f)
    print(fy)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")
    urllib.request.urlretrieve(fy,"donottouch.jpg")
@borg.on(admin_cmd(pattern="hacker ?(.*)", allow_sudo=True))
async def main(event):
    await event.reply("ᴀᴜᴛᴏ ᴘɪᴄ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.\n\nᴘɪᴄs ᴛʏᴘᴇ :- ʜᴀᴄᴋᴇʀ 😎\n\nᴏᴡɴᴇʀ : @KarvorTM") #Owner @NihiNivi
    while True:
        await animepp()
        file = await event.client.upload_file("donottouch.jpg")  
        await event.client(functions.photos.DeletePhotosRequest(await event.client.get_profile_photos("me", limit=1)))
        await event.client(functions.photos.UploadProfilePhotoRequest( file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(60) #Edit this to your required needs
