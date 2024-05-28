class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        k=0
        if x>=0:
            k=int(s[::-1])
        else:
            s=s[0]+s[1:][::-1]
            k= int(s)
        if k>-2**31 and k<2**31-1:
            return k
        else:
            return 0