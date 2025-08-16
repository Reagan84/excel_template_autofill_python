# Excel Template Autofill in Python (ETAP)

## Functionality:

### Create Template
- Save file address, input keys, input values, bundled keys to JSON file, and
- naming conventions
(bundled keys are multiple inputs dicts combined into one dict)

### Load Excel
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

### Get HTML (implement upon completion)
- have user upload a pdf (prob just have it link in the main cmd)
- have user grab it via the EDGAR api

### CMD usage
\>$etap <br>
\>usage: ...

\>$etap addTemplate <br>
\>excel template path: <C://absolute path> # validate that a real excel file exsists here else return error<br>
\>cell key values: <a1:a11>, <a13:19>, <c1:c10> # defines where program will look to find keys for dict value <br>
\>cell input values: <b2:b11>, <b13:b19>, <c1:c10> # defines where program will put input values, all key values must have input values, possession determined by order <br>
\>inputBundleDef: <"short term debt", "treasury bills" "Line of credit", > # key is first, then values, tells program to look for keys and add its values together to get new key value pair <br>
\>add another?: (y/n) <br>
\>Operation Successful

\>$etap makeSheet \<input> \<template> # takes in HTML file (in future edgar api cmds) and uses the template <br>
\>Operation Successful


