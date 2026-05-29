# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        """
        Input: List of pairs of key and value
        Output: List sorted according to key
        Edge Case: Single Element
        Plan:
            - Insertion sort on the keys for each pair from the list
            - start iteration from 2nd element until end
            - compare current element with previous
                - if curr > prev: move to next element
                - if curr < prev: 
                    - swap them both
                    - move to prev of prev until we reach start of array 
                      and keep comparing and swapping
        """
        # Edge Cases
        if len(pairs) <= 1:
            return [pairs]

        # Main Logic
        answer = []
        for i in range(len(pairs)):
            j = i - 1
            while j >= 0 and pairs[j].key > pairs[j+1].key:
                # Swap
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                j -= 1
            answer.append(pairs[:])
        
        return answer
