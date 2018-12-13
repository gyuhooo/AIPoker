import distribute as db
import re

def search(dist) :

    pattern = '.*?(\d+)'
    
    distr = str(dist)
    
    repatter = re.sub("\W'|',|'|]", '', distr)
    result = re.findall(pattern, repatter)
    jorker = re.search('JORKER', repatter)
    
    if not(jorker) :
        hand = result
    else :
        hand = result + [str(jorker.group())]
    return hand
