class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        itr = 0
        for x in nums:
            if x == 1:
                itr += 1
            else:
                ans = max(itr, ans)
                itr = 0
        ans = max(itr, ans)
        return ans