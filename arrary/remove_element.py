"""
Remove Element
https://leetcode.com/problems/remove-element/

"""
class Solution:
    def removeElement(self, nums, val: int) -> int:
        index = 0
        k = 0
        n = len(nums)

        while index + k < n:
            if nums[index]==val:
                nums.pop(index)
                index-=1
                k+=1
            index+=1
            
        return n-k
