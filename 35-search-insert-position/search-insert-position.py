class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        c=0
        for i in range(len(nums)):
            if nums[i]==target:
                c=i
            elif target<nums[i] and target>nums[i-1]:
                c=i
            elif target>nums[i]:
                c=i+1
        return c