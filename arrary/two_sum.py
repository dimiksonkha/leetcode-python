class Solution:
    """
    Two Sum
    https://leetcode.com/problems/two-sum/
    
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = {}
        for i in range(len(nums)):
            if target - nums[i] in results:
                return results[target-nums[i]],i
            else:
                results[nums[i]] = i