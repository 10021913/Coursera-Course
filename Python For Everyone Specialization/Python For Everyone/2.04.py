from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

URL = input("Enter the URL:") #Enter main URL
link_line = int(input("Enter position:")) - 1 #The position of link relative to first link
count = int(input("Enter count:")) #The number of times to be repeated

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while count >= 0:
    html = urlopen(URL, context=ctx).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    print (URL)
    URL = tags[link_line].get("href", None)
    count = count - 1
