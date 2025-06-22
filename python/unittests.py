import unittest
from problem1_two_sum import Solution as twoSumSolution
from problem2_add_two_numbers import ListNode, Solution as AddTwoNumbersSolution
from problem3_longest_substring import Solution as LengthOfLongestSubstringSolution
from problem4_median_of_arrays import Solution as FindMedianSortedArraysSolution
from problem5_longest_palindrome import Solution as LongestPalindromeSolution

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = twoSumSolution()

    def test_example_case_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

    def test_example_case_2(self):
        nums = [3, 2, 4]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [1, 2])
    
    def test_example_case_3(self):
        nums = [3, 3]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

def list_to_linked_list(lst):
    """Helper function to convert a list to a linked list."""
    dummy_head = ListNode(0)
    current = dummy_head
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next

def linked_list_to_list(node):
    """Helper function to convert a linked list to a list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = AddTwoNumbersSolution()

    def test_case_1(self):
        l1 = list_to_linked_list([2, 4, 3])
        l2 = list_to_linked_list([5, 6, 4])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), [7, 0, 8])

    def test_case_2(self):
        l1 = list_to_linked_list([0])
        l2 = list_to_linked_list([0])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), [0])

    def test_case_3(self):
        l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = list_to_linked_list([9, 9, 9, 9])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), [8, 9, 9, 9, 0, 0, 0, 1])

class TestLengthOfLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = LengthOfLongestSubstringSolution()

    def test_example_1(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)
 
    def test_example_3(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)


class TestFindMedianSortedArrays(unittest.TestCase):
    def setUp(self):
        self.solution = FindMedianSortedArraysSolution()

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

class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = LongestPalindromeSolution()

    def test_example_1(self):
        self.assertIn(self.solution.longestPalindrome("babad"), ["bab", "aba"]) 

    def test_example_2(self):
        self.assertEqual(self.solution.longestPalindrome("cbbd"), "bb")

    def test_racecar(self):
        self.assertEqual(self.solution.longestPalindrome("racecar"), "racecar")


if __name__ == "__main__":
    unittest.main()
