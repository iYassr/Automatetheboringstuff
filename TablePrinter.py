tableData = [['apples', 'fdfsdoranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carolaaaa', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print(len(tableData))

def getMax(tableData):
    colWidth = []
    #colWdith = [0] * len(tableData) #to reserve it
    max = 0
    #get the max string value
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if len(tableData[i][j]) > max:
                max = len(tableData[i][j])
        colWidth.append(max)
        #max = 0

    print(colWidth)
    return colWidth


def printTable(tableDate):
    counter = 0
    colWidth = getMax(tableData)
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if j % 4 == 0:
                print()
            print(tableData[i][j].rjust(colWidth[i]),end=' ')
            counter+=1





printTable(tableData)
