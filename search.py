import distribute as db
import re

pattern = '.*?(\d+)|JO+'

distr = str(db.distribute)

repatter = re.sub("r|\W0|,|',|'|]", '', distr)
result = re.findall(pattern, repatter)
jorker = re.search('JORKER', repatter)
 
#デバッグ用
#print(repatter)

if not(jorker) :
    hand = result
else :
    hand = result + [str(jorker.group())]

#デバッグ用
#print(hand)
