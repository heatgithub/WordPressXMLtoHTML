#-*- coding: utf-8 -*-

from WordPressXMLtoHTML_classes import postAndPageData
from WordPressXMLtoHTML_classes import months
from WordPressXMLtoHTML_removeIllegalFileNameCharacters import removeIllegalFileNameCharacters

#**********************************************************************************************************************

def createHTMLIndex(postList, pageList, title, description, favIconFileNameAndPath):
	# folder and file name for the html file
	htmlFolderAndFileName = title + "/" + "index.html"
	
	# create and write to the html file
	with open(htmlFolderAndFileName, 'w', encoding='utf-8') as f:
		# start of page with <title>
		f.write("<!DOCTYPE html>\n")
		f.write("<html>\n")
		f.write("<head>\n")
		f.write("\t<meta charset='UTF-8'>\n")
		f.write("\t<meta name='application-name' content='WordPressXMLtoHTML.py'>\n")
		f.write("\t<title>" + "Index" + " | " + title + "</title>\n")
		f.write("\t<link rel='stylesheet' href='" + title.replace(" ", "-") + ".css'>\n")
		f.write("\t<link rel='icon' type='image/x-icon' href='media/" + favIconFileNameAndPath + "'>\n")
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

		# pages title
		f.write("\t\t<div class='indexpagetitle'>\n")
		f.write("\t\t\t<h1>" + "Pages" + "</h1>\n")
		f.write("\t\t</div>\n")
		# pages
		f.write("\t\t<div class='indexpages'>\n")
		for p in pageList:
			htmlFileName = p.postDateTime[:10] + "_" + p.title.replace(" ", "-") + ".html"
			htmlFileName = removeIllegalFileNameCharacters(htmlFileName) # replace som illegal characters
			f.write("\t\t\t" + "<a href='pages/" + htmlFileName + "'>" + p.title + "</a>")
			f.write("<br>\n")
		f.write("\t\t</div>\n")

		f.write("\t\t<br>\n")

		# posts title
		f.write("\t\t<div class='indexpagetitle'>\n")
		f.write("\t\t\t<h1>" + "Posts" + "</h1>\n")
		f.write("\t\t</div>\n")
		# posts
		f.write("\t\t<div class='indexposts'>\n")
		oldYear = ""
		oldMonth = ""
		for p in postList:
			if p.postDateTime[:4] != oldYear:
				f.write("\t\t\t<div class='indexpostsyear'>\n")
				f.write("\t\t\t\t<h2>" + p.postDateTime[:4] + "</h2>\n")
				f.write("\t\t\t</div>\n")
				oldYear = p.postDateTime[:4]			
			if p.postDateTime[5:7] != oldMonth:
				f.write("\t\t\t<div class='indexpostsmonth'>\n")
				f.write("\t\t\t\t<h4>" + months[int(p.postDateTime[5:7])] + "</h4>\n")
				f.write("\t\t\t</div>\n")
				oldMonth = p.postDateTime[5:7]
			htmlFileName = p.postDateTime[:10] + "_" + p.title.replace(" ", "-") + ".html"
			htmlFileName = removeIllegalFileNameCharacters(htmlFileName) # replace som illegal characters
			f.write("\t\t\t" + "<a href='posts/" + htmlFileName + "'>" + p.postDateTime[:10] + " " + p.title + "</a>")
			f.write("<br>\n")
		f.write("\t\t</div>\n")

		f.write("\t\t<br>\n")

		# end page
		f.write("\t</div>\n")
		f.write("</body>\n")
		f.write("</html>\n")		
		
#**********************************************************************************************************************