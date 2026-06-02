# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Input: integer n ie. the range end value
        Output: number picked
        Plan:
            - start with low and high
            - find mid and check mid using guess()
            - check output of guess()
                - if 0: return mid
                - if -1: high = mid - 1
                - if 1: low = mid + 1
        """
        # Variable Declaration
        low = 1
        high = n
        while low <= high:
            mid = low + (high - low)//2
            guessVal = guess(mid)
            if guessVal == 0:
                return mid
            elif guessVal == -1:
                high = mid - 1
            elif guessVal == 1:
                low = mid + 1
            
