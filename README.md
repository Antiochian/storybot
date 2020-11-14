# storybot
A discord bot that will tell you stories, and remember stories that you tell it

All very W.I.P. and unfinished.

Quick summary of files:
----

*storybot.py* - actual bot file

*tales.json* - database of current known stories and metadata

*tale_manager.py* - interface for adding new storie to the database

*build_tales.py* - temporary script that creates a simple default database of 2 example stories

Currently supported commands:
----

 - !story [ID]
 
 Either tells you a random story (if no "ID" is given) or returns the requested story
 
 - !moreinfo
 
 Tells you more information about the most recently-posted story
 
 - !reload
 
 Reloads the story database
 
 - !exists
 
 Checks if ID exists in database

