class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    f=[i,j]
        return f