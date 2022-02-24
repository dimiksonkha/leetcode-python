class Solution:
    """
    Majority Element II
    https://leetcode.com/problems/majority-element-ii/
    
    """
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or (n == 2 and nums[0]!=nums[1]):
            return nums
        elif n == 2 and nums[0] == nums[1]:
            return [nums[0]]
            
        counting_nums = {}
        major_nums = []
        for i in range(n):
            if nums[i] in counting_nums:
                counting_nums[nums[i]]+=1
                if counting_nums[nums[i]] > n//3 and counting_nums[nums[i]] < (n//3)+2:
                    major_nums.append(nums[i])
            else:
                counting_nums[nums[i]]=1
    
        return major_nums 