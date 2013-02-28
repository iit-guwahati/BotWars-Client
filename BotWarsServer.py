import httplib, urllib
import base64
import os

class BotWarsServer:

	def __init__(self, server):
		self.connection = httplib.HTTPConnection(server)

	def submit(self, teamname, teampassword, problemnumber, filename):
		params = {}
		params["type"]="submit"
		params["teamname"]=teamname
		params["teampassword"]=teampassword
		params["problemnumber"]=problemnumber
		params["filename"]=filename.split(os.sep)[-1]
		program=open(filename)
		programData=program.read()
		params["filedata"]=base64.b64encode(programData)
		headers= {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
		self.connection.request("POST", "/submit", urllib.urlencode(params), headers)
		response = self.connection.getresponse()
		print "Solution sent. Response:-"
		print "Status:", response.status
		print "Body:", response.read()

	def ask(self, teamname, teampassword, problemnumber, doubt):
		params={}
		params["type"]="doubt"
		params["teamname"]=teamname
		params["teampassword"]=teampassword
		params["problemnumber"]=problemnumber
		params["doubt"]=doubt
		headers= {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
		self.connection.request("POST", "/doubt", urllib.urlencode(params), headers)
		response = self.connection.getresponse()
		print "Doubt sent. Response:-"
		print "Status:", response.status
		print "Body:", response.read()

	def getLeaderboard(self, teamname, teampassword):
		params={}
		params["type"]="leaderboard"
		params["teamname"]=teamname
		params["teampassword"]=teampassword
		headers= {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
		self.connection.request("POST", "/leaderboard", urllib.urlencode(params), headers)
		response = self.connection.getresponse()
		print "Score request sent. Response:-"
		print "Status:", response.status
		print "Body:", response.read()

	def getScore(self, teamname, teampassword):
		params={}
		params["type"]="score"
		params["teamname"]=teamname
		params["teampassword"]=teampassword
		headers= {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
		self.connection.request("POST", "/score", urllib.urlencode(params), headers)
		response = self.connection.getresponse()
		print "Score request sent. Response:-"
		print "Status:", response.status
		print "Body:", response.read()

	def ping(self):
		self.connection.request("GET","/")
		response = self.connection.getresponse()
		print "Status:", response.status
		print "Body:", response.read()
