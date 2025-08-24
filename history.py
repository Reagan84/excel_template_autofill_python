
   
"""






soupyDivs = soup.find_all("div") 
postTOC = False
kill = False
search = False
tableNames = ["STATEMENTS OF OPERATIONS", "STATEMENTS OF COMPREHENSIVE", "BALANCE SHEETS", "STATEMENTS OF SHAREHOLDERS’ EQUITY", "STATEMENT OF CASH FLOWS"]
for divToSearch in soupyDivs:
    ldivTosearch = [s.lower() for s in divToSearch.strings]
    if "table of contents" in ldivTosearch:
        postTOC = True
    if postTOC:
        for searchDiv in ldivTosearch:
            if searchDiv.find("item 2") != -1 and search:
                kill = True
        if kill:
            print("IM CUMMING")
            break
        for stringOfDiv in ldivTosearch:
            stringOfDiv = stringOfDiv.upper()
            for name in tableNames:
                if stringOfDiv.find(name) != -1:
                    search = True
                    print("Im going to bust")
    
"""