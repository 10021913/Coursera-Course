hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)

if h > 40:
    firstnumber = 40 * r
    h = h-40
    h = h * r * 1.5
    h = h + firstnumber
else:
    h = h * r
print (h)
