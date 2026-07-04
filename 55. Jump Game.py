class Solution:
    def canJump(self, nums):
        
        maxReach = 0
        
        for i in range(len(nums)):
            
            # Can't reach this position
            if i > maxReach:
                return False
            
            maxReach = max(maxReach, i + nums[i])
        
        return True
