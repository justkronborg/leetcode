import unittest
from problem5_longest_palindrome import Solution

class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertIn(self.solution.longestPalindrome("babad"), ["bab", "aba"]) 

    def test_example_2(self):
        self.assertEqual(self.solution.longestPalindrome("cbbd"), "bb")

    def test_racecar(self):
        self.assertEqual(self.solution.longestPalindrome("racecar"), "racecar")


if __name__ == "__main__":
    unittest.main()