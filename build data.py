# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:08:17 2020

@author: Hal
Rebuilds "default" tales.json
"""

import tale_manager


        
tags = {}
cmd = "gosling"
author= "Unknown"
added_by="Henry"
title = "That Time I Met Ryan Gosling"
string = """I saw Ryan Gosling at a grocery store in Los Angeles yesterday. I told him how cool it was to meet him in person, but I didn’t want to be a douche and bother him and ask him for photos or anything.

He said, “Oh, like you’re doing now?”

I was taken aback, and all I could say was “Huh?” but he kept cutting me off and going “huh? huh? huh?” and closing his hand shut in front of my face. I walked away and continued with my shopping, and I heard him chuckle as I walked off. When I came to pay for my stuff up front I saw him trying to walk out the doors with like fifteen Milky Ways in his hands without paying.

The girl at the counter was very nice about it and professional, and was like “Sir, you need to pay for those first.” At first he kept pretending to be tired and not hear her, but eventually turned back around and brought them to the counter.

When she took one of the bars and started scanning it multiple times, he stopped her and told her to scan them each individually “to prevent any electrical infetterence,” and then turned around and winked at me. I don’t even think that’s a word. After she scanned each bar and put them in a bag and started to say the price, he kept interrupting her by yawning really loudly."""

tale_manager.add_tale_headless(cmd,title,author,added_by,string,overwrite=True,save=False)


tags = {}
cmd = "painter"
author="Unknown"
added_by="Henry"
title = "The Master Painter"
string = """Once there was a master painter who had experienced the most beautiful thing in the universe. It was his intention to use his gift to hold the experience within a painting, such that it would last forever and he could share it with others.
But as he thought about it, he thought: wouldn't its being shared dilute the power of the experience? So he held it to himself, precious thing that it was, and aged with the memory. But as he aged, the memory became tarnished and beaten, and he could no longer recall the glory of the experience.
"""

tale_manager.add_tale_headless(cmd,title,author,added_by,string,overwrite=True, save=True)
