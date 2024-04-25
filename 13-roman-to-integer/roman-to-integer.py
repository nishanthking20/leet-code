class Solution:
    def romanToInt(self, s: str) -> int:
        l={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        k=0
        for i in range(len(s)):
            if i<len(s)-1 and l[s[i]]<l[s[i+1]]:
                k-=l[s[i]]
            else:
                k+=l[s[i]]
        return k