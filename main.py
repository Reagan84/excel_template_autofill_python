# TODO:
# add flags --> allow user to make changes to config file
# turn prompt below into cmd line argument
# have user able to configure different json for template configs
# build a copy of an excel sheet via template config

import json
from openpyxl import Workbook, load_workbook
import urllib.request
import requests
# implement EDGAR API

# TODO: change how url functions
url = "https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json"
# Array of fake user-agent data to decieve bureaucrats
userAgentData = ["User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"]

# returns <Response [200]> if successfully decieved government idiots
repsoneStatus = requests.get(url, headers={userAgentData[0]: userAgentData[1]})
print(repsoneStatus)

# builds the request to government
req = urllib.request.Request(url)
req.add_header(userAgentData[0], userAgentData[1])

# opens request as a JSON to be parsed
with urllib.request.urlopen(req) as finDictRaw:
        finDict = json.load(finDictRaw)

# finDict is broken up into CIK, entity name, and facts
finFacts = finDict["facts"]
# contains: dei, invest, us-gaap, srt
finFUCK = finFacts["us-gaap"]
# us-gaap has items of interest
# within items of interest exists "label", "description", and "units"
# units contains USD (may change)
# USD contains the object of interest: start and end periods, form, year, quarter, file date, and value
#finOMG = finFUCK["GrossProfit"]
#finJesus = finOMG["units"]
#finIDK = finJesus["USD"]
for facts in finFUCK:
        print(facts)
