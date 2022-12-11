y = 0
z = 0
x = 0
text = "X-DSPAM-Confidence:    0.8475";
y = text.find(":")
y = y + 1
z = text.find("5")
z = z + 1
x = text[y:z]
x = x.lstrip()
float(x)
print(x)
