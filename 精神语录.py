from pyrogram import Client
from pagermaid.listener import listener
from pagermaid.utils import Message, client, edit_delete


@listener(command="jise", description="内容十分精神的语录")
async def jise(_: Client, message: Message):
    req = await client.get("https://api.oddfar.com/yl/q.php?c=1009&encode=text")
    if req.status_code == 200:
        await message.edit(req.text)
    else:
        await edit_delete(message, "Api数据获取失败")
