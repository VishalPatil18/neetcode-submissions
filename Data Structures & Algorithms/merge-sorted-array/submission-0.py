class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        Understand: 
            - nums1 has m + n elements
            - merge nums1 and nums2 in increasing order of elements, it should be done inplace
        Input:
            - nums1 list, nums2 list, m and n as int
        Output:
            - Array nums1 with the merged list
        Edge Case:
            - Empty nums1 or nums2
        Plan:
            - start with two iterators for nums1 and nums2
            - start merging from the end in reverse order
            - check which element among itr1 and itr2 is bigger and place it at the end
              of nums1. 
            - keep doing this until you reach the start of nums1 or nums2
            - if one array gets exhausted, then place all the remaining elements of other
              array in same order as it is
        """
        # Edge Cases
        if m == 0:
            nums1[:n] = nums2[:]
            return
        
        itr1 = m-1
        itr2 = n-1
        curr = m + n - 1
        while itr1 >= 0 and itr2 >= 0:
            if nums1[itr1] >= nums2[itr2]:
                nums1[curr] = nums1[itr1]
                itr1 -= 1
            else:
                nums1[curr] = nums2[itr2]
                itr2 -= 1
            curr -= 1

        while itr1 >= 0:
            nums1[curr] = nums1[itr1]
            curr -= 1
            itr1 -= 1

        while itr2 >= 0:
            nums1[curr] = nums2[itr2]
            curr -= 1
            itr2 -= 1

        return
        