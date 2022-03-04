class Solution:
    """
    Find Minimum in Rotated Sorted Array
    https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
    
    """
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1
        if n==1 or nums[low] < nums[high]:
            return nums[low]
        
        mid = low + (high-low)//2
        high_value = nums[high]
        
        if nums[low] < nums[high]:
            return nums[low]
        
        while low<=high:
            if nums[mid] > nums[mid +1]:
                return nums[mid+1]
            elif nums[mid] < high_value:
                high = mid-1
                mid = low + (high-low)//2
            else:
                low = mid+1
                mid = low + (high-low)//2
                   
                