class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "[{(":
                stack.append(c)
            elif c in ")}]":
                p = stack.pop() if stack else ""
                if (p=='(' and c ==')') or (p=='{' and c =='}') or (p=='[' and c ==']'):
                    continue
                else:
                    return False
        if not stack:
            return True
        else:
            return False