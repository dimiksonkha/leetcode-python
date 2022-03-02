class Solution:
    """
    Third Maximum Number
    https://leetcode.com/problems/third-maximum-number/
    
    """
    def thirdMax(self, nums: List[int]) -> int:
        
        max_nums = []
        while len(nums) > 0:
            max_num = nums[0]
            for num in nums:
                if num > max_num:
                    max_num = num
            
            max_nums.append(max_num)
            nums.remove(max_num)
    
        index = 0
        while index+1 < len(max_nums):
            if max_nums[index] == max_nums[index+1]:
                max_nums.remove(max_nums[index])
            else:
                index+=1
                
        if len(max_nums) < 3:
            return max_nums[0]
        else:
            return max_nums[2]