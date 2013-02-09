import os

def validIP(ipaddress):
	ipParts = ipaddress.split('.')
	if not len(ipParts)==4:
		return False
	try:
		for i in [int(j) for j in ipParts]:
			if i<0 or i>255:
				return False
	except ValueError:
		return False
	return True

def validFile(fileName):
	if os.path.isfile(fileName):
		return True
	return False
