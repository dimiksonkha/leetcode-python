class Solution:
    """
    Missing Number
    https://leetcode.com/problems/missing-number/
    
    """
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        my_dict = {nums[i]:i for i in range(n)}
        
        for i in range(n):
            if i not in my_dict:
                return i
        return n    