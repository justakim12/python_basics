import unittest
import get_next_grade


class TestApplyPenalty(unittest.TestCase):
    def test_get_next_grade(self):
        self.assertEqual(get_next_grade.ApplyPenalty('common').get_next_grade,"grey")


if __name__ == '__main__':
    unittest.main()