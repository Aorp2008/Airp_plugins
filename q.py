from pyrogram import Client
from pagermaid.listener import listener
from pagermaid.utils import Message, client, edit_delete
import os


@listener(command="q", description="快捷指令")
async def airp(bot: Client, message: Message):
    if not os.path.exists('q_config.txt'):
        with open('q_config.txt', mode='w', encoding='utf-8') as init_file:
            init_file.write('')
    chat_id = message.chat.id
    command_args = message.text.split()
    if len(command_args) == 2:
        with open('q_config.txt', mode='r', encoding='utf-8') as open_file:
            for User in open_file:
                nmb, q = User.strip().split("----")
                if nmb == command_args[1]:
                    a = ',' + q
                    await bot.send_message(chat_id, a)
                    break
            else:
                await message.edit('未找到相应的指令')
    else:
        await message.edit('格式错误')
