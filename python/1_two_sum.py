class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_hash = {}
        for i in range(0, len(nums)):
            if target - nums[i] in index_hash.keys():
                return [i, index_hash[target-nums[i]]]
            index_hash[nums[i]] = i