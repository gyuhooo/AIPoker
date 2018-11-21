import distribute as db
import re

pattern = '.*'

distr = str(db.distribute)

repatter = re.sub(".0|,|'|]", '', distr)

print(repatter)

