# TODO:
# add flags --> allow user to make changes to config file
# turn prompt below into cmd line argument
# have user able to configure different json for template configs
# build a copy of an excel sheet via template config

import json
from openpyxl import Workbook, load_workbook

# path set by user that directs program to excel file location
userPath = "routeToExcelDirectory"

# add error catching? -- loads config file for use
with open('config.json', 'r') as configFile:
    configData = json.load(configFile)

fpath = configData[userPath]

# test (not permanant) -- needs error catching
print("Provided me with a file")
fname = input()
ftotal = fpath + fname
xlTemplate = load_workbook(filename = ftotal)

# test --> to be changed
ws1 = xlTemplate.create_sheet("Balance Sheet")
ws1['A4'] = "Balance Sheet"
xlTemplate.save(ftotal)

# finising message
print("Operation Finished")