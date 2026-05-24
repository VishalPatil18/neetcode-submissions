class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        
        currItr = 0
        while currItr < len(nums) and nums[currItr] != val:
            currItr += 1
        replacer = currItr
        currItr += 1
        while currItr < len(nums):
            if nums[currItr] != val:
                nums[replacer] = nums[currItr]
                replacer += 1
            currItr += 1
        return replacer