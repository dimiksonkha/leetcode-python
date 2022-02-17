class Solution:
    """
    Search Insert Position
    https://leetcode.com/problems/search-insert-position/
    
    """
    
    def binary_search(self,sorted_list, item):
    
        n = len(sorted_list)
        left = 0
        right = n-1 

        mid = (left + right)//2
        item_index = 0

        while left <= right:

            if item == sorted_list[mid]:
                item_index = mid
                return item_index
            else:
                if item > sorted_list[mid]:
                    left = mid +1 
                    mid = (left + right)//2
                else:
                    right = mid -1
                    mid = (left + right)//2
        return mid+1

    def searchInsert(self, nums: List[int], target: int) -> int:
        index = self.binary_search(nums, target)
        return index