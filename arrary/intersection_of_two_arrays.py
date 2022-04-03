class Solution:
    """
    Intersection of Two Arrays
    https://leetcode.com/problems/intersection-of-two-arrays
    
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        nums2_dict = dict.fromkeys(nums2)
        hash_map = {}
        
        for i in range(n):
            if nums1[i] in nums2_dict:
                hash_map[nums1[i]] = None
        return hash_map 