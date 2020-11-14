# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 11:37:43 2020

@author: Hal
"""
import discord
from discord.ext import commands
import random
import nest_asyncio
nest_asyncio.apply()

import json
import time

DISCORD_TOKEN="EXAMPLE_TOKEN"
DISCORD_GUILD="EXAMPLE_SERVERNAME"

def reload_tales():
    global TALES
    with open("tales.json") as infile:
        TALES = json.load(infile)

global TALES, PREV_ID
TALES = None
PREV_ID = None
reload_tales()


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(bot.user.name," has connected")
    

@bot.command(name="exists")
async def exists(context,*args):
    if len(args) == 0:
        await context.send("Error: No query given")
        return
    pattern=args[0]
    if pattern in TALES:
        await context.send("Story ID '"+pattern+"' exists")
    else:
        await context.send("Story ID '"+pattern+"' does not exist")
    
@bot.command(name="reload")
async def reload(context):
    reload_tales()
    await context.send("Story database reloaded")
    
@bot.command(name="story")
async def story(context, *args):
    taleID = False
    if len(args) == 0:
        print("Random story:")
        taleID = random.choice(list(TALES.keys()))
    elif args[0] in TALES:
        taleID = args[0]
        
    if taleID:
        global PREV_ID 
        PREV_ID = taleID
        await context.send(TALES[taleID][1])
        
@bot.command(name="moreinfo")
async def moreinfo(context):
    if not PREV_ID:
        await context.send("No previous story detected")
        return
    else:
        lines = []
        for key in TALES[PREV_ID][0].keys():
            lines.append(key+": "+str(TALES[PREV_ID][0][key]))
        lines.append("command: !story "+PREV_ID)
        response = "\n".join(lines)
        await context.send(response)
        

bot.run(DISCORD_TOKEN)
