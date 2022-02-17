class Solution:
    """
    Find All Numbers Disappeared in an Array
    https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
    
    """
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        my_dict = {nums[i]:i for i in range(n)}
        missing_list = []
        
        for i in range(1,n+1):
            if i not in my_dict:
                missing_list.append(i) 
        return missing_list