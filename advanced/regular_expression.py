import re

a = "www.123.www"
b = re.match("www", a, re.I)
print(b.group(0, 1))
print(b.groups())
