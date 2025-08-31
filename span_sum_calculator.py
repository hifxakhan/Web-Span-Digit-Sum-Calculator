import urllib.request, ssl
from bs4 import BeautifulSoup

# ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url: ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

total = 0
for span in soup.find_all('span'):
    txt = span.get_text(strip=True)
    if txt.isdigit():          # ensure it's purely digits
        total += int(txt)

print(total)
