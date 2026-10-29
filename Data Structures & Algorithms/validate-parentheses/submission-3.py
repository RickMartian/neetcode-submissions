class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {'}': '{', ')': '(', ']': '['}
        open_brackets = []

        for b in s:
            if b in closeToOpen and open_brackets and open_brackets[-1] == closeToOpen[b]:
                open_brackets.pop()
            else:
                open_brackets.append(b)
        return len(open_brackets) == 0