class Solution:
    """
    Contains Duplicate
    https://leetcode.com/problems/contains-duplicate/
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                return True
            else:
                nums_dict[num] = 0
        return False