class Solution:
    """
    Move Zeroes
    https://leetcode.com/problems/move-zeroes/
    
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
       
        count=0
        for num in nums:
            if num == 0:
                count+=1
       
        index = 0
        while index < len(nums):
            if nums[index] == 0:
                nums.remove(0)
            else:
                index+=1
                
        for i in range(count):
            nums.append(0)