class Solution:
    def isPalindrome(self, s: str) -> bool:
        # return (t := ''.join(c.lower() for c in s if c.isalnum())) == t[::-1]
        return (s := ''.join(filter(str.isalnum, s)).lower()) == s[::-1]
    
        