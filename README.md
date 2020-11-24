# storybot

Recently I have been reading a lot about Welsh folk/fairy tales, and so I was inspired to create this discord bot which remembers and retells any story you tell it.
The cool feature is that users can add their own stories through a Google Form, and the program will interface with the Google API to automatically read and remember these submissions by placing them in a queue, before periodically going through the queue and reading queue stories into a database file to be stored permanently.

Note that there is not yet a good security/vetting system, so the Google Form ID is censored in this github repo to avoid trolls.

**Current Roadmap:**
 - [x] Discord API interface set up
 - [x] Story JSON database designed
 - [x] Basic commands (tell stories, display information)
 - [x] Google Drive API to allow users to add their own stories via Google Forms
 --- feature complete ----
 - [ ] Story vetting pipeline
 - [ ] Packagelock implemented for simultaneous access
 - [ ] embedded image/markdown support?
 
Quick summary of files:
----

*storybot.py* - actual bot file

*tale_manager.py* - interface for evaluating and adding new stories to the database automatically

*responses/read_responses.py* - Google API interface to read results of google poll

*tales.json* - database of current known stories and metadata

*queue.json* - database of queued stories (submitted via Google Forms but not approved yet)

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

