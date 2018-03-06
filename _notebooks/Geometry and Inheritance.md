---
date: 2018-03-05T23:46:26-05:00
source: notebooks/Geometry and Inheritance.ipynb
---

{% include toc %}



```python
class Rectangle(object):
    def __init__(self, x1, y1, width, height):
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height
    
    def get_area(self):
        return w*h

class Triangle(object):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    
    def get_area(self):
        return 0.5*(-self.x2*self.y1 +
                    self.x3*self.y1 +
                    self.x1*self.y2 -
                    self.x3*self.y2 -
                    self.x1*self.y3 +
                    self.x2*self.y3)

class Square(object):
    def __init__(self, x1, y1, side_length):
        self.x1 = x1
        self.y1 = y1
        self.side_length = side_length
    
    def get_area(self):
        return self.side_length**2

class Polygon(object):
    def __init__(self, vertices):
        """ vertices must be in counterclockwise order """
        self.vertices = vertices
    
    def get_area(self):
        """ Using formula from http://mathworld.wolfram.com/PolygonArea.html
        
        >>> p = Polygon([(0, 0), (200, 0), (200, 300), (0, 300)])
        >>> p.get_area()
        60000.0
        """
        area = 0.0
        for i, v_i in enumerate(self.vertices):
            v_i = self.vertices[i]
            v_i_plus_1 = self.vertices[(i+1) % len(self.vertices)]
            area += 0.5*(v_i[0]*v_i_plus_1[1] - v_i[1]*v_i_plus_1[0])
        return area

import doctest
doctest.testmod()
```

{: class="nb-output"}




    TestResults(failed=0, attempted=2)



