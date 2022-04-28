
import unittest
import mathlibrary
import sys


class Test(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(mathlibrary.sum(5.3, 15), 20.3)
        self.assertEqual(mathlibrary.sum(-1.2312123,
                                        10.8809098), 9.6496975)
        self.assertEqual(mathlibrary.sum(-50, -123), -173)
        self.assertEqual(mathlibrary.sum(-50.000868,
                                        123.5578700), 73.557002)
        self.assertEqual(
            mathlibrary.sum(0.0000000, 0.0000000), 0)
        self.assertRaises(OverflowError, mathlibrary.sum, sys.float_info.max, 1)

    def test_sub(self):
        self.assertAlmostEqual(mathlibrary.sub(0.00000000000, 0), 0)
        self.assertAlmostEqual(mathlibrary.sub(-111111, -111111), 0)
        self.assertAlmostEqual(mathlibrary.sub(123.1231231,
                                        50.0000068), 73.1231163)
        self.assertAlmostEqual(mathlibrary.sub(
            123123.1239123, -444.4444444), 123567.5683567)
        self.assertRaises(OverflowError, mathlibrary.sub,
                          sys.float_info.min, -1)

    def test_mult(self):
        self.assertAlmostEqual(mathlibrary.mult(172398071273971293871809.1273908,
                               1.123), 1.9360303404066976e+23
                               )
        self.assertEqual(mathlibrary.mult(41, 0), 0)
        self.assertEqual(mathlibrary.mult(0, 42), 0)
        self.assertAlmostEqual(mathlibrary.mult(
            1.1876, -789.6780000), -937.8215928)
        self.assertAlmostEqual(
            mathlibrary.mult(-1.123213, 123123.1323123), -138293.5028139)
        self.assertRaises(OverflowError, mathlibrary.mult, sys.float_info.min, 2)

    def test_div(self):
        self.assertEqual(mathlibrary.div(5, 2), 2.5)
        self.assertAlmostEqual(
            mathlibrary.div(2.2, 3), 0.7333333)
        self.assertRaises(ZeroDivisionError, mathlibrary.div, 12, 0)
        self.assertRaises(ZeroDivisionError, mathlibrary.div,
                          123123.123123, 0.000000000)
        self.assertEqual(mathlibrary.div(6546.123123, -1), -6546.123123)
        self.assertAlmostEqual(mathlibrary.div(89764590.6700, 2.1234),
                               4.227399014316662e7)
        self.assertEqual(mathlibrary.div(-65, 4), -16.25)
        self.assertEqual(mathlibrary.div(0, 42), 0)

    def test_fac(self):
        self.assertEqual(mathlibrary.fac(12), 479001600)
        self.assertEqual(mathlibrary.fac(24), 620448401733239439360000)
        self.assertRaises(OverflowError, mathlibrary.fac, 1231231245123412312)
        self.assertRaises(ValueError, mathlibrary.fac, -10)

    def test_mypow(self):
        self.assertRaises(ValueError, mathlibrary.mypow, 45, 0.2)
        self.assertAlmostEqual(mathlibrary.mypow(2.5123, 6),
                               251.4368864)
        self.assertEqual(mathlibrary.mypow(123, 12), 11991163848716906297072721)
        self.assertEqual(mathlibrary.mypow(-2, 4), 16)
        self.assertEqual(mathlibrary.mypow(2, 3), 16)
        self.assertEqual(ValueError, mathlibrary.mypow, 42, 0)
        self.assertEqual(mathlibrary.mypow(-2, 3), -8)
        self.assertAlmostEqual(mathlibrary.mypow(2.25, 0.14),
                               0.8926772)

    def test_root(self):
        self.assertEqual(mathlibrary.root(4, 2), 2)
        self.assertAlmostEqual(mathlibrary.root(2, -4), 0.8408964)
        self.assertAlmostEqual(mathlibrary.root(
            2, 2), 1.4142135623730951)
        self.assertAlmostEqual(mathlibrary.root(99, 3), 4.6260650091827)
        self.assertAlmostEqual(mathlibrary.root(1.23, 3), 1.0714412696907731079)
        self.assertRaises(ValueError, mathlibrary.root, -2, 2)
        self.assertRaises(ValueError, mathlibrary.root, -0.123123123, 81231238)
        self.assertRaises(ValueError, mathlibrary.root, 2, 0)
        self.assertRaises(ValueError, mathlibrary.root, 0, 2)

    def test_rem(self):
        self.assertEqual(mathlibrary.rem(5, 2), 1)
        self.assertAlmostEqual(mathlibrary.rem(987.333, 2.33), 1.743)
        self.assertRaises(ZeroDivisionError, mathlibrary.rem, 42, 0)
        self.assertRaises(ZeroDivisionError, mathlibrary.rem, 42,
                          000000000000.000000000000000)
        self.assertEqual(mathlibrary.rem(-3, 2), 1)
        self.assertEqual(mathlibrary.rem(2, -3), -1)
        self.assertEqual(mathlibrary.rem(0, 2.3123), 0)
        self.assertEqual(mathlibrary.rem(0000.000, 2.3123), 0)


if __name__ == '__main__':
    unittest.main()
