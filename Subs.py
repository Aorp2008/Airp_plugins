import requests
import random
import base64
from pyrogram import Client
from pagermaid.listener import listener
from pagermaid.utils import Message, client, edit_delete
sub_list = ['ssr', 'vmess', 'trojan']


@listener(command="Subs",
          description="随机从池子里拉取一个指定类型的节点(ssr/vmess/trojan)")
async def example(_: Client, message: Message):
    args = message.text.split()
    if len(args) > 1:
        arg = args[1]
        if arg in sub_list:
            if arg == 'ssr':
                url = 'https://proxypool.link/ssr/sub'
                response = requests.get(url)
                bash64_sub = response.text
                decoder = base64.b64decode(bash64_sub)
                sub = decoder.decode('utf-8')
                suiji = sub.strip()
                with open('Airp_sub.txt', mode='w', encoding='utf-8') as Airp_sub:
                    Airp_sub.write(suiji)
                with open('Airp_sub.txt', mode='r', encoding='utf-8') as open_Airp_sub:
                    nodes = open_Airp_sub.readlines()
                    random_node = random.choice(nodes).strip()
                await message.edit(random_node)
            elif arg == 'vmess':
                url = 'https://proxypool.link/vmess/sub'
                response = requests.get(url)
                bash64_sub = response.text
                decoder = base64.b64decode(bash64_sub)
                sub = decoder.decode('utf-8')
                suiji = sub.strip()
                with open('Airp_sub.txt', mode='w', encoding='utf-8') as Airp_sub:
                    Airp_sub.write(suiji)
                with open('Airp_sub.txt', mode='r', encoding='utf-8') as open_Airp_sub:
                    nodes = open_Airp_sub.readlines()
                    random_node = random.choice(nodes).strip()
                await message.edit(random_node)
            elif arg == 'trojan':
                url = 'https://proxypool.link/trojan/sub'
                response = requests.get(url)
                bash64_sub = response.text
                decoder = base64.b64decode(bash64_sub)
                sub = decoder.decode('utf-8')
                suiji = sub.strip()
                with open('Airp_sub.txt', mode='w', encoding='utf-8') as Airp_sub:
                    Airp_sub.write(suiji)
                with open('Airp_sub.txt', mode='r', encoding='utf-8') as open_Airp_sub:
                    nodes = open_Airp_sub.readlines()
                    random_node = random.choice(nodes).strip()
                await message.edit(random_node)
        else:
            await message.edit('错误的节点类型')
    else:
        await message.edit('请指定节点的类型')
