from bs4 import BeautifulSoup
import requests
import csv

#request a page and store that in a variable
page_to_scrape = requests.get("http://quotes.toscrape.com/")
#parsing the html website and store it in a variable
soup = BeautifulSoup(page_to_scrape.text, "html.parser")


'''
# <span> tag is an inline container used to mark up a part of a text, or a part of a document.
# <small> tag defines smaller text (like copyright and other side-comments)
# "class" attribute is used to specify a class for an HTML element aka text and author
'''
#this code will go through all qoutes and authors in the website and save it as a list
quotes = soup.findAll("span", attrs = {"class":"text"})
authors = soup.findAll("small", attrs = {"class":"author"})

#variable that opens a csv file and another variable that writes to it
file = open("scraped_quotes.csv", "w")
writer = csv.writer(file)
#stuff to be written into it:
writer.writerow(["QUOTES", "AUTHORS"])


#iterates over all qoutes and authors in the website
#format needs to be qouts followed by author names by combining loops
for quotes, authors in zip(quotes, authors):
    print(quotes.text + " - " + authors.text)
    #allows to write a new row for each quote and author
    #writer.writerow([quotes.text, authors.text])
#break the loop and closes the csv file
file.close()