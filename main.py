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
