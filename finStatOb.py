# TODO:
# intake an html file defined as fileToParsePath
# parse through file to find financial information
# save this information to an object

from bs4 import BeautifulSoup
import csv

def main():
    # apple 10q --> aapl-20250628
    fileToParsePath = "../appl.htm"

    # open the file
    fileToParse = open(fileToParsePath)

    # print out contents thereof
    soup = (BeautifulSoup(fileToParse, "html.parser"))
    
    tableTitle = soup.find_all(style = "margin-top:9pt;text-align:center")
    for titles in tableTitle:
        titleTable = titles.next_sibling.next_sibling.next_sibling
        finSheet = titleTable.find("table")
        if finSheet != None:
            print(titles.string)
            finRow = finSheet.find_all("tr")
            for stringRow in finRow:
                stringTemp = ""
                for strrow in stringRow.stripped_strings:
                    stringTemp +=  (strrow + ", ")
                print(stringTemp[:-2])
            






main()