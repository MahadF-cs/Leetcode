class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        full = range(0, max(nums) + 2)
        return min(list(set(full).difference(set(nums))))
