class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_arr = [1]
        right_arr  = [1]
        for i in range(len(nums)-1):
            left_arr.append(left_arr[i] * nums[i])
            right_arr.insert(0, right_arr[0] * nums[len(nums)-i-1])
        
        result = []
        for i in range(len(nums)):
            result.append(left_arr[i] * right_arr[i])
        return result
