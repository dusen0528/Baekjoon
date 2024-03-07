testCaseCount = int(input(''))


for i in range(testCaseCount):
    inputs = input().split()
    loopNum = int(inputs[0])
    word = inputs[1]
    for j in range(len(word)):
        for k in range(loopNum):
            print(word[j], end='')
    print('')
        
        
        
        