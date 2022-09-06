#-*- coding: utf-8 -*-

#**********************************************************************************************************************

def findWPFileNameAndPath(imagePath):
	# find the filename with year and month path but without wordpress adress
	wordpressAdress = "WORDPRESS.COM"
	pos = imagePath.upper().find(wordpressAdress) + len(wordpressAdress) + 1 # +1 in order to remove the / sign after the wordpress adress
	fileName = imagePath[pos:]
	endPos = fileName.upper().find("\"")
	fileName = fileName[:endPos]
	
	# remove any query string from file name
	qsPos = fileName.find("?")
	if qsPos > 0: fileName = fileName[:qsPos]
	
	return fileName

#**********************************************************************************************************************
