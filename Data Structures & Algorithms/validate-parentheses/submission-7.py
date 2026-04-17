class Solution:
    def isValid(self, s: str) -> bool:
        maps = {'}' : '{', ']' : '[', ')' : '('}
        stack = []

        for c in s:
            if c not in maps:
                stack.append(c)
                continue
            if not stack or stack[-1] != maps[c]:
                return False
            stack.pop()
        return not stack