class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        c=[1]
        for i in range(rowIndex):
            d=[1]
            for j in range(1,i+1):
                d+=[c[j-1]+c[j]]
            d+=[1]
            c=d
        return c