from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the two sorted arrays
        merged = nums1 + nums2
        merged.sort()

        mid = len(merged) // 2

        # If the length of the merged array is even, return the average of the two middle elements
        # If the length is odd, return the middle element
        if len(merged)%2!=0:
            return merged[mid]
        else:
            return (merged[mid]+merged[mid-1])/2
