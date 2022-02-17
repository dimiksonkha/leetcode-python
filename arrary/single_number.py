class Solution:
    """
    Single Number
    https://leetcode.com/problems/single-number/
    """
    def singleNumber(self, nums: List[int]) -> int:
        my_dict = {i:nums[i] for i in range(0, len(nums))}
        for i in range(len(nums)):
            temp_value = my_dict[i] 
            my_dict[i] = None
            if temp_value not in my_dict.values():
                return temp_value
            my_dict[i] = temp_value 