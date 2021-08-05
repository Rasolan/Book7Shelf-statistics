import discord
from mcstatus import MinecraftServer
from mctools import RCONClient



rcon = RCONClient('book7shelf.ru')
port= 25575
success = rcon.login('F97E0011CA552CF9AA')
print('RCONClient - Работает')

#Эта ветка отвичает за статус и за статистику сервера

num = 1
while num < 10:
    server = MinecraftServer.lookup("book7shelf.ru")
num = 1
while num < 10:    
    status=server.status()
print('server status - Работает')
#Тут начало дискорд бота
client = discord.Client()
@client.event 
async def on_ready():
    print('Discord BOT - Работает')
#Просто статус бота  
    status=server.status()
    game = discord.Game("{0} из 20 Игроков на сервере".format(status.players.online, status.latency))
    await client.change_presence(status=discord.Status.idle, activity=game)

#Проверка статуса бота работает/не работает
@client.event
async def on_message(message):
    if message.content.startswith('!status'):
        try:
            status=server.status()
            embedVar = discord.Embed(title="Сервер онлайн ✅".format(status.players.online, status.latency), color=0x19a617)
            await message.channel.send(embed=embedVar)

        except:
            embedVar = discord.Embed(title="Сервер оффлайн ".format(status.players.online, status.latency), color=0xd21919)


#Показывает онлайн бата 
@client.event
async def on_message(message):
    if message.content.startswith('!online'):
        try:
            player = server.status()
            embedVar = discord.Embed(title="Онлайн сервера 📌".format(status.players.online, status.latency), description=("Сейчас играют {0} игроков из 20".format(status.players.online, status.latency)), color=0x191ce1)
            await message.channel.send(embed=embedVar)
        except:
            embedVar = discord.Embed(title="Сервер оффлайн".format(status.players.online, status.latency), color=0xd21919)
            await message.channel.send(embed=embedVar)


client.run('ODIzNjc3NzA5NDU1NTg5NDY4.YFkTpQ.0LUMykmFEatj7PQao12-KSzJbO0м')


