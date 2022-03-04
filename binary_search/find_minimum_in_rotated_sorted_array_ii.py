class Solution:
    """
    Find Minimum in Rotated Sorted Array II 
    https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
    
    """
    def findMin(self, nums: List[int]) -> int:
        
        index = 0
        while index+1 < len(nums):
            if nums[index] == nums[index+1]:
                del nums[index]
            else:
                index+=1
                
        n = len(nums)
        low = 0
        high = n-1
        if n==1 or nums[low] < nums[high]:
            return nums[low]
        
        mid = low + (high-low)//2
        high_value = nums[high]
        
        while low<=high:
            if nums[mid] > nums[mid +1]:
                return nums[mid+1]
            elif nums[mid] < high_value:
                high = mid-1
                mid = low + (high-low)//2
            else:
                low = mid+1
                mid = low + (high-low)//2
                   
                