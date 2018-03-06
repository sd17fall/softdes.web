---
date: 2018-03-05T23:47:27-05:00
source: notebooks/Geometry and Inheritance.ipynb
---

{% include toc %}


# Inheritance Example: 2D Geometry

Todo write prompts


```python
class Rectangle(object):
    """ Represents a rectangle in 2D """
    def __init__(self, x1, y1, width, height):
        """ Initialize a rectangle from the upper left corner vertex and
            its width and height.
            
            x1: x-coordinate of the upper left corner of the rectangle
            y1: y-coordinate of the upper left corner of the rectangle
            width: width of the rectangle
            height: height of the rectangle
        """
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height
    
    def get_area(self):
        return w*h

class Triangle(object):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        """ Initialize a triangle from its three vertices.  The vertices
            are assumed to be in counterclockwise order.
            
            x1: x-coordinate of the first vertex of the triangle
            y1: y-coordinate of the first vertex of the triangle
            x2: x-coordinate of the second vertex of the triangle
            y2: y-coordinate of the second vertex of the triangle
            x3: x-coordinate of the third vertex of the triangle
            y3: y-coordinate of the third vertex of the triangle
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    
    def get_area(self):
        # using formula from http://mathworld.wolfram.com/TriangleArea.html
        return 0.5*(-self.x2*self.y1 +
                    self.x3*self.y1 +
                    self.x1*self.y2 -
                    self.x3*self.y2 -
                    self.x1*self.y3 +
                    self.x2*self.y3)

class Square(object):
    def __init__(self, x1, y1, side_length):
        """ Initialize a square from the upper left corner vertex and
            its side length.
            
            x1: x-coordinate of the upper left corner of the rectangle
            y1: y-coordinate of the upper left corner of the rectangle
            side_length: side length of the square
        """
        self.x1 = x1
        self.y1 = y1
        self.side_length = side_length
    
    def get_area(self):
        return self.side_length**2

class Polygon(object):
    def __init__(self, vertices):
        """ Initialize a polygon from a list of vertices, where each
            vertex is represented as an (x, y) tuple.
            
            vertices: the vertices of the polygone (note: vertices
                      are assumed to be in counterclockwise order """
        self.vertices = vertices
    
    def get_area(self):
        """
        >>> p = Polygon([(0, 0), (200, 0), (200, 300), (0, 300)])
        >>> p.get_area()
        60000.0
        """
        # Using formula from http://mathworld.wolfram.com/PolygonArea.html
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




1.  Simplify the code above using inheritance.

<ol start="2">
<li>Using inheritance, create a right triangle class.</li>
</ol>

Going beyond:
