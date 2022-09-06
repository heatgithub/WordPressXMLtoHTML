#-*- coding: utf-8 -*-

#**********************************************************************************************************************

def removeDivTags(content):
	tempContent = ""
	pos = content.upper().find("<DIV")
	while pos > -1:
		# find <div...> to </div> tag
		divTag = content[pos:]
		endTagPos = divTag.upper().find("</DIV>") + 6
		divTag = divTag[:endTagPos]
		
		# temporary content without <div...> to </div> tag
		tempContent += content[:pos]
		
		# continue search content
		content = content[pos + endTagPos:]
		pos = content.upper().find("<DIV")

	tempContent += content
	# return modified content
	return tempContent

#**********************************************************************************************************************
