'''
@author Alex Trautman
Summer 2014
-tool which downloads This American Life podcasts
To use: -enter the range of episodes you want in the variables $start and $stop
        -run
'''

import urllib2
import sys
import time

#define some variables
url1 = "http://audio.thisamericanlife.org/jomamashouse/ismymamashouse/"
url2 = ".mp3"

#enter the episodes you want to download:
start = 475 #first episode we want to download
stop = 499 #last episode we want to download

#open the url with the given episode
def getIt(episode):
    request = urllib2.Request(url1 + str(episode) + url2)
    response = urllib2.urlopen(request)

    data = response.read() #grab the data

    mp3Name = str(episode) + ".mp3"
    song = open(mp3Name, "wb")
    song.write(data)
    song.close()

#display the percent complete, based on current, and the start and stop episode numbers from above
def percent(current):
    percent = 100 - ((float(stop) - current) / (stop - start)) * 100
    i = int(percent)
    if (i != 0 and i != 100):
        sys.stdout.write("\r%i percent complete" % i)
        print #flush it out
        sys.stdout.flush()

#loop through episodes, and run our functions
def main():
    print 'Downloading...'
    for episode in range(int(start), stop + 1):
        getIt(episode)
        percent(episode)
    print
    sys.stdout.write("Hooray!\n")

if __name__ == "__main__":
    main()