class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a=nums.index(target) if target in nums else -1
        return a