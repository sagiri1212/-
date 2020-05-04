import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("병신짓")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!안녕 사기리"):
        await message.channel.send("어디서 하찮은인간주제에 나에게말을건네냐")

    if message.content.startswith("!명령어"):
        await message.channel.send("명령어,안녕 사기리.사기리야 섹스,사기리야 미육봇,사기리야 종로로갈까")

    if message.content.startswith("!사기리야 섹스"):
        await message.channel.send("시발 섹스하고싶으니깐 하지마라")


@client.event
async def on_message(message):
    if message.content.startswith("!사기리야 미육봇"):
        await message.channel.send("그새기 꼭잡는다")

    if message.content.startswith("!사기리야 종로로갈까"):
        await message.channel.send("명동으로가")

























































































client.run("NzA2NzM0NzkxMzE5NjE3NTg3.Xq-kKw.m6ZFElvehi-d747Yax9CLPETcZE")
