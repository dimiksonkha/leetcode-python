class Solution:
    """
    Find All Duplicates in an Array
    https://leetcode.com/problems/find-all-duplicates-in-an-array/
    
    """
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_dict = {}
        duplecate_nums = []
        for num in nums:
            if num in nums_dict:
                duplecate_nums.append(num)
            else:
                nums_dict[num] = 0
                
        return duplecate_nums 