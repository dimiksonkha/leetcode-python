class Solution:
    """
    Find Peak Element
    https://leetcode.com/problems/find-peak-element/
    
    """
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        elif n == 2:
            if nums[0] > nums[1]:
                    return 0
            else:
                    return 1
                
        low = 0
        high = n-1
        mid = low+(high-low)//2
       
        while low<=high:
            if ((mid > 0 and nums[mid] > nums[mid-1]) and (mid < n-1  and nums[mid] > nums[mid+1])) or (mid == n-1 and nums[mid] > nums[mid-1]) or (mid==0 and nums[mid] > nums[mid+1]):   
                return mid
            elif nums[mid] < nums[mid-1]:
                    high = mid-1
                    mid = low + (high-low)//2
            else :
                low = mid+1
                mid = low +(high-low)//2