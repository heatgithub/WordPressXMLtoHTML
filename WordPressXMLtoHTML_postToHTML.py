#-*- coding: utf-8 -*-

# import functions
from WordPressXMLtoHTML_modifyLinks import modifyLinks
from WordPressXMLtoHTML_removeDivTags import removeDivTags
from WordPressXMLtoHTML_removeCommentTags import removeCommentTags
from WordPressXMLtoHTML_modifyFigure import modifyFigure
from WordPressXMLtoHTML_modifyImage import modifyImage
from WordPressXMLtoHTML_removeIllegalFileNameCharacters import removeIllegalFileNameCharacters
from WordPressXMLtoHTML_fixLFandBreaksInContent import fixLFandBreaksInContent

#**********************************************************************************************************************

def getNextAndPreviousPost(postList, postDateTime):
	nextPost = ""
	previousPost = ""
	nextLink = ""
	previousLink = ""
	
	# search postList for current post based on date and time
	i = 0
	while (i < len(postList)):
		if (postDateTime == postList[i].postDateTime):
			# if first post in list
			if (i == 0):
				previousPost = ""
				previousLink = ""
			else:
				previousPost = postList[i - 1].postDateTime[:10] + " " + postList[i - 1].title
				previousLink = postList[i - 1].postDateTime[:10] + "_" + postList[i - 1].title.replace(" ", "-") + ".html"
				previousLink = removeIllegalFileNameCharacters(previousLink) # replace som illegal characters
			# if last post in list
			if (i == len(postList) - 1):
				nextPost = ""
				nextLink = ""
			else:
				nextPost = postList[i + 1].postDateTime[:10] + " " + postList[i + 1].title
				nextLink = postList[i + 1].postDateTime[:10] + "_" + postList[i + 1].title.replace(" ", "-") + ".html"
				nextLink = removeIllegalFileNameCharacters(nextLink) # replace som illegal characters
		# increase i
		i += 1
	
	return nextPost, previousPost, nextLink, previousLink

#**********************************************************************************************************************

def postToHTML(postType, postList, pageList, title, description, favIconFileNameAndPath, postTitle, postDateTime, lastModifiedDateTime, content, categoriesList, commentsList):
	# folder and file name for the html file
	folder = postType + "s"
	htmlFileFolder = title + "/" + folder
	htmlFileName = postDateTime[:10] + "_" + postTitle.replace(" ", "-") + ".html"
	htmlFileName = removeIllegalFileNameCharacters(htmlFileName) # replace som illegal characters
	htmlFolderAndFileName = htmlFileFolder + "/" + htmlFileName
	
	# create and write to the html file
	with open(htmlFolderAndFileName, 'w', encoding='utf-8') as f:
		# start of page with <title>
		f.write("<!DOCTYPE html>\n")
		f.write("<html>\n")
		f.write("<head>\n")
		f.write("\t<meta charset='UTF-8'>\n")
		f.write("\t<meta name='application-name' content='WordPressXMLtoHTML.py'>\n")
		f.write("\t<title>" + postTitle + " | " + title + "</title>\n")
		f.write("\t<link rel='stylesheet' href='../" + title.replace(" ", "-") + ".css'>\n")
		f.write("\t<link rel='icon' type='image/x-icon' href='../media/" + favIconFileNameAndPath + "'>\n")
		f.write("</head>\n")
		f.write("<body>\n")
		f.write("\t<div class='body'>\n")

		# header
		f.write("\t\t<header>\n")
		f.write("\t\t\t<div class='header'>\n")
		f.write("\t\t\t\t<h1>" + title + "</h1>\n")
		f.write("\t\t\t\t<div class='headerdescription'>\n")
		f.write("\t\t\t\t\t" + description + "\n")
		f.write("\t\t\t\t</div>\n")
		f.write("\t\t\t</div>\n")
		f.write("\t\t</header>\n")
		
		# navigation
		if postType == "post":
			nextPost, previousPost, nextLink, previousLink = getNextAndPreviousPost(postList, postDateTime)
			f.write("\t\t<div class='navigation'>\n")
			if (previousLink != ""):
				f.write("\t\t\t<p><a href='" + previousLink + "'>" + "< " + previousPost + "</a></p>\n")
			else:
				f.write("\t\t\t<p></p>\n")
			if (nextLink != ""):
				f.write("\t\t\t<p><a href='" + nextLink + "'>" + nextPost + " >" + "</a></p>\n")
			else:
				f.write("\t\t\t<p></p>\n")
			f.write("\t\t</div>\n")
		
		# post title
		f.write("\t\t<div class='posttitle'>\n")
		f.write("\t\t\t<h1>" + postTitle + "</h1>\n")
		f.write("\t\t</div>\n")
		# post date and time
		f.write("\t\t<div class='postdatetime'>\n")
		f.write("\t\t\t<p>Published: " + postDateTime)
		if lastModifiedDateTime != postDateTime:
			f.write(", Last modified: " + lastModifiedDateTime)
		f.write("</p>\n")
		f.write("\t\t</div>\n")
		# post content
		content = removeCommentTags(content)
		content = removeDivTags(content)
		content = modifyLinks(content)
		content = modifyFigure(content)
		content = modifyImage(content)
		content = fixLFandBreaksInContent(content)
		f.write("\t\t<div class='postcontent'>\n")
		f.write("\t\t\t" + content + "\n")
		f.write("\t\t</div>\n")
		
		# categories
		if len(categoriesList) > 0:
			cats = 0
			f.write("\t\t<div class='categories'>\n")
			f.write("\t\t\t<p>Categories: ")
			for category in categoriesList:
				if cats > 0: f.write(", ")
				f.write(category)
				cats += 1
			f.write("</p>\n")
			f.write("\t\t</div>\n")
			
		# comments
		if len(commentsList) > 0:
			for comment in commentsList:
				f.write("\t\t<div class='commentdate'>\n")
				f.write("\t\t\t(" + comment.dateTime + ") " + comment.author + ":<br>\n")
				f.write("\t\t</div>\n")
				f.write("\t\t<div class='comment'>\n")
				#f.write("\t\t\t" + comment.content.replace("\n", "<br>") + "<br>\n")
				f.write("\t\t\t" + comment.content + "<br>\n")
				f.write("\t\t</div>\n")
		
		# end page
		f.write("\t</div>\n")
		f.write("</body>\n")
		f.write("</html>\n")		
	
#**********************************************************************************************************************
