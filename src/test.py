from decimal import ValueError
import unittest
import calc
import sys


class Test(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(calc.sum(5.3, 15), 20.3)
        self.assertAlmostEqual(calc.sum(-1.12312123123231231,
                                        10.1231231288090883123123123), 9.0000018975767760023123123)
        self.assertEqual(calc.sum(-50, -123), -173)
        self.assertAlmostEqual(calc.sum(-50.00000000000000000000068,
                                        123.123123123123412412435465578700), 73.123123123123412412435465578768)
        self.assertEqual(
            calc.sum(0.000000000000000000000000, 0.00000000000), 0)
        self.assertRaises(OverflowError, calc.sum, sys.float_info.max, 1)

    def test_sub(self):
        self.assertEqual(calc.sub(0.000000000000000000000000, 0), 0)
        self.assertEqual(calc.sub(-111111, -111111), 0)
        self.assertAlmostEqual(calc.sub(123.123123123123412412435465578700,
                                        50.00000000000000000000068), 73.123123123123412412435465578768)
        self.assertEqual(calc.sub(
            123123.123123, -444.4444444123), 123567.567567)
        self.assertRaises(OverflowError, calc.sub,
                          sys.float_info.min, -1)

    def test_mul(self):
        self.assertAlmostEqual(calc.mul(172398071273971293871809.1273908217308120938,
                               1.123), 1.936030340406697630180416500598928037019813374e23)
        self.assertEqual(calc.mul(41, 0), 0)
        self.assertEqual(calc.mul(0, 42), 0)
        self.assertEqual(calc.mul(1.1876, -789.67800000000), -937.8215928)
        self.assertEqual(calc.mul(-1.123213, 123123.1323123), -138293.5028139)
        self.assertRaises(OverflowError, calc.mul, sys.float_info.min, 2)

    def test_div(self):
        self.assertEqual(calc.div(5, 2), 2.5)
        self.assertAlmostEqual(
            calc.div(2.2, 3), 0.73333333333333333333333333333333)
        self.assertRaises(ValueError, calc.div, 12, 0)
        self.assertRaises(ValueError, calc.div, 123123.123123, 0.000000000)
        self.assertEqual(calc.div(6546.123123, -1), -6546.123123)
        self.assertEqual(calc.div(89764590.6700, 2.1234),
                         4.2273990143224849298295186e7)
        self.assertEqual(calc.div(-65, 4), 16.25)
        self.assertEqual(calc.div(0, 42), 0)

    def test_fac(self):
        self.assertEqual(calc.fac(12), 479001600)
        self.assertEqual(calc.fac(24), 620448401733239439360000)
        self.assertRaises(ValueError, calc.fac, 1231231245123412312)

    def test_pow(self):
        self.assertRaises(ValueError, calc.pow, 45, 0.2)
        self.assertAlmostEqual(calc.pow(2.5123, 6),
                               251.436886405351180727441689)
        self.assertEqual(calc.pow(123, 12), 11991163848716906297072721)
        self.assertEqual(calc.pow(-2, 4), 16)
        self.assertEqual(calc.pow(2, 3), 16)
        self.assertEqual(ValueError, calc.pow, 42, 0)
        self.assertEqual(calc.pow(-2, 3), -8)
        self.assertAlmostEqual(calc.pow(2.25, 0.14),
                               0.892677210129945408009515433)

    def test_root(self):
        self.assertEqual(calc.root(4, 2), 2)
        self.assertEqual(calc.root(2, -4), 0.840896415253714543031125476233214)
        self.assertAlmostEqual(calc.root(
            2, 2), 1.4142135623730950488016887242)
        self.assertEqual(calc.root(-27, 3), -3)
        self.assertAlmostEqual(calc.root(99, 3), 4.6260650091827)
        self.assertAlmostEqual(calc.root(1.23, 3), 1.0714412696907731079)
        self.assertRaises(ValueError, calc.root, -2, 2)
        self.assertRaises(ValueError, calc.root, -0.123123123, 81231238)
        self.assertRaises(ValueError, calc.root, 2, 0)
        self.assertRaises(ValueError, calc.root, 0, 2)

    def test_rem(self):
        self.assertEqual(calc.rem(5, 2), 1)
        self.assertRaises(calc.rem(987.333, 2.33), 1.743)
        self.assertRaises(ValueError, 42, 0)
        self.assertRaises(ValueError, 42,
                          000000000000.000000000000000)
        self.assertEqual(calc.rem(-3, 2), 1)
        self.assertEqual(calc.rem(2, -3), -1)
        self.assertEqual(calc.rem(0, 2.3123), 0)
        self.assertEqual(calc.rem(0000.000, 2.3123), 0)


if __name__ == '__main__':
    unittest.main()
