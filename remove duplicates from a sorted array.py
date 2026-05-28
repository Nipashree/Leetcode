from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        
        dq = deque()
        result = []
        
        for i in range(len(nums)):
            
            # Remove indices outside window
            while dq and dq[0] <= i - k:
                dq.popleft()
            
            # Remove smaller elements
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)
            
            # Store result after first window
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result
