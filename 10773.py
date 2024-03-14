class Stack:
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        return len(self.stack) == 0 
        
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop() 
        return None
        
K = int(input())

numStack = Stack()

for _ in range(K):
    num = int(input())
    if(num==0): numStack.pop()
    else: numStack.push(num)

result = sum(numStack.stack)
print(result)