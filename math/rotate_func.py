class Solution:
    """
    Rotate Function
    https://leetcode.com/problems/rotate-function/
    """
          
    def maxRotateFunction(self, nums: List[int]) -> int:
        f=0
        all_sum = nums[0]
        n = len(nums)
        for i in range(1,n):
            f+=i*nums[i]
            all_sum+=nums[i]
        
        max_f = f
        for i in range(n-1,0,-1):
            f = f + all_sum- (n*nums[i])
            if f > max_f:
                max_f = f       
            
        return max_f
        