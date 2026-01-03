# importing modules
import urllib.request 
from bs4 import BeautifulSoup

# providing url
# url = "https://www.geeksforgeeks.org/python/how-to-automate-an-excel-sheet-in-python/"

# # opening the url for reading
# html = urllib.request.urlopen(url)
# print(html)

# # parsing the html file
# htmlParse = BeautifulSoup("linkedin.html", 'html.parser')
filee = open("linkedin.html", mode="rt")

print(filee.read())
# getting all the paragraphs
# for para in htmlParse.find_all("p"):
#     print(para.get_text())