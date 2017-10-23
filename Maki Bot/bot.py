import discord
from discord.ext import commands

TOKEN = 'MzYzODIzMzA2ODk1NTIzODQw.DNASgQ.vrh7hsjLzZFF_psYMmlm9xMXw4U'

description = '''Maki-chan bot for random commands by Echo#6945'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	bot.change_presence(game='Testing testing', status=None, afk=False)
	print('Status updated')
	print('------')
	
@bot.event
async def on_message(message):
	if message.content.startswith('$react'):
		msg = await bot.send_message(message.channel, 'React with thumbs up or thumbs down.')
		res = await bot.wait_for_reaaction(['👍', '👎'], message=msg)
		await bot.send_message(message.channel, '{0.user} reacted with {0.reaction.emoji}!'.format(res))
		
@bot.command()
async def ping():
	"""ping"""
	await bot.say("pong! :smile:")
	
@bot.command()
async def confused():
	"""Confused Maki"""
	await bot.say("https://i.imgur.com/OpOhKxi.jpg")
	
@bot.command()
async def what():
	"""What?! Maki"""
	await bot.say("https://i.imgur.com/iAdUYUe.png")
	
@bot.command()
async def smug():
	"""Smug Maki"""
	await bot.say("https://i.imgur.com/MRUjqwF.png")
	
@bot.command()
async def surprised():
	"""Surprised Maki"""
	await bot.say("https://i.imgur.com/InQ2Q1O.png")
	
@bot.command()
async def sad():
	"""Sad Hanamaru"""
	await bot.say("https://i.imgur.com/OTEFITG.png")
	
@bot.command()
async def teehee():
	"""Teehee Mari"""
	await bot.say("https://i.imgur.com/XOgFVQr.png")
	
@bot.command()
async def shrug():
	"""Shrugging Riko"""
	await bot.say("https://i.imgur.com/8QiBJKU.png")
	
@bot.command()
async def loli():
	"""Cute Ruby"""
	await bot.say("https://i.imgur.com/qQG8rfp.jpg")
	
@bot.command()
async def add(left : int, right : int):
	"""Adds 2 numbers"""
	await bot.say(left + right)
	
@bot.command()
async def subtract(left : int, right : int):
	"""Subtracts 2 numbers"""
	await bot.say(left - right)
	
@bot.command()
async def multiply(left : int, right : int):
	"""Multiplies 2 numbers"""
	await bot.say(left * right)
	
@bot.command()
async def divide(left : int, right : int):
	"""Divides 2 numbers"""
	await bot.say(left / right)
	
bot.run(TOKEN)