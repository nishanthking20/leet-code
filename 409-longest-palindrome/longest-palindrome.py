class Solution:
    def longestPalindrome(self, s: str) -> int:
        a=set()
        c=0
        for i in s:
            if i in a:
                a.remove(i)
                c += 2
            else:
                a.add(i)
        if a:
            c += 1
        return c