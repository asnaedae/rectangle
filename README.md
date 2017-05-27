Rectangle
=========

Simple python module to test for the following operations on rectangles

  * Contains: One rectangle contains the other
  * Intersections: One rectangle intersects with another
  * Touches: share a side either wholly or partially

This code was written under time limited conditions and as such should not
be used in production, a better library would be to use the Shapely library.
Initially developed using Test Driven Development techniques such that the test
harness was used to prove requirements during development.

Shapely can be enabled by changing the import statements at the top of
``test_shape.py`` as follows:
```
from shapely.geometry import box
import unittest
```

Requirements:
------------

  * Python

Install nose using pip:
```
pip install unittest
```

Usage:

Simple usage would be to apply the python interpreter to ``rectangle.py``, e.g:

```
$ python rectangle/rectangle.py
A : L 1 R 2 T 2 B 1
B : L 1 R 2 T 2 B 1
A intersects B : False
A touches B : False
A contains B : True
```

Another method would be to modify the unit test framework to add additional
conditions:

```
$ python rectangle/test_shape.py
......
----------------------------------------------------------------------
Ran 6 tests in 0.005s

OK
```
Failures in implementation will be shown as follows:
```
$ python rectangle/test_shape.py
..FF..
======================================================================
FAIL: test_shapes_dont_touch (test_shape.tdd)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/mike/rectangle/test_shape.py", line 43, in test_shapes_dont_touch
    self.assertFalse(b1.intersects(b2))
AssertionError: True is not false
-------------------- >> begin captured stdout << ---------------------
Box1 L 10 R 20 T 20 B 10
Box2 L 30 R 40 T 20 B 10
--------------------- >> end captured stdout << ----------------------

======================================================================
FAIL: test_shapes_intersect (test_shape.tdd)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/mike/rectangle/test_shape.py", line 34, in test_shapes_intersect
    self.assertTrue(b1.intersects(b2))
AssertionError: False is not true
-------------------- >> begin captured stdout << ---------------------
Box1 L 10 R 20 T 20 B 10
Box2 L 15 R 25 T 25 B 15
--------------------- >> end captured stdout << ----------------------

----------------------------------------------------------------------
Ran 6 tests in 0.004s

FAILED (failures=2)
```

Assumptions:
-----------
* Rectangles are defined by lower left corner and then upper right corner only
* Only tested in first quadrant coordinates
