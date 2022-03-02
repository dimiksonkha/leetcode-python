class Solution:
    """
    Kth Largest Element in an Array
    https://leetcode.com/problems/kth-largest-element-in-an-array/
    
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        max_nums = []
        while len(nums) > 0:
            max_num = nums[0]
            for num in nums:
                if num > max_num:
                    max_num = num
            
            max_nums.append(max_num)
            nums.remove(max_num)
    
                
        if len(max_nums) < k:
            return max_nums[0]
        else:
            return max_nums[k-1]