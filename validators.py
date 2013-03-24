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
