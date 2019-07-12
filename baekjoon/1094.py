import unittest


class Backjoon1094(unittest.TestCase):
    def f1094(self, x):
        length = 64
        sum = 0
        count = 0

        while x > 0:
            if length > x:
                length /= 2
            else:
                count += 1
                print("length > x {}".format(length))
                x -= length
        return count

    def test1094(self):
        expect = 4
        actual = self.f1094(23)
        self.assertEqual(expect, actual)
