# storybot
A discord bot that will tell you stories, and remember stories that you tell it. The cool feature is that users can add their own stories through a Google Form, and the program will interface with the Google API to automatically read and remember these submissions.

All very W.I.P. and unfinished.

**Currenet Roadmap:**
 - [x] Discord API interface set up
 - [x] Story JSON database designed
 - [x] Basic commands (tell stories, display information)
 - [x] Google Drive API to allow users to add their own stories via Google Forms
 - [ ] Story vetting pipeline
 - [ ] Packagelock implemented for simultaneous access
 - [ ] TTS support
 - [ ] embedded image/markdown support?
 
Quick summary of files:
----

*storybot.py* - actual bot file

*tales.json* - database of current known stories and metadata

*tale_manager.py* - interface for adding new storie to the database

*build_tales.py* - temporary script that creates a simple default database of 2 example stories

Currently supported commands:
----
 - *!story [ID]* - tells you a story (will pick a random story if [ID] is left blank)
 - *!moreinfo* - displays info about the most recently-told story
 - *!exists [ID]* - tells you if ID exists in the database or not
 - *!add* - contribute your own story!
 - *!reload* - reloads story database
 - *!updatequeue* - checks for new submissions of stories
 - *!reviewnext* - approve/disapprove next item in submission queue
 - *!help* - list all commands

