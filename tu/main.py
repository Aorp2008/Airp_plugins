from pyrogram import Client
from pagermaid.listener import listener
from pagermaid.utils import Message, client, edit_delete


@listener(command="tu_like", description="非常土的情话")
async def tu_like(_: Client, message: Message):
    req = await client.get("https://api.oddfar.com/yl/q.php?c=1001&encode=text")
    if req.status_code == 200:
        await message.edit(req.text)
    else:
        await edit_delete(message, "Api数据获取失败")