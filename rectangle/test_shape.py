#!/usr/bin/env python

#from shapely.geometry import box
import unittest
from rectangle import box

class tdd(unittest.TestCase):

    def test_shapes_are_identical(self):
        # shape defined as
        b1 = box(0, 0, 10, 10)
        b2 = box(0, 0, 10, 10)
        self.assertEqual(b1, b2)

    def test_shapes_touch_subline(self):
        b1 = box(10, 10, 20, 30)
        b2 = box(20, 20, 40, 35)
        self.assertNotEqual(b1, b2)
        self.assertTrue(b1.touches(b2))

    def test_shapes_touch_wholly(self):
        b1 = box(10, 10, 20, 30)
        b2 = box(20, 10, 30, 30)
        self.assertTrue(b1.touches(b2))

    def test_shapes_contains(self):
        b1 = box(10, 10, 20, 20)
        b2 = box(15, 15, 17, 17)
        self.assertTrue(b1.contains(b2))
        self.assertFalse(b2.contains(b1))

    def test_shapes_intersect(self):
        b1 = box(10, 10, 20, 20)
        b2 = box(15, 15, 25, 25)
        self.assertTrue(b1.intersects(b2))
        self.assertFalse(b1.contains(b2))
        self.assertFalse(b1.touches(b2))

    def test_shapes_dont_touch(self):
        b1 = box(10, 10, 20, 20)
        b2 = box(30, 10, 40, 20)
        self.assertFalse(b1.touches(b2))
        self.assertFalse(b1.contains(b2))
        self.assertFalse(b1.intersects(b2))

    def test_shapes_intersect_at_corner(self):
        b1 = box(10, 10, 30, 30)
        b2 = box(20, 20, 40, 40)
        self.assertTrue(b1.intersects(b2))
        self.assertTrue(b2.intersects(b1))

if __name__ == '__main__':
    unittest.main()
