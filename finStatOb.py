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
    tRows = soup.find_all("tr")
    for row in tRows:
        aRow = row.strings
        lRow = list(aRow)
        rowDict = {}
        keyInput = 0
        # think this through
        for i in range(0, len(lRow)):
            if i == 0:
                keyInput = lRow[i]
            else:
                rowDict = {keyInput: lRow[i]}
        if len(lRow) > 1:
            print(rowDict[keyInput])

        for i in rowDict:
            print("key: " + i)
            
    # print out dicts




main()