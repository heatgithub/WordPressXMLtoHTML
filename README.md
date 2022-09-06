# WordPressXMLtoHTML.py

Converts downloaded blog from WordPress, including media, to HTML pages.

## Prerequests and preparation

Export the blog content from WordPress as an XML file.

Save the XML file in a folder where the HTML pages will be created.

Export the media library from WordPress.

Make sure you have Python installed!

## Running the script to create the HTML pages

Put all the WordPressXMLtoHTML python script files in the folder containing the downloaded XML file.

Run the script like this: `python.exe WordPressXMLtoHTML.py wp_blog_content.xml` (change the name of XML file).

After this there will be a subfolder with same name as the blogs name. This subfolder will have two folders named _pages_ 
and _posts_ containing pages and posts from the blog. There will also be a _index.html_ with clickable links to all
pages and posts.

## Adding the media library to the HTML pages

In the same folder as _pages_ and _posts_, create a new folder named _media_. Extract all the media files from the 
downloaded media library into this _media_ folder, including all subfolders (named YYYY/MM).

## Styling the HTML pages

Without a CSS file with styling, the HTML pages will look rather dull. The created HTML pages contains a lot of
`<div>` tags with class names that can be used.

Create a CSS file with the same name as the blog (change spaces to - [minus sign]) and save it in the first folder
together with the _index.html_ file.

Among all the python script files, there is a CSS sample file named _WordPressXMLtoHTML.css_ that can be used.