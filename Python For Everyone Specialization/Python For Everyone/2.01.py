import re
file = ('tester.txt')
file = open(file)
count = 0
for line in file:
    line = re.findall('[0-9]+',line)
    for e in line:
        e = int(e)
        count = count + e
print(count)
