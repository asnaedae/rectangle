#!/usr/bin/env python

class box:
    def __init__(self, x1, y1, x2, y2):
        """ only handle case where object points are min(x,y) to max(x,y)
        error if this is not the case."""
        if x1 > x2 or y1 > y2:
            raise ValueError("x1y1 must be smaller than x2y2")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        # calculate & store box's vertices
        self.top = max(y1, y2)
        self.bottom = min(y1, y2)
        self.left = min(x1, x2)
        self.right = max(x1, x2)

    def dump(self, name="Rectangle"):
        """ dump out rectangle """
        print("%s : L %d R %d T %d B %d" %(name, self.left, self.right, self.top, self.bottom))

    def __iter__(self):
        # allow to iterate over object (for __eq__)
        yield self.x1
        yield self.y1
        yield self.x2
        yield self.y2

    def __eq__(self, o):
        """ compare objects that they are both same type(box)
        and also match contents """
        return isinstance(o, box) and tuple(self) == tuple(o)

    def contains(self, o):
        """ Check that other rectange sits within space of self """
        return self.x1 <= o.x1 <= self.x2 and self.x1 <= o.x2 <= self.x2

    def intersects(self, o):
        """ do we collide with the other box """
        if (self.left > o.left and self.left < o.right) or (self.right < o.right and self.right > o.left):
            return not (self.bottom >= o.top or self.top <= o.bottom )
        if (self.top > o.bottom and self.top < o.top ) or (self.bottom > o.bottom and self.bottom < o.top ):
            return not (self.left >= o.right or self.right >= o.left)
        return False

    def touches(self, o):
        """ adjacent if two sides touch """
        if self.left == o.right or self.right == o.left:
            """ and that bottom or top are within the range of the other side """
            return not (self.bottom >= o.top or self.top <= o.bottom )
        if self.top == o.bottom or self.bottom == o.top:
            return not (self.left >= o.right or self.right >= o.left)
        return False

if __name__ == "__main__":
    """
    Two rectangles, each defined by X1, Y1, and X2, Y2
    """
    a =  box(1, 1, 2, 2)
    b =  box(1, 1, 2, 2)
    a.dump("A")
    b.dump("B")
    print ("A intersects B : %s" %(a.intersects(b)))
    print ("A touches B : %s" %( a.touches(b)))
    print ("A contains B : %s" %( a.contains(b)))
