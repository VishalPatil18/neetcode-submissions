class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Understand:
            - n is the number of stairs
            - 1 or 2 steps at a time
        Input:  n - number of stairs to climb
        Output: Number of distinct ways to climb the top
        Plan:
            - Recursively, keep track of current sum
            - take 1 and 2 every time since we've these two choices
            - if sum == 5, add to the answer
            - if sum > 5, return and do not add
            - if sum < 5, take 1 and 2 recursively again.
        """
        # Base Case
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Recursive Statement
        answer = self.climbStairs(n - 1) + self.climbStairs(n - 2) 
        return answer
