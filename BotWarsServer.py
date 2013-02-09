import httplib, urllib
import base64

class BotWarsServer:

	def __init__(self, server):
		self.connection = httplib.HTTPConnection(server)

	def submit(self, teamname, teampassword, problemnumber, filename):
		params = {}
		params["teamname"]=teamname
		params["teampassword"]=teampassword
		params["problemnumber"]=problemnumber
		params["filename"]=filename
		program=open(filename)
		programData=program.read()
		params["filedata"]=base64.b64encode(programData)
		headers= {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
		self.connection.request("POST", "/dump", urllib.urlencode(params), headers)
		response = self.connection.getresponse()
		print "Status:", response.status
		print "Body:", response.read()

	def ping(self):
		self.connection.request("GET","/")
		response = self.connection.getresponse()
		print "Status:", response.status
		print "Body:", response.read()
