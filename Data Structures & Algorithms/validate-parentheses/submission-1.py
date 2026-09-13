class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in '[({':
                stack.append(p)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if p == ')':
                    if top != '(':
                        return False
                if p == ']':
                    if top != '[':
                        return False
                if p == '}':
                    if top != '{':
                        return False
        return len(stack) == 0        
