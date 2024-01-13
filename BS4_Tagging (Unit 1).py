
# %%

# Code written with beautifulsoup, html.parser
from urllib.request import urlopen
from bs4 import BeautifulSoup


the_html_link = urlopen("https://en.wikipedia.org/wiki/Informant")

bs4_object = BeautifulSoup(the_html_link.read(), "html.parser")
bs = BeautifulSoup(the_html_link, "html.parser")

print(bs4_object.h1)
print(bs4_object.h1)
print(bs4_object.html.body.h1)
print(bs4_object.html.h1)

# %%
# The same code as above, but with lxml parser
from urllib.request import urlopen
from bs4 import BeautifulSoup


the_html_link = urlopen("http://www.pythonscraping.com/pages/page1.html")

bs4_object = BeautifulSoup(the_html_link.read(), "lxml")
bs = BeautifulSoup(the_html_link, "lxml")

print(bs4_object.h1)
print(bs4_object.h1)
print(bs4_object.html.body.h1)
print(bs4_object.html.h1)


# %%
# The same code as above, but with html5lib
from urllib.request import urlopen
from bs4 import BeautifulSoup


the_html_link = urlopen("http://www.pythonscraping.com/pages/page1.html")

bs4_object = BeautifulSoup(the_html_link.read(), "html5lib")
bs = BeautifulSoup(the_html_link, "html5lib")

print(bs4_object.h1)
print(bs4_object.h1)
print(bs4_object.html.body.h1)
print(bs4_object.html.h1)

# %%

# Handling errors with try/except/else ...

from urllib.request import urlopen
from urllib.error import HTTPError

try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
# return null, break, or do some other "Plan B"
else:
    pass
# program continues.
# Note: If you return or break in the # exception catch, you do not need to use the "else" statement
# %%


from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError


# %%


from urllib.request import urlopen
from urllib.error import URLError
from urllib.error import HTTPError



try:
    the_html_link = urlopen("http://www.pythonscraping.com/pages/page1.html")

    bs4_object = BeautifulSoup(the_html_link.read(), "html.parser")
    bs = BeautifulSoup(the_html_link, "html.parser")




#%%

import scrapy

class HeadlinesSpider(scrapy.Spider):
    name = 'headlines'
    start_urls = ['http://example.com']

    def parse(self, response):
        # Extract headlines here
        pass
# %%
# %%
from urllib.request import urlopen
from bs4 import BeautifulSoup

# It is to handle the link:
html_link = urlopen("http://www.pythonscraping.com/pages/page1.html")

# It is to create a BS4 object:
bs4 = BeautifulSoup(html_link.read(), "html.parser")


nameList = bs4.findAll("span", {"class": "green"})
for name in nameList:
    print(name.get_text())
# %%


from urllib.request import urlopen
from bs4 import BeautifulSoup


my_link = urlopen("http://www.pythonscraping.com/pages/page3.html")

bs4_2 = BeautifulSoup(my_link, "html.parser")

for child in bs4_2.find("table", {"id": "giftList"}).children:
    print(child)
# %%
from urllib.request import urlopen
from bs4 import BeautifulSoup


my_link = urlopen("https://www.mehrnews.com/")

bs4_2 = BeautifulSoup(my_link, "html.parser")

for child in bs4_2.div.h3.find("a").children:
    print(child)

# %%

from urllib.request import urlopen
from bs4 import BeautifulSoup

link2 = urlopen("https://www.mehrnews.com/")
bs44 = BeautifulSoup(link2, "html.parser")


print(bs44)





# %%

# Some important points on regular expressions:

# https://www.regexpal.com/
# %%

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html, "html.parser")

images = bs.find_all("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})

for image in images:
    print(image["src"])

bs.find_all(lambda tag: len(tag.attrs) == 2)
# %%


bs.find_all(lambda tag: tag.get_text() == "Or maybe he's only resting?")

bs.find_all("", text="Or maybe he's only resting?")

# %%

from urllib.request import urlopen

import urllib.request
from bs4 import BeautifulSoup


try:
    url = "https://en.wikipedia.org/wiki/Informant"
    response = urllib.request.urlopen(url)
    html = response.read()

    bs4_object = BeautifulSoup(html, "html.parser")

    # Find the first h1 tag in the HTML
    h1_tag = bs4_object.find("h1")

    if h1_tag:
        print("First h1 tag found: ", h1_tag.text)
    else:
        print("No h1 tag found")

except urllib.error.HTTPError as e:
    print("HTTP Error:", e.code, "-", e.reason)
except urllib.error.URLError as e:
    print("URL Error:", e.reason)
except Exception as e:
    print("An error occurred:", str(e))



print(bs4_object.html.body.h1)
print(bs4_object.html.h1)

the_html_link = urlopen("https://en.wikipedia.org/wiki/Informant")

bs4_object = BeautifulSoup(the_html_link.read(), "html.parser")
bs = BeautifulSoup(the_html_link, "html.parser")



# %%

# Code written with beautifulsoup, html.parser
from urllib.request import urlopen
from bs4 import BeautifulSoup


the_html_link = urlopen("https://en.wikipedia.org/wiki/Informant")

bs4_object = BeautifulSoup(the_html_link.read(), "html.parser")
bs = BeautifulSoup(the_html_link, "html.parser")

print(bs4_object.h1)
print(bs4_object.h1)
print(bs4_object.html.body.h1)
print(bs4_object.html.h1)

# %%
# The same code as above, but with lxml parser
from urllib.request import urlopen
from bs4 import BeautifulSoup


the_html_link = urlopen("http://www.pythonscraping.com/pages/page1.html")

bs4_object = BeautifulSoup(the_html_link.read(), "lxml")
bs = BeautifulSoup(the_html_link, "lxml")

print(bs4_object.h1)
print(bs4_object.h1)
print(bs4_object.html.body.h1)
print(bs4_object.html.h1)


# %%
# The same code as above, but with html5lib
from urllib.request import urlopen
from bs4 import BeautifulSoup



from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find('div', {'id':'bodyContent'}).find_all( 'a', href=re.compile('^(/wiki/)((?!:).)*$')):
if 'href' in link.attrs: print(link.attrs['href'])



from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random import re
random.seed(datetime.datetime.now()) def getLinks(articleUrl):
html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
bs = BeautifulSoup(html, 'html.parser')
return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')) 
