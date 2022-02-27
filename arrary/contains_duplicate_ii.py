class Solution:
    """
    Contains Duplicate II
    https://leetcode.com/problems/contains-duplicate-ii/
    
    """
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        nums_dict = {}
        for i in range(n):
            if nums[i] in nums_dict:
                temp = i - nums_dict[nums[i]]
                if temp <=k:
                    return True
                else:
                    nums_dict[nums[i]] = i 
            else:
                nums_dict[nums[i]] = i
                
        return False