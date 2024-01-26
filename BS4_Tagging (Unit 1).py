
# %%

# Code written with beautifulsoup, html.parser
from urllib.request import urlopen
from bs4 import BeautifulSoup

# THis part of the code handles the links:
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

######################################################NEWLYADDEDCODES################################################

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

#There might be several issues with the  codes below:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random import re
random.seed(datetime.datetime.now()) def getLinks(articleUrl):
html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
bs = BeautifulSoup(html, 'html.parser')
return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')) 





from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages = set()
def getLinks(pageUrl):
global pages
html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
bs = BeautifulSoup(html, 'html.parser') for link in bs.find_all('a', href=re.compile('^(/wiki/)')): 
    if 'href' in link.attrs: if link.attrs['href'] not in pages:
#We have encountered a new page

newPage = link.attrs['href'] print(newPage) 
pages.add(newPage) 
getLinks(newPage)
getLinks('')






class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26

        for ch in word1:
            freq1[ord(ch) - ord('a')] += 1

        for ch in word2:
            freq2[ord(ch) - ord('a')] += 1

        for i in range(26):
            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
                return False

        freq1.sort()
        freq2.sort()

        for i in range(26):
            if freq1[i] != freq2[i]:
                return False

        return True



## Optimization



import requests
from bs4 import BeautifulSoup


def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

def scrape_html(url):
    html_content = get_html_content(url)
    if html_content:
        soup = BeautifulSoup(html_content, "lxml")
        return soup

def get_element_text(soup, tag):
    element = soup.find(tag)
    if element:
        return element.text.strip()
    else:
        return None


url = "http://www.pythonscraping.com/pages/page1.html"
soup = scrape_html(url)

if soup:
    print(get_element_text(soup, "h1"))
    print(get_element_text(soup, "h2"))
    print(get_element_text(soup, "h3"))



This has been updated




from urllib.request import urlopen
from bs4 import BeautifulSoup

the_html_link = urlopen("https://en.wikipedia.org/wiki/Informant")

bs4_object = BeautifulSoup(the_html_link.read(), "html.parser")

# Print the first h1 element
print(bs4_object.h1)

# Print all h1 elements
h1_elements = bs4_object.find_all("h1")
for h1 in h1_elements:
    print(h1)







from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

try:
    the_html_link = urlopen("http://www.pythonscraping.com/pages/page1.html")

    bs4_object = BeautifulSoup(the_html_link.read(), "html.parser")

    # Use the bs4_object for further processing
    # ...
    
except URLError as e:
    print("URL Error:", e)
except HTTPError as e:
    print("HTTP Error:", e)


# THis is the more advanced approach to this


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
try:
    print(bs.h1.get_text())
    print(bs.find(id ='mw-content-text').find_all('p')[0]) print(bs.find(id='ca-edit').find('span') .find('a').attrs['href'])
except AttributeError:
    print('This page is missing something! Continuing.')
for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
    if 'href' in link.attrs: 
        if link.attrs['href'] not in pages:
#We have encountered a new page
newPage = link.attrs['href']
print('-'*20)
print(newPage) pages.add(newPage) getLinks(newPage)
getLinks('')


# What is your idea about this part of the code?

allExtLinks = set() allIntLinks = set()
def getAllExternalLinks(siteUrl):
html = urlopen(siteUrl) domain = '{}://{}'.format(urlparse(siteUrl).scheme, urlparse(siteUrl).netloc) bs = BeautifulSoup(html, 'html.parser') internalLinks = getInternalLinks(bs, domain) externalLinks = getExternalLinks(bs, domain) for link in externalLinks: if link not in allExtLinks: allExtLinks.add(link)
print(link)
for link in internalLinks: if link not in allIntLinks: allIntLinks.add(link) getAllExternalLinks(link)
allIntLinks.add('http://oreilly.com') getAllExternalLinks('http://oreilly.com')
