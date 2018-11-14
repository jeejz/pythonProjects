def generateGroupKeysForKey(key):
    grpKeyList = []
    for i in [1,4,7]:
        if i <= int(key[0]) < i+3 :
            cKeyX = int((i + i + 2)/2)
        if i <= int(key[1]) < i+3 :
            cKeyY = int((i + i + 2)/2)

    for k in [cKeyX-1, cKeyX, cKeyX+1]:
        for l in [cKeyY - 1, cKeyY, cKeyY + 1]:
            grpKeyList.append(str(k)+str(l))

    return grpKeyList

def generateColKeysForKey(key):
    colGrpKeysList = []
    for i in range(1, 10):
        colGrpKeysList.append(key[0]+str(i))
    return colGrpKeysList

def generateRowKeysForKey(key):
    rowGrpKeysList = []
    for i in range(1,10):
        rowGrpKeysList.append(str(i)+key[1])
    return rowGrpKeysList

key = '24'
print(generateGroupKeysForKey(key))
print(generateColKeysForKey(key))
print(generateRowKeysForKey(key))

defaultAvailableValues = [[[1,2,3,4,5,6,7,8,9]]]

print (defaultAvailableValues)