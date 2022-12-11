# Use the file name mbox-short.txt as the file name
total = 0
count = 0
avarage = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.strip('X-DSPAM-Confidence:')
    line = line.rstrip()
    total = total + float(line)
    count = count + 1
avarage = total / count
print('Average spam confidence:',avarage)
