#-*- coding: utf-8 -*-

from WordPressXMLtoHTML_findWPFileNameAndPath import findWPFileNameAndPath
from WordPressXMLtoHTML_findWPFileNameAndPathFromIMGTag import findWPFileNameAndPathFromIMGTag

#**********************************************************************************************************************

def modifyImage(content):
	tempContent = ""
	pos = content.upper().find("<IMG ")
	while pos > -1:
		# find link tag <img ... to >
		completeImageTag = content[pos:]
		completeImageTagEndPos = completeImageTag.upper().find(">") + 1
		completeImageTag = completeImageTag[:completeImageTagEndPos]
	
		# path to image
		imageFileName = findWPFileNameAndPathFromIMGTag(completeImageTag)
		
		# create new image tag
		newImgTag = "<img src='../media/" + imageFileName + "' class='postimage' alt='' />"
		
		# temporary content with modified <img ... to > tag
		tempContent += content[:pos]
		tempContent += newImgTag
		
		# continue search content
		content = content[pos + completeImageTagEndPos:]
		pos = content.upper().find("<IMG ")

	tempContent += content
	# return modified content
	return tempContent

#**********************************************************************************************************************