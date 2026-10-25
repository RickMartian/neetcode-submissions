class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([l for l in s.replace(' ', '') if l.isalnum()]).lower()
        return s == s[::-1]