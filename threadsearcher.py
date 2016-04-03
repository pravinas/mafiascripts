import urllib2
import time

threadBase = "http://www1.flightrising.com/forums/forga/1654388/"
minPage = 80
maxPage = 88
searchAuthor = "JohnWatsGoingOn"
searchAuthor2 = "SmashedFish"
searchAuthor3 = "Druddigon8"
outputCSV = open(searchAuthor+'.html', 'wb')
outputCSV2 = open(searchAuthor2+'.html', 'wb')
outputCSV3 = open(searchAuthor3+'.html', 'wb')

def parsePage(f, page):
    #pagefile = open(filename, 'r')
    pagestring = f.read()
    #print pagestring
    postArray = pagestring.split('<a name=\"post_')
    for i in range(1, len(postArray)):
        #print "post", i
        post = postArray[i]
        parsePost(post, page)

def parsePost(post, page):
    #print post.split(">")[1].split("</div")[0]
    delim = '\n'
    postID = post.split("\"")[0]
    postContent = post.split("<span class=\"posttext\"")[1].split("</span>")[0]
    poster = post.split("style=\"font-weight:bold;color#731d08\">")[1].split("</a>")[0]
    postLink = threadBase + page + "#post_" + str(postID)
    #print "~~~"
    #print postLink
    #print poster
    #print postContent
    #outputCSV.write(postLink + delim +"poster\t" + poster + delim + postContent + "\n\n\n\n")
    if poster == searchAuthor:
        outputCSV.write("<hr><a href=\""+postLink+"\">Link to Post</a><p>"+postContent+"</p><hr>")
        for span in postContent.split("<span"):
            outputCSV.write("</span>")
    if poster == searchAuthor2:
        outputCSV2.write("<hr><a href=\""+postLink+"\">Link to Post</a><p>"+postContent+"</p><hr>")
        for span in postContent.split("<span"):
            outputCSV2.write("</span>")
    if poster == searchAuthor3:
        outputCSV3.write("<hr><a href=\""+postLink+"\">Link to Post</a><p>"+postContent+"</p><hr>")
        for span in postContent.split("<span"):
            outputCSV3.write("</span>")

for i in range(minPage, maxPage+1):
    print "page", i
    time.sleep(0.2)
    filename = urllib2.urlopen(threadBase+str(i))
    parsePage(filename, str(i))
outputCSV.close()
