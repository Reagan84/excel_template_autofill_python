# TODO:
"""
- open template JSON file
- open excel file
- Save Value keys to an array
- Soupify HTML and chop it into its table parts by the row
OR
- Run imaging api to save values by the row
- save rows to a dict, first coloumn being the key and the remaining being the values
- make copy of excel template
- load dict to excel copy via pandas 
- save and close excel copy and excel template
"""

from bs4 import BeautifulSoup
import pandas as pd

def main():
    # apple 10q --> aapl-20250628
    fileToParsePath = "../appl.htm"
    fileToParsePathD = "/mnt/c/Users/Michi/Documents/codeSpace/appl.htm"

    # open the file
    fileToParse = open(fileToParsePathD)

    # print out contents thereof
    soup = (BeautifulSoup(fileToParse, "html.parser"))
    
    # put html Table rows in dicts
    treeRows = soup.find_all("tr")
    tableContents = {}
    tableHasher = []
    for treeRow in treeRows:
        treeRowStringsArr = list(treeRow.strings)
        if(len(treeRowStringsArr) > 0):
            tableHasher.append(treeRowStringsArr[0])
            tableContents[treeRowStringsArr[0]] = treeRowStringsArr[1:]

    
    # print out dicts
    for i in tableHasher: 
        print(tableContents[i])



main()