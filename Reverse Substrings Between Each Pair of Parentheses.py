class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = []
        for i in range(n):
            if s[i] != ')':
                stack.append(s[i])
            else:
                temp = ''
                while stack and stack[-1] != '(':
                    cur = stack.pop()
                    temp += str(cur)
                stack.pop()
                for j in temp:
                    stack.append(j)
        return ''.join(stack)
