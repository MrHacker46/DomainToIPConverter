#Greetings to Domaintools
#Coded by Exploiter~Xed
#Team_CC
import re, urllib2
headers = { 'User-Agent' : 'Mozilla/5.0' }
filename = raw_input('Type the domain list filename: \n')
fileopen = open(filename, 'r').readlines()
for i in fileopen:
    try:
        i = i.replace('\n','')
        if 'http://' in i:
            i = i.replace('http://', '')
        print 'Working on,', i
        req = urllib2.Request('http://reverseip.domaintools.com/search/?q=' + i, None, headers)
        html = urllib2.urlopen(req).read()
        found = re.findall('<title>.[\w]+.[\w]+.[\w]+.[\w]+',html)
        found[0] = found[0].replace('<title>','')
        print 'IP is:', found[0]
        open('IP_collected.txt', 'a+').write(found[0] + '\n')
    except:
        print 'Found error on', i
        pass
print 'All saved as IP_collected.txt'
