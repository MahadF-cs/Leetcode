class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        
        start_index = 0
        end_index = len(nums) - 1
        
        while nums[start_index] != target:
            start_index += 1
        
        while nums[end_index] != target:
            end_index -= 1
            
        return [start_index, end_index]
            
