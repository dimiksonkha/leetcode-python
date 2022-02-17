class Solution:
    """
    Convert 1D Array Into 2D Array
    https://leetcode.com/problems/convert-1d-array-into-2d-array/
    
    """
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        new_list = []
        if m*n != len(original):
            return new_list
        else:
            start = 0
            for i in range(m):
                end = start + n 
                temp_list = original[start:end]
                new_list.append(temp_list)
                start +=n
            return new_list