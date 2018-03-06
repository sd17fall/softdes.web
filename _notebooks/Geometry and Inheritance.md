---
date: 2018-03-05T23:47:27-05:00
source: notebooks/Geometry and Inheritance.ipynb
---

{% include toc %}


# Inheritance Example: 2D Geometry

The classes below represent simple 2D shapes.  Currently the only supported functionality is `get_area`, but more could be added.


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
        """
        >>> Rectangle(1.0, 3.0, 100.0, 50.0).get_area()
        5000.0
        """
        return self.width*self.height

class Triangle(object):
    """ Represents a triangle in 2D """

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
        """
        >>> Triangle(0.0, 0.0, 10.0, 0.0, 0.0, 5.0).get_area()
        25.0
        """
        # using formula from http://mathworld.wolfram.com/TriangleArea.html
        return 0.5*(-self.x2*self.y1 +
                    self.x3*self.y1 +
                    self.x1*self.y2 -
                    self.x3*self.y2 -
                    self.x1*self.y3 +
                    self.x2*self.y3)

class Square(object):
    """ Represents a square in 2D """

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
        """
        >>> Square(1.0, 3.0, 50.0).get_area()
        2500.0
        """
        return self.side_length**2

class Polygon(object):
    """ Represents a polygon in 2D """
    def __init__(self, vertices):
        """ Initialize a polygon from a list of vertices, where each
            vertex is represented as an (x, y) tuple.
            
            vertices: the vertices of the polygone (note: vertices
                      are assumed to be in counterclockwise order """
        self.vertices = vertices
    
    def get_area(self):
        """
        >>> Polygon([(0, 0), (200, 0), (200, 300), (0, 300)]).get_area()
        60000.0
        """
        # Using formula from http://mathworld.wolfram.com/PolygonArea.html
        area = 0.0
        for i, v_i in enumerate(self.vertices):
            v_i_plus_1 = self.vertices[(i+1) % len(self.vertices)]
            area += 0.5*(v_i[0]*v_i_plus_1[1] - v_i[1]*v_i_plus_1[0])
        return area

import doctest
doctest.testmod()
```

{: class="nb-output"}




    TestResults(failed=0, attempted=4)




1.  Simplify the code above using inheritance.  You can either cut-and-paste the code  and modify it in the cell below, or modify the original code.

<ol start="2">
<li>Create a right triangle class (make sure to use inheritance!)</li>
</ol>

<ol start="3">
<li>Add a function called `get_hypotenuse_length` to your right triangle class.</li>
</ol>
