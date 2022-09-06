#-*- coding: utf-8 -*-

#**********************************************************************************************************************

def modifyFigure(content):
	tempContent = ""
	pos = content.upper().find("<FIGURE ")
	while pos > -1:
		# find figure tag <figure ...> to </figure>
		completeFigureTag = content[pos:]
		completeFigureTagEndPos = completeFigureTag.upper().find("</FIGURE>") + 9
		completeFigureTag = completeFigureTag[:completeFigureTagEndPos]
		
		# find figure text
		figureTextStartPos = completeFigureTag.upper().find(">") + 1
		figureTextEndPos = completeFigureTag.upper().find("</FIGURE>")
		figureText = completeFigureTag[figureTextStartPos:figureTextEndPos]

		# if there is a <figcaption> tag
		newFigureText = ""
		if figureText.upper().find("<FIGCAPTION") > 0:

			# find figcaption tag <figcaption ...> to </figcaption>
			figcaptionStartPos = figureText.upper().find("<FIGCAPTION")
			figcaptionEndPos = figureText.upper().find("</FIGCAPTION>") + 13
			figcaptionTag = figureText[figcaptionStartPos:figcaptionEndPos]
			
			# find figcaption text
			figcaptionTextStartPos = figcaptionTag.upper().find(">") + 1
			figcaptionTextEndPos = figcaptionTag.upper().find("</FIGCAPTION>")
			figcaptionText = figcaptionTag[figcaptionTextStartPos:figcaptionTextEndPos]
			
			# create new figcaption tag
			newFigcaptionTag = "<figcaption class='postfigcaption'>" + figcaptionText + "</figcaption>"
			
			# create new figure text with new figcaption tag
			newFigureText = figureText[:figcaptionStartPos] + newFigcaptionTag + figureText[figcaptionEndPos:]
		
		# if there is not <figcaption> tag
		else:
			# use old figure text
			newFigureText = figureText
		
		# create new figure tag
		newFigureTag = "<figure class='postfigure'>" + newFigureText + "</figure>"
		
		# temporary content with modified <figure ...> tag
		tempContent += content[:pos]
		tempContent += newFigureTag
		
		# continue search content
		content = content[pos + completeFigureTagEndPos:]
		pos = content.upper().find("<FIGURE ")

	tempContent += content
	# return modified content
	return tempContent

#**********************************************************************************************************************