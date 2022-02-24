class Solution:
    """
    Majority Element
    https://leetcode.com/problems/majority-element/
    
    """
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
            
        counting_nums = {}
        for i in range(n):
            if nums[i] in counting_nums:
                counting_nums[nums[i]]+=1
                if counting_nums[nums[i]] > n/2:
                    return nums[i]
            else:
                counting_nums[nums[i]]=1