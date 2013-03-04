Utility
--------

This client-side tool is meant to interact with the BotWars Server 
(https://github.com/WebAndCodingClub-IITGuwahati/BotWars-Server). This provides
an interface to submit files corresponding to particular problems, view score
gained by all entries and to check the leaderboard.

What is BotWars?
----------------

BotWars is the name given to the programming competition format that aims at 
bringing participants together to try and create code that outperforms others'
code. Unlike algorithmic challenges, these competitions don't have a fixed
output or a fixed score. The better the solution produced by your code, the 
higher you can score and, consequently, move up the leaderboard.

Instructions
------------

This utility is written in Python and requires the user to have a Python
interpreter installed on his computer. 

- To run this, execute the following command to submit a solution for a problem:
    `$ python main.py <server> <port> <username> <password> submit <problem_name> <filename>`

- To view leaderboard or score, 
    `$ python main.py <server> <port> <username> <password> [leaderboard|score]`
