x = list()
y = 0
e = 0
wer = list()
times = list()
histogram = dict()
keylist = list()
valuelist = list()
name = input("Enter file:")

if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

for line in handle:
    line.rstrip()

    if line.startswith('From'):
        x = line.split()
        e = x[5:6]

        for wer in e:
            wer = wer[0:2]

            if wer in histogram:
                histogram[wer] = histogram[wer] + 1

            else:
                histogram[wer] = 1

for k,v in histogram.items():
    print(k,v)
