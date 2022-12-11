Filename = input('Enter a file you would like to open: ')
File = open(Filename)
x = ("")
y = 0
count = 0
for line in File:
    y = line.startswith('From:')
    if y == False:
        continue
    if y == True:
        line = line.rstrip()
        line = line.replace('From: ','')
        print(line)
        count = count + 1
x.split()
print('There were',count,'lines in the file with From as the first word')
