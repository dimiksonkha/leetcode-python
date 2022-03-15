class Solution:
    """
    Max Consecutive Ones
    https://leetcode.com/problems/max-consecutive-ones/
    
    """
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        max_count = 0
        count = 0
        for i in range(n):
            if nums[i] == 1:
                count+=1
            elif nums[i] == 0:
                if count > max_count:
                    max_count = count
                count = 0
                
        if count > max_count:
            max_count = count
        
        return max_count