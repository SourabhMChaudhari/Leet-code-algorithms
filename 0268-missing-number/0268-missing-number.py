class Solution:
    def missingNumber(self, nums: List[int]) -> int:
          
            length = len(nums)
            
            for i in range(0, length + 1):
                 
                if i not in nums:
                    return i
            