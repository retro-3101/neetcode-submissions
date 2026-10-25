class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        brackets = {'(': ')', '{': '}', '[': ']'}

        for ch in s:
            if ch in brackets.keys():
                stack.append(ch)
            
            elif ch in brackets.values():
                if len(stack) == 0 or brackets[stack[-1]] != ch:
                    return False
                else:
                    stack.pop()

        if len(stack) == 0:
            return True

        return False 