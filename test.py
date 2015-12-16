#!/usr/bin/python
import unittest
import align


class AlignTest(unittest.TestCase):


    def test_calc_alignment(self):
        expected = [1,1,1,1,1]
        actual = align.calc_alignment("aaaaa", "aaaaa")
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
