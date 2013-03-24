#!/usr/bin/python
#
# This file is part of the BotWars-Client program.
# Copyright (C) 2013 Suhail Sherif, Rajat Khanduja
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import re
from BotWarsServer import *
import validators

usage='''
	python main.py <server ip> <server port> <teamname> <teampassword> <command+>
where command+ is one of:
	submit <problem number> <filename>
	ask <problem number> <doubt>
	leaderboard
	score
'''

def main(args):
	serverIP=args[0]
	if not validators.validIP(serverIP):
		print "Invalid server IP"
		return

	serverPort=args[1]
	try:
		int(serverPort)
	except ValueError:
		print "Invalid server port"
		return

	server = BotWarsServer(serverIP+":"+serverPort)

	teamName=args[2]
	teamPassword=args[3]

	if args[4]=="submit":
		if len(args)<7:
			print usage
			return
		problemNumber = args[5]
		fileName = args[6]
		if not validators.validFile(fileName):
			print "Invalid filename"
			return
		server.submit(teamName, teamPassword, problemNumber, fileName)

	elif args[4]=="ask":
		if len(args)<6:
			print usage
			return
		problemNumber = args[5]
		doubt = reduce(lambda x,y: x+" "+y, args[6:])
		server.ask(teamName, teamPassword, problemNumber, doubt)

	elif args[4]=="leaderboard":
		server.getLeaderboard(teamName, teamPassword)

	elif args[4]=="score":
		server.getScore(teamName, teamPassword)

	else:
		print usage
		return

if __name__=="__main__":
	if len(sys.argv)<6:
		print usage
	else:
		main(sys.argv[1:])
