#Greetings to Domaintools
#Coded by Exploiter~Xed
#Team_CC
import re, urllib2
headers = { 'User-Agent' : 'Mozilla/5.0' }
fileopen = open('s.txt', 'r').readlines()
unique=[]
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
        if 'Reverse' in found[0]:
            continue
        print 'IP is:', found[0]
        unique.append(found[0])
    except:
        print 'Found error on', i
        pass
unique = list(set(unique))
for i in unique:
    open('IP_collected.txt', 'a+').write(i + '\n')
print 'All saved as IP_collected.txt'
