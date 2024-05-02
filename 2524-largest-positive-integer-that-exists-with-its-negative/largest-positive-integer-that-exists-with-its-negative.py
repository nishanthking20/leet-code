class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        while i<len(nums) and nums[i]<0:
            a=abs(nums[i])
            if a in nums:
                return a
            else:
                i+=1
        return -1