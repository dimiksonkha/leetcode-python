class Solution:
    """
    Product of Array Except Self
    https://leetcode.com/problems/product-of-array-except-self/
    
    """
    def product_all_nums(self, nums):
        prod = 1
        zero_count = 0
        for i in range(len(nums)):
            if i==0:
                zero_count+=1
            prod*=nums[i]
        return prod, zero_count        
    
    def product_except_index(self, nums, index):
        prod = 1
        for i in range(len(nums)):
            if i!= index:
                prod*=nums[i]
        return prod        
        
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        prod_nums, zero_count = self.product_all_nums(nums)
        if prod_nums !=0:
            for i in range(len(nums)):
                prod =  prod_nums//nums[i]
                answer.append(prod)
        elif prod_nums ==0 and zero_count > 1:
            for i in range(len(nums)):
                answer.append(0)
        elif prod_nums ==0 and zero_count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    prod = prod = self.product_except_index(nums,i)
                    answer.append(prod)
                else:
                    answer.append(0)
        
        return answer    