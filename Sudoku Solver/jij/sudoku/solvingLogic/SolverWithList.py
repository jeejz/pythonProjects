defAllPossibleValues = '123456789'

list = [defAllPossibleValues for i in range(100)]

for i in range(0,10):
    list[i] = None
for i in range(10,100,10):
    list[i] = None


for i in range(len(list)):
    print(i,"-",list[i],end='\t')
    if(i%10 == 0):
        print("")
