#-*- coding: utf-8 -*-

from WordPressXMLtoHTML_findWPFileNameAndPath import findWPFileNameAndPath
from WordPressXMLtoHTML_findWPFileNameAndPathFromIMGTag import findWPFileNameAndPathFromIMGTag
	
#**********************************************************************************************************************

def modifyLinks(content):
	tempContent = ""
	pos = content.upper().find("<A ")
	while pos > -1:
		# find link tag <a ...> to </a>
		completeLinkTag = content[pos:]
		completeLinkTagEndPos = completeLinkTag.upper().find("</A>") + 4
		completeLinkTag = completeLinkTag[:completeLinkTagEndPos]

		# find start link tag <a ...>
		startLinkTagEndPos = completeLinkTag.upper().find(">") + 1
		startLinkTag = completeLinkTag[:startLinkTagEndPos]
		startLinkTag = startLinkTag.replace("'", "\"")
		
		# find link url
		linkUrlStartPos = startLinkTag.upper().find("HREF=\"") + 6
		linkUrl = startLinkTag[linkUrlStartPos:]
		linkUrlEndPos = linkUrl.upper().find("\"")
		linkUrl = linkUrl[:linkUrlEndPos]
		
		# find link text
		linkTextStartPos = completeLinkTag.upper().find(">") + 1
		linkTextEndPos = completeLinkTag.upper().find("</A>")
		linkText = completeLinkTag[linkTextStartPos:linkTextEndPos]
		
		# create new link tag
		newLinkTag = ""
		
		# if the link is an image
		if linkText[:4].upper() == "<IMG":
			imageFileName = findWPFileNameAndPathFromIMGTag(linkText)
			newLinkTag = "<a href='../media/" + imageFileName + "' target='_blank' class='postlinkimage'>" + linkText + "</a>"
		# if the link is not an image
		else:
			newLinkTag = "<a href='" + linkUrl + "' target='_blank' class='postlink'>" + linkText + "</a>"
		
		# temporary content with modified <a ...> to </a> tag
		tempContent += content[:pos]
		tempContent += newLinkTag
		
		# continue search content
		content = content[pos + completeLinkTagEndPos:]
		pos = content.upper().find("<A ")

	tempContent += content
	# return modified content
	return tempContent

#**********************************************************************************************************************