#-*- coding: utf-8 -*-

#**********************************************************************************************************************

def removeCommentTags(content):
	tempContent = ""
	pos = content.upper().find("<!--")
	while pos > -1:
		# find <!-- to --> tag
		commentTag = content[pos:]
		endTagPos = commentTag.upper().find("-->") + 3
		commentTag = commentTag[:endTagPos]
		
		# temporary content without <!-- to --> tag
		tempContent += content[:pos]
		
		# continue search content
		content = content[pos + endTagPos:]
		pos = content.upper().find("<!--")

	tempContent += content
	# return modified content
	return tempContent

#**********************************************************************************************************************
