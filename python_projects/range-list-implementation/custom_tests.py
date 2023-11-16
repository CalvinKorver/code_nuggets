import unittest

from RangeList import RangeList


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.rl = RangeList()

    def test_empty(self):
        self.assertEqual(self.rl.toString(), "")

    def test_one_interval(self):
        self.rl.add([1, 5])
        self.assertEqual(self.rl.toString(), "[1, 5)")

    def test_two_intervals(self):
        self.rl.add([1, 5])
        self.rl.add([10, 20])
        self.assertEqual(self.rl.toString(), "[1, 5), [10, 20)")

    def test_single_overlapping_intervals(self):
        self.rl.add([1, 5])
        self.rl.add([3, 8])
        self.assertEqual(self.rl.toString(), "[1, 8)")

    def test_remove_exact_match(self):
        self.rl.add([1, 5])
        self.rl.remove([1, 5])
        self.assertEqual(self.rl.toString(), "")

    def test_edgy_casie(self):
        self.rl.add([1, 8])
        self.rl.add([10, 21])
        self.rl.remove([3, 19])
        self.assertEqual(self.rl.toString(), "[1, 3), [19, 21)")


if __name__ == '__main__':
    unittest.main()

