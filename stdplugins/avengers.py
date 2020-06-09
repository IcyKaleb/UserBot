#Made By @Nihinivi Keep Credits If You Are Goanna Kang This Lol
#And Thanks To The Creator Of Autopic This Script Was Made from Snippets From That Script
#Usage .gamerpfp  Im Not Responsible For Any Ban caused By This
import requests , re , random 
import urllib , os 
from telethon.tl import functions
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from uniborg.util import admin_cmd
import asyncio
from time import sleep


COLLECTION_STRING = [

  "avengers-logo-wallpaper",

  "avengers-hd-wallpapers-1080p",

  "avengers-iphone-wallpaper",

  "iron-man-wallpaper-1920x1080",

  "iron-man-wallpapers"

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

@borg.on(admin_cmd(pattern="avengersdp ?(.*)", allow_sudo=True))

async def main(event):

    await event.reply("Auto Pic has been started sucessfully")

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(30) #Edit this to your required needs

