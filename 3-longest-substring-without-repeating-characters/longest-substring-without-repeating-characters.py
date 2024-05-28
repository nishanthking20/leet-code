class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x=0
        i=0
        c=0
        k=len(s)
        while i<k:
            g=''
            while i<k and s[i] not in g:
                g+=s[i]
                i+=1
            if len(g)>x:
                x=len(g)
            if i<k:
                i=s.index(s[i],i-len(g),k)+1
        return x
