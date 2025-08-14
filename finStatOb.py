from bs4 import BeautifulSoup

# apple 10q
fileToParsePath = "appl.htm"

# open the file
fileToParse = open(fileToParsePath)

# print out contents thereof
print(BeautifulSoup(fileToParse, "html.parser"))
