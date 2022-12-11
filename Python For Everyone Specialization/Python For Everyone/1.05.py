x = 0
values = 0
number = 0
z = None
largest = 0
word = None

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)
histogram = dict()
for line in handle:
    if line.startswith('From:'):
        wds = line.split()
        x = wds[1]
        if x in histogram:
            histogram[x] = histogram [x] + 1
        else:
            histogram[x] = 1

for k,v in histogram.items():
    if v > largest:
        largest = v
        word = k
print(word,largest)
