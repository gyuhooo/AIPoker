import distribute as db
import re

pattern = '.*?(\d+)|JO+'

distr = str(db.distribute)

repatter = re.sub("\W0|,|',|'|r|]", '', distr)
result = re.findall(pattern, repatter)
jorker = re.search('JORKER', repatter)

if jorker :
    print(repatter)
    print(result)
    print(jorker.group())
else :
    print(repatter)
    print(result)

