
import unittest
import mathlibary
import sys


class Test(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(mathlibary.sum(5.3, 15), 20.3)
        self.assertEqual(mathlibary.sum(-1.2312123,
                                        10.8809098), 9.6496975)
        self.assertEqual(mathlibary.sum(-50, -123), -173)
        self.assertEqual(mathlibary.sum(-50.000868,
                                        123.5578700), 73.557002)
        self.assertEqual(
            mathlibary.sum(0.0000000, 0.0000000), 0)
        self.assertRaises(OverflowError, mathlibary.sum, sys.float_info.max, 1)

    def test_sub(self):
        self.assertEqual(mathlibary.sub(0.00000000000, 0), 0)
        self.assertEqual(mathlibary.sub(-111111, -111111), 0)
        self.assertEqual(mathlibary.sub(123.1231231,
                                        50.0000068), 73.1231163)
        self.assertEqual(mathlibary.sub(
            123123.1239123, -444.4444444), 123567.568)
        self.assertRaises(OverflowError, mathlibary.sub,
                          sys.float_info.min, -1)

    def test_mul(self):
        self.assertAlmostEqual(mathlibary.mul(172398071273971293871809.1273908,
                               1.123), 1.9360303e23
                               )
        self.assertEqual(mathlibary.mul(41, 0), 0)
        self.assertEqual(mathlibary.mul(0, 42), 0)
        self.assertAlmostEqual(mathlibary.mul(
            1.1876, -789.6780000), -937.8215928)
        self.assertAlmostEqual(
            mathlibary.mul(-1.123213, 123123.1323123), -138293.5028139)
        self.assertRaises(OverflowError, mathlibary.mul, sys.float_info.min, 2)

    def test_div(self):
        self.assertEqual(mathlibary.div(5, 2), 2.5)
        self.assertAlmostEqual(
            mathlibary.div(2.2, 3), 0.7333333)
        self.assertRaises(ZeroDivisionError, mathlibary.div, 12, 0)
        self.assertRaises(ZeroDivisionError, mathlibary.div,
                          123123.123123, 0.000000000)
        self.assertEqual(mathlibary.div(6546.123123, -1), -6546.123123)
        self.assertAlmostEqual(mathlibary.div(89764590.6700, 2.1234),
                               4.2273990143224849298295186e7)
        self.assertEqual(mathlibary.div(-65, 4), 16.25)
        self.assertEqual(mathlibary.div(0, 42), 0)

    def test_fac(self):
        self.assertEqual(mathlibary.fac(12), 479001600)
        self.assertEqual(mathlibary.fac(24), 620448401733239439360000)
        self.assertRaises(OverflowError, mathlibary.fac, 1231231245123412312)
        self.assertRaises(ValueError, mathlibary.fac, -10)

    def test_pow(self):
        self.assertRaises(ValueError, mathlibary.pow, 45, 0.2)
        self.assertAlmostEqual(mathlibary.pow(2.5123, 6),
                               251.4368864)
        self.assertEqual(mathlibary.pow(123, 12), 11991163848716906297072721)
        self.assertEqual(mathlibary.pow(-2, 4), 16)
        self.assertEqual(mathlibary.pow(2, 3), 16)
        self.assertEqual(ValueError, mathlibary.pow, 42, 0)
        self.assertEqual(mathlibary.pow(-2, 3), -8)
        self.assertAlmostEqual(mathlibary.pow(2.25, 0.14),
                               0.8926772)

    def test_root(self):
        self.assertEqual(mathlibary.root(4, 2), 2)
        self.assertAlmostEqual(mathlibary.root(2, -4), 0.8408964)
        self.assertAlmostEqual(mathlibary.root(
            2, 2), 1.4142135)
        self.assertEqual(mathlibary.root(-27, 3), -3)
        self.assertAlmostEqual(mathlibary.root(99, 3), 4.6260650091827)
        self.assertAlmostEqual(mathlibary.root(1.23, 3), 1.0714412696907731079)
        self.assertRaises(ValueError, mathlibary.root, -2, 2)
        self.assertRaises(ValueError, mathlibary.root, -0.123123123, 81231238)
        self.assertRaises(ValueError, mathlibary.root, 2, 0)
        self.assertRaises(ValueError, mathlibary.root, 0, 2)

    def test_rem(self):
        self.assertEqual(mathlibary.rem(5, 2), 1)
        self.assertRaises(mathlibary.rem(987.333, 2.33), 1.743)
        self.assertRaises(ZeroDivisionError, 42, 0)
        self.assertRaises(ZeroDivisionError, 42,
                          000000000000.000000000000000)
        self.assertEqual(mathlibary.rem(-3, 2), 1)
        self.assertEqual(mathlibary.rem(2, -3), -1)
        self.assertEqual(mathlibary.rem(0, 2.3123), 0)
        self.assertEqual(mathlibary.rem(0000.000, 2.3123), 0)


if __name__ == '__main__':
    unittest.main()
