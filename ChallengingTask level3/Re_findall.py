s = input()
#l = [ i for i in s if i.isdigit()]
#print(l)

import re
print(re.findall("\d+",s))
print(re.findall("\w+",s))
