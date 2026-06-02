class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Input: int array piles which piles[i] = no. of banana in ith pile, int h = no of hours
        Output: minimum int K such that you eat all bananas in h hours
        Plan:
            - minrate (k) = 1
            - maxrate (k) = max of piles
            - do a binary search for k in this range of 1 to max of piles
            - check if that k satisfies the eating of all bananas in less than h hours
            - if yes -> move to left
            - if no -> move to right
            - do till end and return the last answer that satisfied the condition
        """
        low, high = 1, max(piles)
        ans = high

        while low <= high:
            k = (low + high)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            
            if hours <= h:
                ans = min(ans, k)
                high = k - 1
            else:
                low = k + 1

        return ans