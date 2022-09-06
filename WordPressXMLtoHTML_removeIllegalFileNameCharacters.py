#-*- coding: utf-8 -*-

#**********************************************************************************************************************

def removeIllegalFileNameCharacters(fileName):

	keepcharacters = (' ', '.' ,'_', '-')
	legalFileName = "".join(c for c in fileName if c.isalnum() or c in keepcharacters).rstrip()

	return legalFileName

#**********************************************************************************************************************