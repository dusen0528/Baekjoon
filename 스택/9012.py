class Stack():
    def __init__(self):
        self.stack = []
    
    def sizeof(self):
        return len(self.stack)
    def isEmpty(self):
        return len(self.stack)==0
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None
       

count = int(input(''))


for _ in range(count):
    VPS = input('')
    stack = Stack()

    for i in VPS:
        if i == '(':
            stack.push(i)
        elif i ==')':
            if stack.isEmpty():
                stack.push(i)
                break
            else:
                stack.pop()
        
    if stack.isEmpty():
        print("YES")
    else:
        print("NO")