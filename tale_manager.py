# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:58:01 2020

@author: Hal
"""


import json
import datetime


filename = "tales.json"
#data format:
#   data[name] = [{tags}, response string]

global TALES
try:
    with open("tales.json") as infile:
        TALES = json.load(infile)
except:
    TALES = {}
        
        
def add_tale_headless(cmd,title,author,added_by,string,overwrite=False,save=True):
    tags = {}
    added_on = datetime.datetime.now().strftime("%d-%b-%Y (%H:%M)")
    tags['title'] = title
    tags['author'] = author
    tags['added_by'] = added_by
    tags['added_on'] = added_on
    tags['length'] = len(string)
    global TALES
    if cmd in TALES and (not overwrite):
        inp = input("Warning: tale '"+cmd+"'already exists. Overwrite? Y/[n]: ")
        if inp != "Y":
            print("Quitting without changes.")
            return
        else:
            print("Overwriting...")
    TALES[cmd] = [tags, string]
    if save:
        with open( filename, 'w' ) as outfile:
            json.dump( TALES, outfile, sort_keys=True, indent=4, separators=(',', ': '))
            print("New database saved to", filename)


def add_tale_commandline():
    cmd=input("Story command/ID (eg: 'myStory'): ")
    title=input("Story title: ")
    if not title:
        title = "Unknown"
    author=input("Original Author: ")
    if not author:
        author="Unknown"
    added_by=input("Added by: ")
    if not added_by:
        added_by = unknown
    string=input("Story text: ")
    if (not string) or (not cmd):
        print("ERR: Story/command field cannot be blank. Exiting without changes")
        return
    else:
        add_tale_headless(cmd,title,author,added_by,string)
        
def save_tales():
    global TALES
    with open( filename, 'w' ) as outfile:
            json.dump( TALES, outfile, sort_keys=True, indent=4, separators=(',', ': '))
            print("New database saved to", filename)
            
