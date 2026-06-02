class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Input: array nums sorted in asc order, target int that we need to find
        Output: Index of target, else -1
        Edge Case: Empty Array
        Plan:
            - have two pointers low and high
            - while low <= high, find the mid of low and high
            - check if mid == target, if yes return mid
            - if mid < target: check on right side, ie. low = mid + 1
            - if mid > target: check on left side, ie. high = mid - 1
            - if low > high: return -1
        """
        # Edge Case
        if not nums:
            return -1
        
        # Variable Declaration
        low = 0
        high = len(nums) - 1
        
        # Main Logic
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
            
        return -1
