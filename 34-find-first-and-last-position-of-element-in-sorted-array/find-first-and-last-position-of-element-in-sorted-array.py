class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0 or target not in nums:
            return [-1,-1]
        else:
            return [nums.index(target),len(nums)-1-nums[::-1].index(target)]