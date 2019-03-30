"""Create Private Groups
Available Commands:
.create (b|g) GroupName"""
from telethon import functions
from uniborg import util


@borg.on(util.admin_cmd(r"\.create (b|g) (.*)"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    type_of_group = event.pattern_match.group(1)
    group_name = event.pattern_match.group(2)
    if type_of_group == "b":
        try:
            await borg(functions.messages.CreateChatRequest(  # pylint:disable=E0602
                users=["@GoogleIMGBot"],
                # Not enough users (to create a chat, for example)
                # Telegram, no longer allows creating a chat with ourselves
                title=group_name
            ))
            await event.edit("Group `{}` created successfully!".format(group_name))
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
    elif type_of_group == "g":
        try:
            await borg(functions.channels.CreateChannelRequest(  # pylint:disable=E0602
                title=group_name,
                about="This is a Test from @UniBorg",
                megagroup=True
            ))
            await event.edit("Group `{}` created successfully!".format(group_name))
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
    else:
        await event.edit("Read .helpme to know how to use me")
