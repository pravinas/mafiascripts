import urllib2
import time

threadBase = "http://www1.flightrising.com/forums/forga/1643194/"
maxPage = 123
outputCSV = open('playerlist.txt', 'wb')
playerset = set()

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
    playerset.add(poster)
    outputCSV.write(poster+delim)

for i in range(1, maxPage+1):
    print "page", i
    time.sleep(0.2)
    filename = urllib2.urlopen(threadBase+str(i))
    parsePage(filename, str(i))
outputCSV.close()

for player in playerset:
    print player
