import discord
from discord.ext import commands, tasks
from itertools import cycle
client = commands.Bot(command_prefix='!')
status = cycle(['Made by: __', '!help'])
 
 
#events
@client.event
async def on_ready():
   change_status.start()
   print("Live!")
 
 
@tasks.loop(seconds=10)
async def change_status():
   await client.change_presence(activity=discord.Game(next(status)))
 
 
@client.event
async def on_command_error(ctx, error):
   if isinstance(error, commands.CommandNotFound):
       await ctx.send(
           'Invaid command used.\nUse command !help to find out all the commands.'
       )
 
 
# commands
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
   await ctx.channel.purge(limit=amount)
 
 
@clear.error
async def clear_error(ctx, error):
   if isinstance(error=commands.MissingRequiredArgument):
       await ctx.send('Please add an amount you want to delete.')
 
 
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
   await member.kick(reason=reason)
   await ctx.send(f'Kicked {member.mention}')
 
 
@kick.error
async def kick_error(ctx, error):
   if isinstance(error=commands.MissingRequiredArgument):
       await ctx.send(
           'Please give me a username you want to kick.\n Ex. !kick @user#0000'
       )
 
 
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
   await member.ban(reason=reason)
   await ctx.send(f'Banned {member.mention}')
 
 
@ban.error
async def ban_error(ctx, error):
   if isinstance(error=commands.MissingRequiredArgument):
       await ctx.send(
           'Please give me a username you want to ban.\n Ex. !ban @user#0000')
 
@client.command()
async def ask(ctx, *, question):
   responses = [
       'It is certain', 'It is decidedly so', 'Without a doubt',
       'Yes, definitely', 'You may rely on it', 'As I see it, yes',
       'Most likely', 'Outlook good', 'Yes', 'Signs point to yes',
       'Don’t count on it', 'My reply is no', 'My sources say no',
       'Outlook not so good', 'Very doubtful'
   ]
 
   await ctx.send(random.choice(responses))
 
@client.command()
async def quote(ctx):
   responses = [
       #'Quote of the day\n““ - ??',
       #'Quote of the day\n““ - ??',
       #'Quote of the day\n““ - ??',
       #'Quote of the day\n““ - ??',
       #'Quote of the day\n““ - ??',
       #'Quote of the day\n““ - ??',
       #'Quote of the day\n““ - ??',
       #'Quote of the day\n““ - ??',
       #'Quote of the day\n““ - ??',
       #'Quote of the day\n““ - ??',
       #'Quote of the day\n““ - ??',
       #'Quote of the day\n““ - ??',
       #'Quote of the day\n““ - ??',
       #'Quote of the day\n““ - ??'
   ]
   await ctx.send(random.choice(responses))
 
# Token
client.run('')
