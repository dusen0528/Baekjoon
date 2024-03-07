class Stack:
    def __init__(self): # 스택 초기화
        self.items = []
        
    def push(self, data): # 스택 데이터 삽입
        self.items.append(data)
        
    def pop(self): # 스택 맨 뒤 요소 리턴
        if(self.isSize()==0):
            return -1
        else:
            return self.items.pop()
    
    def isSize(self):
        return len(self.items)
        
    def isEmpty(self): # 스택 요소 검사
        if(self.isSize()==0):
            return 1
        else:
            return 0
    
    def peek(self):
        if(self.isSize()==0):
            return -1
        else:
            return self.items[-1]
    
stack = Stack()
        
loop = int(input())

for count in range(loop):
    operation = input().split()
    if(int(operation[0])==1): # push
        value = int(operation[1])
        stack.push(value)
    elif(int(operation[0])==2): # pop
        print(stack.pop())
    elif(int(operation[0])==3): # isSize
        print(stack.isSize())
    elif(int(operation[0])==4): # isEmpty
        print(stack.isEmpty())
    elif(int(operation[0])==5): # peek
        print(stack.peek())
        
        