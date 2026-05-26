class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        Input: List of int
        Output: List of int with new concatenated arr
        Edge Cases: Empty Array
        Plan: 
            - create a new array and insert the same array to it using concat
        """
        ans = nums + nums
        return ans