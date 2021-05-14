import discord # Import discord library
from discord.ext import commands
import json # Import json library
import os # Allow to interact with the os (operating system)

with open("./config.json") as f:
    configData = json.load(f)

prefix = configData["prefix"] # The prefix from the "config.json" file
token = configData["token"] # The token from the "config.json" file

bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help") # Remove the default help command (Optional)

@bot.event
async def on_ready(): # Event that work when the bot is ready
    print(f'{bot.user} Online.') # Print in the console "Username#0000 Online."

@bot.command
async def ping(ctx):
    await ctx.send("Pong!") # Sends "Pong!" in chat
    await ctx.author.send("Pong!") # Sends "Pong!" in dm to the message author

bot.run(token) # Start the bot