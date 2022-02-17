class Solution:
    """
    Rotate Array
    https://leetcode.com/problems/rotate-array/
    
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k > n and n!=0:
            k = n + (k%n)
        
        first_index = 0
        mid_index = n-k
        last_index = n
        
        part1 = nums[first_index:mid_index]
        part2 = nums[mid_index:last_index]
        nums[:] = part2 + part1