import distribute as db
import re

pattern = '.*?(\d+)'

distr = str(db.distribute)

repatter = re.sub("\W'|',|'|]", '', distr)
result = re.findall(pattern, repatter)
jorker = re.search('JORKER', repatter)
 
#for debug
#print(repatter)

if not(jorker) :
    hand = result
else :
    hand = result + [str(jorker.group())]

#for debug
#print(hand)
