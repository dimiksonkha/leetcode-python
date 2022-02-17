"""
Remove Duplicates from Sorted Array.
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        k = len(nums)
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                index+=1
                nums[index] = nums[i+1]
            else:
                k-=1              
        
        return k
