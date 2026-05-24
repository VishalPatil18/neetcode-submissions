class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
            Understand
                - start from last
                - make last el as -1
                - from second last el, keep track of max num till now
                - input in prev el, this curr max el
                - find curr max again with curr el
                - do this until first el in arr
            Input
                - arr
            Output
                - modified arr
            Edge Cases
                - empty arr
                - only 1 el in arr
        """
        currItr = len(arr)
        # Edge Cases
        if currItr == 0:
            return arr
        if currItr == 1:
            return [-1]
        
        # Main Logic
        currItr -= 1
        replacer = -1
        while currItr >= 0: # Start from last until first
            currVal = arr[currItr]
            arr[currItr] = replacer
            replacer = max(replacer, currVal)
            currItr -= 1
        
        return arr

            