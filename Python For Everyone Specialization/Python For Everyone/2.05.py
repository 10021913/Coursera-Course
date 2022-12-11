# imports
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# variables
url = input('Enter URL - ')
count = 0

# bpassing certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# opening the cnnection to the web and reading the data
uh = urllib.request.urlopen(url)
data = uh.read()

# getting the data we want
lst = tree.findall('comments/name/count')
counts = tree.findall('.//count')

# counting up the data
for each in counts:
    x = each.text
    count = count + int(x)
print(count)
