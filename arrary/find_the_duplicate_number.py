class Solution:
    """
    Find the Duplicate Number
    https://leetcode.com/problems/find-the-duplicate-number/
    """
    def findDuplicate(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                return num
            else:
                nums_dict[num] = 0