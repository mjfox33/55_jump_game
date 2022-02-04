class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        if n==1:
            return True
        if nums[0] == n-1:
            return True
        if nums[0] == 0:
            return False
        if nums[0] == 1 and nums[1] == 0:
            return False

        max_reach = 0
        for i in range(n):
            if nums[i] >= n-1-i:
                return True
            if nums[i] > 0:
                max_reach = max(max_reach,i + nums[i])
            if max_reach <= i:
                return False
        return True
            
                
                            