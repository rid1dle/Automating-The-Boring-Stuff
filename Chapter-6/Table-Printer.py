tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


for j in range(len(tableData[0])):
    ar = []
    for i in range(len(tableData)):
        ar.append(tableData[i][j])
    print(' '.join(ar))
