#-*- coding: utf-8 -*-

from WordPressXMLtoHTML_findWPFileNameAndPath import findWPFileNameAndPath

#**********************************************************************************************************************

def findWPFileNameAndPathFromIMGTag(imageTag):
	# find the <img> tag
	pos = imageTag.upper().find("<IMG")
	imgTag = imageTag[pos:]
	endTagPos = imgTag.upper().find(">") + 1
	imgTag = imgTag[:endTagPos]

	fileName = findWPFileNameAndPath(imgTag)
	
	return fileName

#**********************************************************************************************************************