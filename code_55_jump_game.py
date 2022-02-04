class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        if n==1:
            return True
        if nums[0] == n-1:
            return True
        if nums[0] == 0:
            return False
        
        for i in range(n-1):
            if nums[i] >= n-1-i:
                if i==0:
                    return True
                for j in range(i):
                    if nums[j] >= i-j:
                        if j==0:
                            return True
                        for k in range(j):
                            if nums[k] >= j-k:
                                return True
        return False
        