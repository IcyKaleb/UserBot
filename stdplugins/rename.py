"""Rename Telegram Files
Syntax:
.rnupload file.name
.rnstreamupload file.name
By @Ck_ATR"""

import asyncio
import time
from datetime import datetime
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
import math
import os
from pySmartDL import SmartDL
from telethon.tl.types import DocumentAttributeVideo
from uniborg.util import progress, humanbytes, time_formatter, admin_cmd


thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"


@borg.on(admin_cmd(pattern="rename (.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    url = input_str
    file_name = os.path.basename(url)
    to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
    if "|" in input_str:
        url, file_name = input_str.split("|")
    url = url.strip()
    file_name = file_name.strip()
    downloaded_file_name = os.path.join(to_download_directory, file_name)
    downloader = SmartDL(url, downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    display_message = ""
    c_time = time.time()
    while not downloader.isFinished():
        total_length = downloader.filesize if downloader.filesize else None
        downloaded = downloader.get_dl_size()
        now = time.time()
        diff = now - c_time
        percentage = downloader.get_progress() * 100
        speed = downloader.get_speed()
        elapsed_time = round(diff
