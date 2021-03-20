import discord
import asyncio
import random


token = "ODA0OTk4MjA0MzEwODE0NzMx.YBUfAA.jOddKEoXW84JSXgf5-Z46jhmVws"



client = discord.Client()


@client.event
async def on_ready():
    print(client.user.name)
    print("성공적으로 봇이 시작되었습니다.")
    game = discord.Game("수원봇")
    await client.change_presence(status=discord.Status.online,activity=game)

@client.event
async def on_message(message):
	if message.content.startswith('vs c가위바위보'):
		rsp = ["가위","바위","보"]
		embed = discord.Embed(title="가위바위보",description="가위바위보를 합니다 5초내로 (가위/바위/보)를 써주세요!", color=0x00aaaa)
		channel = message.channel
		msg1 = await message.channel.send(embed=embed)
		def check(m):
			return m.author == message.author and m.channel == channel
		try:
			msg2 = await client.wait_for('message', timeout=5.0, check=check)
		except asyncio.TimeoutError:
			await msg1.delete()
			embed = discord.Embed(title="가위바위보",description="시간초과", color=0x00aaaa)
			await message.channel.send(embed=embed)
			return
		else:
			await msg1.delete()
			bot_rsp = str(random.choice(rsp))
			user_rsp  = str(msg2.content)
			answer = ""
			if bot_rsp == user_rsp:
				answer = "저는 " + bot_rsp + "을 냈고, 당신은 " + user_rsp + "을 내셨내요.\n" + "아쉽지만 비겼습니다."
			elif (bot_rsp == "가위" and user_rsp == "바위") or (bot_rsp == "보" and user_rsp == "가위") or (bot_rsp == "바위" and user_rsp == "보"):
				answer = "저는 " + bot_rsp + "을 냈고, 당신은 " + user_rsp + "을 내셨내요.\n" + "아쉽지만 제가 졌습니다."
			elif (bot_rsp == "바위" and user_rsp == "가위") or (bot_rsp == "가위" and user_rsp == "보") or (bot_rsp == "보" and user_rsp == "바위"):
				answer = "저는 " + bot_rsp + "을 냈고, 당신은 " + user_rsp + "을 내셨내요.\n" + "제가 이겼습니다!"
			else:
				embed = discord.Embed(title="가위바위보",description="앗, 가위, 바위, 보 중에서만 내셔야죠...", color=0x00aaaa)
				await message.channel.send(embed=embed)
				return
			embed = discord.Embed(title="가위바위보",description=answer, color=0x00aaaa)
			await message.channel.send(embed=embed)
			return



		



client.run("ODA0OTk4MjA0MzEwODE0NzMx.YBUfAA.jOddKEoXW84JSXgf5-Z46jhmVws")
