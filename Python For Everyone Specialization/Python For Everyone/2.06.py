# imports
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

# variables
print('')
url = input('Enter URL - ')
count = 0

# bpassing certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
print('bypassed certificate errors')


# opening the cnnection to the web and reading the data
uh = urllib.request.urlopen(url)
data = uh.read()
print('opened url')

# trying to load the data
try:
    js = json.loads(data)
    print('loading...')
except:
    print('loading...')
    print('###### ERROR ######')
    print(data)


x = 0
x = js['comments']
for item in x:
    count = count + int(item['count'])
print('')
print('')
print('Count:', count)
