class Solution:
    """
    Binary Search
    https://leetcode.com/problems/binary-search/
    """
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1 

        mid = (left + right)//2
        item_index = 0

        while left <= right:

            if target == nums[mid]:
                item_index = mid
                return item_index
            else:
                if target > nums[mid]:
                    left = mid +1 
                    mid = (left + right)//2
                else:
                    right = mid -1
                    mid = (left + right)//2
        return -1