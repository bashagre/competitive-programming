from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        
        
        mem=Stack()
        
        if len(s)%2 != 0:
            return False


        for i in range(len(s)):
            if s[i] == "{":
                mem.push("{")
            elif s[i] == "}":
                if mem.pop() != "{":
                    return False
                   

            elif s[i] == "[":
                mem.push("[")
            elif s[i] == "]":
                if mem.pop() != "[":
                    return False
                    

            elif s[i] == "(":
                mem.push("(")
            elif s[i] == ")":
                if mem.pop() != "(":
                    return False
                    

        if mem.size() != 0:
            return False
        else:
            return True
        
        
        
class Stack:
    def __init__(self):
        self.buffer=deque()
        
    def push(self,val):
        self.buffer.append(val)
        
    def isempty(self):
        if len(self.buffer)==0:
            return True
        else:
            return False
    
    def pop(self):
        if len(self.buffer)==0:
            return 
        else:
            return self.buffer.pop()
    def size(self):
        return len(self.buffer)
