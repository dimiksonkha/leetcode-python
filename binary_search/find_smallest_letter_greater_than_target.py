class Solution:
    """
    Find Smallest Letter Greater Than Target
    https://leetcode.com/problems/find-smallest-letter-greater-than-target/
    
    """
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        if n == 1:
            return letters[0]
        elif n == 0:
            return letters
        low = 0
        high = n-1
        mid = low+(high-low)//2
        last_index = 0
    
        while low<=high:
            if target == letters[mid]:
                
                if mid!=n-1 and letters[mid+1] == target :
                    mid = mid+1
                elif mid!=n-1:
                    return letters[mid+1]
                else:
                    return letters[0]
                
            elif target < letters[mid]:
                    last_index = mid
                    high = mid-1
                    mid = low + (high-low)//2
            else :
                low = mid+1
                mid = low +(high-low)//2

      
        if (last_index == n-1 and target < letters[last_index]) or (last_index > 0 and last_index <n-1):
            return letters[last_index]
        
        else:
            return letters[0]
                
        