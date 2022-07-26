import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix="w?")
client.remove_command("help")

@client.event 
async def on_ready():
  print("Cock n Balls")

@client.event
async def on_command_error(ctx, error):
  if (error, commands.MissingRequiredArgument):
    await ctx.send(f"```{error}```")

@client.event
async def on_member_join(member):
  global warncounter
  warncounter[member.id] = 0

@client.command()
async def help(ctx):
  embed = discord.Embed(
    title = "Help Station",
    description = "Learn about commands or smth",
    color = discord.Color.blue()
  )
  embed.add_field(
    name = "Moderation",
    value = "kick,ban,warn"
  )
  await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason = "No Reason Provided!"):
  await ctx.send(f"Banned {member.mention}. Reason = {reason}")
  try:
    await member.send(f"You were Banned from Wozee's Bakery. Reason: {reason}")
  except:
    await ctx.send("Couldn't DM member")
  
  await member.ban()

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason = "No Reason Provided!"):
  await ctx.send(f"Kicked {member.mention}. Reason: {reason}")
  try:
    await member.send(f"You were kicked from Wozee's Bakery. Reason: {reason}")
  except:
    await ctx.send("Couldn't DM Member")
  
  await member.kick()

@client.command()
async def warn(ctx, member: discord.Member, *, reason = "No Reason Provided!"):
  await ctx.send(f"Warned {member.mention}. Reason: {reason}")
  try:
    await member.send(f"You were warned from Wozee's Bakery. Reason: {reason}")
  except:
    await ctx.send("Couldn't DM Member")

keep_alive()
client.run(os.environ['TOKEN'])
