# TODO:
# have program open, from a file path, excel
from openpyxl import Workbook, load_workbook

wb = Workbook()

fpath = "../../../Desktop/"

print("Provided me with a file")
fname = input()
ftotal = fpath + fname
xlTemplate = load_workbook(filename = ftotal)


ws1 = xlTemplate.create_sheet("Balance Sheet")
ws1['A4'] = "Balance Sheet"
xlTemplate.save(ftotal)

print("Operation Finished")