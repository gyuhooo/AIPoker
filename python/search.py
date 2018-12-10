import distribute as db
import re

def search() :

    pattern = '.*?(\d+)'
    
    distr = str(db.player)
    
    repatter = re.sub("\W'|',|'|]", '', distr)
    result = re.findall(pattern, repatter)
    jorker = re.search('JORKER', repatter)
    
    if not(jorker) :
        hand = result
    else :
        hand = result + [str(jorker.group())]

    return hand
