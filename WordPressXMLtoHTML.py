#-*- coding: utf-8 -*-

# import python standard modules
import os
import sys
import operator
import xml.etree.ElementTree as ET
# import classes
from WordPressXMLtoHTML_classes import commentData
from WordPressXMLtoHTML_classes import postAndPageData
# import functions
from WordPressXMLtoHTML_findWPFileNameAndPath import findWPFileNameAndPath
from WordPressXMLtoHTML_postToHTML import postToHTML
from WordPressXMLtoHTML_createHTMLIndex import createHTMLIndex

# define som variables
prgName = "WordPressXMLtoHTML"
prgVersion = "1.00"
prgDate = "2022-09-06"
inputFileName = ""

# print program information
print(prgName + ", v" + prgVersion + ", " + prgDate)

# check program arguments
numOfArgs = len(sys.argv) - 1 # - 1 because 0 = name of the program

# are there no arguments so end the program and print name of program, version and syntax
if numOfArgs == 0:
	print("Usage: " + prgName + " input_file_name.xml")
	sys.exit()

# if one or more parameters, take the first parameter as file name for input, ie the xml file
inputFileName = sys.argv[1]

# check that input file exist
if os.path.exists(inputFileName) == False:
	print("Can't find input file: " + inputFileName + "")
	sys.exit()

# open and read the xml file
print("Opening " + inputFileName)
wpTree = ET.parse(inputFileName)
wpRoot = wpTree.getroot()

# get the namespaces used in the xml file to access the namespace prefixes needed to read some tags (like <wp:post_type>)
namespaces = dict([node for _, node in ET.iterparse(inputFileName, events=['start-ns'])])

# the blogs title, description, link and favicon
title = wpRoot.find("channel/title").text
description = wpRoot.find("channel/description").text
link = wpRoot.find("channel/link").text
favIconURL = wpRoot.find("channel/image/url").text

# fix path to favIcon
favIconFileName = findWPFileNameAndPath(favIconURL)

# create a folder with same name as the blogs title
if not os.path.exists(title):
	os.makedirs(title)
# create subfolders for posts and pages
if not os.path.exists(title + "/" + "posts"):
	os.makedirs(title + "/" + "posts")
if not os.path.exists(title + "/" + "pages"):
	os.makedirs(title + "/" + "pages")

# read all categories
print("Reading categories")
categories = []
for x in wpRoot.findall("channel/wp:category/wp:cat_name", namespaces):
	categories.append(x.text)

# read all tags
print("Reading tags")
tags = []
for x in wpRoot.findall("channel/wp:tag/wp:tag_name", namespaces):
	tags.append(x.text)

# initialize data for posts ang pages index
postList = []
pageList = []
print("Preparing for index")
for x in wpRoot.findall("channel/item"):
	postType = x.find("wp:post_type", namespaces).text
	# data for post index
	if postType == "post":
		p = postAndPageData()
		p.postDateTime = x.find("wp:post_date", namespaces).text
		p.title = x.find("title", namespaces).text
		postList.append(p)

	# data for page index
	if postType == "page":
		p = postAndPageData()
		p.postDateTime = x.find("wp:post_date", namespaces).text
		p.title = x.find("title", namespaces).text
		pageList.append(p)
# sort postList and page List
postList.sort(key=operator.attrgetter('postDateTime'))
pageList.sort(key=operator.attrgetter('postDateTime'))

#***** create index page for posts and pages *****
print("Creating index")
createHTMLIndex(postList, pageList, title, description, favIconFileName)
		

#***** process all <item> which can be post, page and attachment *****
#print("Processing posts, pages and attachments:")
print("Processing posts and pages: ", end="")
for x in wpRoot.findall("channel/item"):
	postType = x.find("wp:post_type", namespaces).text
	#***** post and page ***********************************************************************************************
	if postType == "post" or postType == "page":
		# the post
		postTitle = x.find("title", namespaces).text
		postDateTime = x.find("wp:post_date", namespaces).text
		lastModifiedDateTime = x.find("wp:post_modified", namespaces).text
		content = x.find("content:encoded", namespaces).text
		# categories
		categoriesList = []
		for c in x.findall("category", namespaces):
			categoriesList.append(c.text)
		# the comments
		commentsList = []
		for c in x.findall("wp:comment", namespaces):
			comment = commentData()
			comment.author = c.find("wp:comment_author", namespaces).text
			comment.dateTime = c.find("wp:comment_date", namespaces).text
			comment.content = c.find("wp:comment_content", namespaces).text
			commentsList.append(comment)
		# make html page of the post
		postToHTML(postType, postList, pageList, title, description, favIconFileName, postTitle, postDateTime, lastModifiedDateTime, content, categoriesList, commentsList)
		# done with this one
		print(".", end="")


	#***** attachment **************************************************************************************************
	# attachments are ignored at this moment
	#if postType == "attachment":
		#filename = x.find("title", namespaces).text
		#print(".", end="")


print("\nDone! " + str(len(postList)) + " posts and " + str(len(pageList)) + " pages created.")

