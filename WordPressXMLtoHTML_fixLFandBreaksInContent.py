#-*- coding: utf-8 -*-

#**********************************************************************************************************************

def fixMultipleBreaks(content):
	content = content.replace("<br><br><br><br>", "")
	content = content.replace("<br><br><br>", "<br>")
	content = "<p>" + content + "</p>"
	content = content.replace("<p><br><p>", "<p><p>")
	return content

#**********************************************************************************************************************
	
def fixLFandBreaksInContent(content):
	tempContent = ""
	pos = content.upper().find("<TABLE")
	while pos > -1:
		# find <table...> to </table> tag
		tableTag = content[pos:]
		endTagPos = tableTag.upper().find("</TABLE>") + 8
		tableTag = tableTag[:endTagPos]
		
		# fix <table...> tag
		newTableTag = fixMultipleBreaks(tableTag)
		
		# fix content before <table...> tag
		fixedContent = content[:pos].replace("\n", "<br>")
		fixedContent = fixMultipleBreaks(fixedContent)
		
		# temporary content with fixed breaks and LF
		tempContent += fixedContent
		tempContent += newTableTag
		
		# continue search content
		content = content[pos + endTagPos:]
		pos = content.upper().find("<TABLE")

	# fix remaining content
	content = content.replace("\n", "<br>")
	content = fixMultipleBreaks(content)

	tempContent += content
	
	# return modified content
	return tempContent
	
#**********************************************************************************************************************
