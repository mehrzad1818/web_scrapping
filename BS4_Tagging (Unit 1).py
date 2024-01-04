
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
