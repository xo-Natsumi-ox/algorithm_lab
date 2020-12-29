from naivniy import naive_search
import unittest


class TestMethods(unittest.TestCase):
    def test_one(self):
        self.assertEqual(naive_search("aabbaaaaaabaabbbb", "aab"), [(0, 2), (8, 10), (11, 13)])

    def test_two(self):
        self.assertEqual(naive_search("abcdababcabecdebabce", "abc"), [(0, 2), (6, 8), (16, 18)])

    def test_three(self):
        self.assertEqual(naive_search("trololo", "olo"), [(2, 4), (4, 6)])

    def test_four(self):
        self.assertEqual(naive_search("ololol", "olol"), [(0, 3), (2, 5)])

    def test_five(self):
        self.assertEqual(naive_search("eeeeee", "eee"), [(0, 2), (1, 3), (2, 4), (3, 5)])

    def test_empty_string(self):
        self.assertEqual(naive_search("", "eee"), [])

    def test_empty_substring(self):
        self.assertEqual(naive_search("eee", ""), [])

if __name__ == '__main__':
    unittest.main()
