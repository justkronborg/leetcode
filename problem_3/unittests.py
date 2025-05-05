import unittest
from problem3_longest_substring import Solution

class TestLengthOfLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)
 
    def test_example_3(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)


if __name__ == "__main__":
    unittest.main()
