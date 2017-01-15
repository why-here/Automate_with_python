#！ python3
#printTable.py - Print given table list with rjust() method.

tableData = [['apple', 'oranges', 'cherries' ,'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidths = [0]*(len(tableData))
for i in range(len(colWidths)):
    colWidths[i] = max(map(len, tableData[i]))
for i in range(len(tableData[0])):
    strPrint = ''
    for j in range(len(tableData)):
        strPrint = strPrint + tableData[j][i].rjust(colWidths[j]) + ' '
    print(strPrint)