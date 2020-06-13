"""**Know Your UniBorg**
◇ list of all loaded plugins
◆ `.helpme`\n
◇ to know Data Center
◆ `.dc`\n
◇ powered by
◆ `.config`\n
◇ to know syntax
◆ `.syntax` <plugin name>
"""


import sys
from telethon import events, functions, __version__
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="ziking ?(.*)", allow_sudo=True))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    splugin_name = event.pattern_match.group(1)
    if splugin_name in borg._plugins:
        s_help_string = borg._plugins[splugin_name].__doc__
    else:
        s_help_string = ""
    help_string = """🔼ᴢɪ ᴋɪɴɢ ᴜsᴇʀʙᴏᴛ🔽ɪs ᴜᴘ ᴀɴᴅ ʀᴜɴɴɪɴɢ. 
° ᴘʀᴏᴛᴏɴ : 1.14.0
° ɴᴇᴜᴛʀᴏɴ: 3.8.2 (ʟᴀsᴛ ᴛᴇsᴛᴇᴅ ᴀᴛ ᴊᴜɴᴇ 10, 2020 ɪɴ ᴢɪ ᴋɪɴɢ's ʟᴀʙ.)
° os: ʟɪɴᴜx/ɢɴᴜ  
° ᴄᴜʀʀᴇɴᴛ ᴅᴄ : 4 
° ᴜsᴇʀ : @ZiKing
° ᴏᴡɴᴇʀ : @ZiKing 
° ʜᴇʀᴏᴋᴜ: ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴡɪᴛʜ ʜᴋ16
° ɢɪᴛʜᴜʙ ʀᴇᴘᴏ: ᴘʀɪᴠᴀᴛᴇ
° sᴜᴅᴏ ᴜsᴇʀs: ᴀʟʟᴏᴡᴇᴅ 
° ᴜsᴇʀʙᴏᴛ ʟɪᴠᴇ ɪɴ:  ᴜsᴀ """.format(
        sys.version,
        __version__
    )
    tgbotusername = Config.TG_BOT_USER_NAME_BF_HER  # pylint:disable=E0602
    if tgbotusername is not None:
        results = await borg.inline_query(  # pylint:disable=E0602
            tgbotusername,
            help_string + "\n\n" + s_help_string
        )
        await results[0].click(
            event.chat_id,
            reply_to=event.reply_to_msg_id,
            hide_via=True
        )
        await event.delete()
    else:
        await event.reply(help_string + "\n\n" + s_help_string)
        await event.delete()


@borg.on(admin_cmd(pattern="dc"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetNearestDcRequest())  # pylint:disable=E0602
    await event.edit(result.stringify())


@borg.on(admin_cmd(pattern="alive"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602
    result = result.stringify()
    logger.info(result)  # pylint:disable=E0602
    await event.edit("""Telethon UserBot powered by @UniBorg""")


@borg.on(admin_cmd(pattern="syntax (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    plugin_name = event.pattern_match.group(1)
    if plugin_name in borg._plugins:
        help_string = borg._plugins[plugin_name].__doc__
        unload_string = f"Use `.unload {plugin_name}` to remove this plugin.\n           [©UniBorg](https://telegra.ph/file/1bef11711dd89cee0de6f.jpg)"
        if help_string:
            plugin_syntax = f"Syntax for plugin **{plugin_name}**:\n\n{help_string}\n{unload_string}"
        else:
            plugin_syntax = f"No DOCSTRING has been setup for {plugin_name} plugin."
    else:
        plugin_syntax = "Enter valid **Plugin** name.\nDo `.exec ls stdplugins` or `.helpme` to get list of valid plugin names."
    await event.edit(plugin_syntax)
