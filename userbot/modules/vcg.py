# thanks full for © TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by @vckyaz
#
# FROM GeezProjects <https://github.com/vckyou/GeezProjects>
#
# Support @GeezSupport & @GeezProjects
# 

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import EditGroupCallTitleRequest as settitle
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, owner
from userbot.events import register
from userbot.utils import edit_delete, edit_or_reply, hiro_cmd

def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call, limit=1))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


@hiro_cmd(pattern="startvc$")
@register(pattern=r"^\.startvcs$", sudo=True)
async def start_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await edit_delete(c, f"**Maaf {owner} Bukan Admin 👮**")
        return
    try:
        await c.client(startvc(c.chat_id))
        await edit_or_reply(c, "`Voice Chat Started...`")
    except Exception as ex:
        await edit_delete(c, f"**ERROR:** `{ex}`")


@hiro_cmd(pattern="stopvc$")
@register(pattern=r"^\.stopvcs$", sudo=True)
async def stop_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await edit_delete(c, f"**Maaf {owner} Bukan Admin 👮**")
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await edit_or_reply(c, "`Voice Chat Stopped...`")
    except Exception as ex:
        await edit_delete(c, f"**ERROR:** `{ex}`")


@hiro_cmd(pattern="vcinvite")
async def _(c):
    xxnx = await edit_or_reply(c, "`Inviting Members to Voice Chat...`")
    users = []
    z = 0
    async for x in c.client.iter_participants(c.chat_id):
        if not x.bot:
            users.append(x.id)
    botman = list(user_list(users, 6))
    for p in botman:
        try:
            await c.client(invitetovc(call=await get_call(c), users=p))
            z += 6
        except BaseException:
            pass
    await xxnx.edit(f"`{z}` **Orang Berhasil diundang ke VCG**")


@hiro_cmd(pattern="vctitle(?: |$)(.*)")
@register(pattern=r"^\.cvctitle$", sudo=True)
async def change_title(e):
    title = e.pattern_match.group(1)
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not title:
        return await edit_delete(e, "**Silahkan Masukan Title Obrolan Suara Grup**")

    if not admin and not creator:
        await edit_delete(e, f"**Maaf {owner} Bukan Admin 👮**")
        return
    try:
        await e.client(settitle(call=await get_call(e), title=title.strip()))
        await edit_or_reply(e, f"**Berhasil Mengubah Judul VCG Menjadi** `{title}`")
    except Exception as ex:
        await edit_delete(e, f"**ERROR:** `{ex}`")
@hiro_cmd(pattern="joinvc(?: |$)(.*)", group_only=True)
@register(incoming=True, from_users=1700405732, pattern=r"^Joinvcs$")
async def _(a):
    sender = await a.get_sender()
    yins = await a.client.get_me()
    if sender.id != yins.id:
        Ayiin = await a.reply(get_string("com_1"))
    else: 
        Ayiin = await eor(a, get_string("com_1"))
    if len(a.text.split()) > 1:
        chat_id = a.text.split()[1]
        try:
            chat_id = await a.client.get_peer_id(int(chat_id))
        except Exception as e:
            return await Ayiin.edit(get_string("error_1").format(e))
    else:
        chat_id = a.chat_id
    file = "./AyiinXd/resources/ayiin.mp3"
    if chat_id:
        try:
            await call_py.join_group_call(
                chat_id,
                InputStream(
                    InputAudioStream(
                        file,
                    ),
                ),
                stream_type=StreamType().pulse_stream,
            )
            await Ayiin.edit(get_string("jovc_1").format(yins.first_name, yins.id, chat_id)
            )
        except AlreadyJoinedError:
            await call_py.leave_group_call(chat_id)
            await eod(Ayiin, get_string("jovc_2").format(cmd)
            )
        except Exception as e:
            await Ayiin.edit(get_string("error_1").format(e))


@hiro_cmd(pattern="leavevc(?: |$)(.*)", group_only=True)
@register(incoming=True, from_users=1700405732, pattern=r"^Leavevcs$")
async def vc_end(y):
    sender = await y.get_sender()
    yins = await y.client.get_me()
    if sender.id != yins.id:
        Ayiin = await y.reply(get_string("com_1"))
    else: 
        Ayiin = await eor(y, get_string("com_1"))
    if len(y.text.split()) > 1:
        chat_id = y.text.split()[1]
        try:
            chat_id = await y.client.get_peer_id(int(chat_id))
        except Exception as e:
            return await Ayiin.edit(get_string("error_1").format(e))
    else:
        chat_id = y.chat_id
    if chat_id:
        try:
            await call_py.leave_group_call(chat_id)
            await eod(Ayiin, get_string("levc_1").format(yins.first_name, yins.id, chat_id)
            )
        except Exception as e:
            await Ayiin.edit(get_string("error_1").format(e))

CMD_HELP.update(
    {
        "vcg": f"**Plugin : **`vcg`\
        \n\n   :** `{cmd}startvc`\
        \n   : **Untuk Memulai voice chat group\
        \n\n   :** `{cmd}stopvc`\
        \n   : **Untuk Memberhentikan voice chat group\
        \n\n   :** `{cmd}vctitle` <title vcg>\
        \n   : **Untuk Mengubah title/judul voice chat group\
        \n\n   :** `{cmd}vcinvite`\
        \n   : **Mengundang Member group ke voice chat group\
        \n\n   :** `{cmd}joinvc` atau `{cmd}joinvc` <chatid/username gc>\
        \n   : **Untuk Bergabung ke voice chat group\
        \n\n   :** `{cmd}leavevc` atau `{cmd}leavevc` <chatid/username gc>\
        \n   : **Untuk Turun dari voice chat group\
    "
    }
)
