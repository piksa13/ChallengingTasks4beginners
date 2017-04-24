import re
emailAddress = input()
pat2 = "(\w+)@(\w+\.)+(com)"
#pat2 = "(\w+)@(\w+)+(.com)"
r2 = re.match(pat2,emailAddress)

print('here is the whole match:', r2.group())

print('Here is the first part ' + r2.group(1))
print('Here is the second part '+ r2.group(2))
print('Here is the last part '  + r2.group(3))