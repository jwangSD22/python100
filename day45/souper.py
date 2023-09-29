from bs4 import BeautifulSoup

with open('sf_scrape.html','r',encoding='utf-8') as f:
    contents = f.read()
    print(contents)
    # soup = BeautifulSoup(contents,'html.parser')
    # print(soup.prettify())