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

import tale_manager

def split_into_sections(text, charlim):
    if len(text) < charlim:
        return [text]
    else:
        words = iter(text.split(" "))
        lines, current = [], next(words)
        for word in words:
            if len(current) + 1 + len(word) > charlim:
                lines.append(current)
                current = word
            else:
                current += " " + word
        lines.append(current)
        return lines

def reload_tales():
    global TALES
    with open("tales.json") as infile:
        TALES = json.load(infile)


DISCORD_TOKEN="TOKEN GOES HERE"
DISCORD_GUILD="SERVERNAME GOES HERE"

global TALES, PREV_ID
TALES = None
PREV_ID = None
reload_tales()


start_time = time.time()

bot = commands.Bot(command_prefix='!')
bot.remove_command("help")
@bot.event
async def on_ready():
    print(bot.user.name," has connected")
    await bot.change_presence(status=discord.Status.online, activity=discord.CustomActivity("just vibing"))
    
@bot.command(name="updatequeue")
async def updatequeue(context):
    if tale_manager.read_responses_into_queue():
        await context.send("No updates found")
    else:
        await context.send("Queue updated.")
        print("Queue updated")
    return

@bot.command(name="uptime")
async def uptime(context):
    upt = str(round((time.time()-start_time)/60,3))
    await context.send("*uptime:* "+upt+" minutes")
    print("*uptime:* "+upt+" minutes")
    
@bot.command(name="reviewnext")
async def review(context):
    print("Reviewing queue item")
    try:
        with open("queue.json") as infile:
            QUEUE = json.load(infile)
    except:
        QUEUE = {}
    
    if not QUEUE:
        await context.send("Queue empty or missing")
        return
    key = next(iter(QUEUE))
    candidate = QUEUE[key]
    await context.send("**Candidate story: "+ candidate[0]['title']+"**")
    full_story = split_into_sections(candidate[1], 2000)
    for section in full_story:
        await context.send(section)
    await context.send("*Uploaded by "+ candidate[0]["added_by"]+"*")
    await context.send("\n Approve message? (Y/N): ")
    try:
        msg = await bot.wait_for('message',timeout=60)
    except:
        await context.send("Timed out, no action taken")
        return
    msg = msg.content
    if msg == "Y":
        if tale_manager.promote_from_queue(key):
            await context.send("Unknown error, no action taken")
            return
        else:
            await context.send("Story promoted out of queue and into database.")
            reload_tales()
            print("Queue item promoted")
            await context.send("Story database reloaded")
    elif msg == "N":
        await context.send("Story rejected and deleted from queue.")
    else:
        await context.send("Input not recognised, no action taken.")
    return

@bot.command(name="exists")
async def exists(context,*args):
    print("Exist check called")
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
    print("Story database reloaded")
    await context.send("Story database reloaded")
    
@bot.command(name="story")
async def story(context, *args):
    print("Telling story...")
    if not TALES:
        await context.send("No tales in database!")
        return
    taleID = False
    if len(args) == 0:
        print("Random story:")
        taleID = random.choice(list(TALES.keys()))
    elif args[0] in TALES:
        taleID = args[0]
        
    if taleID:
        print("ID: ", taleID)
        global PREV_ID 
        PREV_ID = taleID
        full_story = split_into_sections(TALES[taleID][1], 2000)
        for section in full_story:
            await context.send(section)
        
@bot.command(name="moreinfo")
async def moreinfo(context):
    print("Moreinfo requested")
    if not PREV_ID:
        await context.send("No previous story detected")
        return
    else:
        lines = []
        for key in TALES[PREV_ID][0].keys():
            lines.append("*"+key+":* "+str(TALES[PREV_ID][0][key]))
        lines.append("*command:* !story "+PREV_ID)
        response = "\n".join(lines)
        await context.send(response)
     
@bot.command(name="add")
async def add(context):
    await context.send("To contribute your own story, go to: CENSORED" )

@bot.command(name="help")
async def gimmickhelp(context):
    print("Help requested")
    msg = """ 
    *!story [ID]* - tells you a story (will pick a random story if [ID] is left blank)
    *!moreinfo* - displays info about the most recently-told story
    *!exists [ID]* - tells you if ID exists in the database or not
    *!add* - contribute your own story!
    *!reload* - reloads story database
    *!updatequeue* - checks for new submissions of stories
    *!reviewnext* - approve/disapprove next item in submission queue
    """
    await context.send(msg)
    

bot.run(DISCORD_TOKEN)
