import unittest
import stats

class TestStats(unittest.TestCase):

    def test_count(self):
        self.assertEqual(stats.get_count([1, 2, 3, 4, 5]), 5)

    def test_sum(self):
        self.assertEqual(stats.get_sum([1, 2, 3, 4, 5]), 15)

    def test_mean(self):
        self.assertEqual(stats.get_mean([1, 2, 3, 4, 5]), 3)

    def test_median(self):
        self.assertEqual(stats.get_median([1, 2, 3, 4, 5]), 3)

if __name__ == '__main__':
    unittest.main()
