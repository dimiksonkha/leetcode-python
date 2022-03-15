class Solution:
    """
    Summary Ranges
    https://leetcode.com/problems/summary-ranges/
    
    """
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums.append(None)
        n = len(nums)
        range_list = []
        a = nums[0]
        b = None
        for i in range(n-1):   
            if nums[i]+1 != nums[i+1]:
                b = nums[i]
                if a == b:
                    range_list.append(str(a))
                else:
                    range_list.append(str(a)+'->'+str(b))
                a = nums[i+1]
            elif i+1 == n-1:
                b=nums[i+1]
                if a == b:
                    range_list.append(str(a))
                else:
                    range_list.append(str(a)+'->'+str(b))
        return range_list