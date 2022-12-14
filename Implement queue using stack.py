class MyQueue:

    def __init__(self):
        
        self.stack1 = []
        

    def push(self, x: int) -> None:
        stack2 = []
       
        while self.stack1:
            stack2.append(self.stack1.pop())
        
        self.stack1.append(x)
        
        while stack2:
            self.stack1.append(stack2.pop())
        

    def pop(self) -> int:
         
        return self.stack1.pop()
        

    def peek(self) -> int:
        
        return self.stack1[-1]
        

    def empty(self) -> bool:
        return len(self.stack1) == 0
