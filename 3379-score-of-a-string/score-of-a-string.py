class Solution:
    def scoreOfString(self, s: str) -> int:
        x=0
        for i in range(1,len(s)):
            x+=abs(ord(s[i-1])-ord(s[i]))
        return x
        