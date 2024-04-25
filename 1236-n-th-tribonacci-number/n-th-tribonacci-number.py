class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        l=[0,1,1]
        while len(l)<=n:
            l+=[l[-1]+l[-2]+l[-3]]
        return l[-1]