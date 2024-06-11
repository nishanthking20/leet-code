class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l=[]
        for i in arr2:
            l+=[i]*arr1.count(i)
        return l+sorted([i  for i in arr1 if i not in arr2])
        