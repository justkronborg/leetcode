import unittest
from problem4_median_of_arrays import Solution


class TestFindMedianSortedArrays(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums1 = [1, 3]
        nums2 = [2]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 2.0)

    def test_example_2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 2.5)


if __name__ == "__main__":
    unittest.main()
