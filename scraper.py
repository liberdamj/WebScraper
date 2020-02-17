import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/p/pl?Submit=StoreIM&Depa=1&Category=38"

# Opening up connection and grabbing page.
uClient = uReq(my_url)
# Saving HTML into page_html.
page_html = uClient.read()
# Closing connection that grabbed page.
uClient.close()

# Parses HTML with BeautifulSoup
page_soup = soup(page_html, "html.parser")

# Grabs each div with the class item-container
containers = page_soup.findAll("div", {"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "product_name, shipping\n"

f.write(headers)


for container in containers:

    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    f.write(product_name.replace(",", "|") + " , " + shipping + "\n")

f.close()
