
# Day 4 Notes

## `has_triangle`, the hard way

We're asked to write a function that returns True iff either of two triplets is a triangle.

`is_triangle` does something close to what we want. We'll use it for reference.


```python
def is_triangle(a, b, c):
    if a > b + c:
        return False
    if b > a + c:
        return False
    if c > a + b:
        return False
    return True
```

Now incorporate two copies of `is_triangle` into our new function:


```python
import doctest

def has_triangles_1(a, b, c, d):
    """Return true iff either of (a, b, c) and (b, c, d) is a triangle.
    >>> has_triangles(3, 4, 5, 6)
    True
    >>> has_triangles(10, 4, 5, 6)
    """
    # first copy of is_triangle; tests a, b, c
    if a > b + c:
        return False
    if b > a + c:
        return False
    if c > a + b:
        return False
    # second copy of is_triangle; tests b, c, d
    if b > c + d:
        return False
    if c > b + d:
        return False
    if d > b + c:
        return False
    return True

doctest.run_docstring_examples(has_triangles_1, globals())
```

    **********************************************************************
    File "__main__", line 5, in NoName
    Failed example:
        has_triangles(3, 4, 5, 6)
    Expected:
        True
    Got nothing
    **********************************************************************
    File "__main__", line 7, in NoName
    Failed example:
        has_triangles(10, 4, 5, 6)
    Expected nothing
    Got:
        False


Oops! The implementation above returns True if *both* (a, b, c), (b, c, d) are triangles,
instead of if *either* of these is a triangle.

You might be able to see in the code that it returns False if *either* triplet is *not* a triangle.

Returning False iff either of two things is False, is the same as returning True iff both those things are True. [[De Morgan's Laws](https://en.wikipedia.org/wiki/De_Morgan's_laws)].

This is difficult to fix starting from the implementation of `is_triangle` above, because it returns out of the whole function as soon as it detects a triangle violation.

We'll modify `is_triangle` to remember its result into a variable instead of returning right away. This will be easier to work with.


```python
def is_triangle_2(a, b, c):
    result = True
    if a > b + c:
        return result
    if b > a + c:
        return result
    if c > a + b:
        return result
    return result
```


```python
def has_triangles_2(a, b, c, d):
    """Return true iff either of (a, b, c) and (b, c, d) is a triangle.
    >>> has_triangles(3, 4, 5, 6)
    True
    >>> has_triangles(10, 4, 5, 6)
    False
    """
    # first copy of the new is_triangle
    tri1 = True
    if a > b + c:
        tri1 = False
    if b > a + c:
        tri1 = False
    if c > a + b:
        tri1 = False
    # second copy
    tri2 = True
    if b > c + d:
        return tri2
    if c > b + d:
        return tri2
    if d > b + c:
        return tri2
    return tri1 and tri2
```

`has_triangles_2` is functionally identical to `has_triangles_1`. It doesn't fix the bug. It is, however, easier to work with.

In particular, now we can change the final `and` to `or`.


```python
def has_triangles_2(a, b, c, d):
    """Return true iff either of (a, b, c) and (b, c, d) is a triangle.
    >>> has_triangles(3, 4, 5, 6)
    True
    >>> has_triangles(10, 4, 5, 6)
    False
    """
    # first copy of the new is_triangle
    tri1 = True
    if a > b + c:
        tri1 = False
    if b > a + c:
        tri1 = False
    if c > a + b:
        tri1 = False
    # second copy
    tri2 = True
    if b > c + d:
        tri2 = False
    if c > b + d:
        tri2 = False
    if d > b + c:
        tri2 = False
    # now combine them
    return tri1 and tri2

doctest.run_docstring_examples(has_triangles_2, globals())
```

    **********************************************************************
    File "__main__", line 3, in NoName
    Failed example:
        has_triangles(3, 4, 5, 6)
    Expected:
        True
    Got nothing


`has_triangles_2` fixes the problem for the computer, but not for the human. It's still difficult to read. It's therefore difficult to match up the implementation against the specification; and it's difficult to test. (There's a lot of different paths the code could take, and it's effortful to construct test cases for them all.)

Instead of using the original `is_triangle` to copy from, we can simply call it.


```python
def has_triangles_3(a, b, c, d):
    tri1 = is_triangle_1(a, b, c)
    tri2 = is_triangle_1(b, c, d)
    return tri1 and tri2
```

Or eliminate the temporary variables:


```python
def has_triangles_4(a, b, c, d):
    return is_triangle(a, b, c) and is_triangle(b, c, d)
```


```python
## Lists and `for`
```


```python
def contains_triangle(triplets):
    """Returns true if any of triplets is the sides of a triangle.
    
    Triplets is a list of triples. Each triple is a list of three numbers.
    Example:
    >>> contains_triangle([[10, 2, 3]])
    False
    >>> contains_triangle([[10, 2, 3], [4, 5, 6]])
    True
    """
    for triplet in triplets:
        a = triplet[0]
        b = triplet[1]
        c = triplet[2]
        if is_triangle(a, b, c):
            return True
    return False

doctest.run_docstring_examples(contains_triangle, globals())
```

## Code Golfing `is_triangle`


```python
# as presented
def is_triangle(a, b, c):
    if a > b + c:
        return False
    if b > a + c:
        return False
    if c > a + b:
        return False
    return True

# ->

def is_triangle(a, b, c):
    return not (a > b + c) and not (b > a + c) and not (c > a + b)

# ->

def is_triangle(a, b, c):
    return a <= b + c and b <= a + c and c <= a + b

is_triangle(3, 4, 5)
```




    True




```python
def has_triangle(a, b, c, d):
    """Return true if either or both (a, b, c) or (b, c, d) is a triangle."""
    # Return true if (a, b, c) and (b, c, d) are both triangle.
    tri1 = is_triangle(a, b, c)
    tri2 = is_triangle(b, c, d)
    return tri1 or tri2

# has_triangle(3, 4, 5, 6)

has_triangle(10, 4, 5, 6)
```




    True




```python
def contains_triangle(triples):
    """Return true if any of the triples is a triangle."""
    for a, b, c in triples:
        if is_triangle(a, b, c):
            return True
    return False

contains_triangle([[1, 1, 3], [3, 4, 5]])
```




    True




```python
# Code-Golfing contains_triangle
```


```python
def contains_triangle(triplets):
    for triplet in triplets:
        a, b, c = triplet[0]
        if is_triangle(a, b, c):
            return True
    return False
```


```python
def contains_triangle(triplets):
    for triplet in triplets:
        if is_triangle(triplet[0], triplet[1], triplet[2]):
            return True
    return False
```

### Code-Golfing using advanced techniques

Using a "starred expression", to unpack the elements in a list (triplets) into individual values that are successive arguments to `is_triangle`.

[In other languages you may see this called "spread", "splat", "argument unpacking", or "variadic arguments".]


```python
def contains_triangle(triplets):
    for triplet in triplets:
        if is_triangle(*triplet):
            return True
    return False
```

Using the `any` function, and a [generator comprehension](https://www.python.org/dev/peps/pep-0289/):


```python
def contains_triangle(triplets):
    return any(is_triangle(a, b, c) for a, b, c in triplets)
```

Starred expression together with a generator comprehension:


```python
def contains_triangle(triplets):
    return any(is_triangle(*triplet) for triplet in triplets)
```

Now let's code-golf `is_triangle`. (Conceptually) unpacking this is left as an exercise for the reader.

I've changed the signature of `is_triangle` to take a triple instead of three separate sides. You could use the original signature by starting each of these with:

    def  is_triangle(a, b, c):
        sides = [a, b, c]
        …


```python
def is_triangle(a, b, c):
    """Return true iff either of (a, b, c) and (b, c, d) is a triangle.
    >>> is_triangle(3, 4, 5)
    True
    >>> is_triangle(10, 4, 5)
    False
    """
    sides = [a, b, c]
    # The following overwrites the original parameter values of a, b, c.
    # We are very far from readable code at this point anyway…
    for i, a in enumerate(sides):
        b, c = sides[:i] + sides[i + 1:]
        if a > b + c:
            return False
    return True
    
doctest.run_docstring_examples(is_triangle, globals())
```


```python
def is_triangle(a, b, c):
    """Return true iff either of (a, b, c) and (b, c, d) is a triangle.
    >>> is_triangle(3, 4, 5)
    True
    >>> is_triangle(10, 4, 5)
    False
    """
    sides = [a, b, c]
    return all(a <= b + c
               for i, a in enumerate(sides)
               for b, c in [sides[:i] + sides[i + 1:]])
    
doctest.run_docstring_examples(is_triangle, globals())
```


```python
import itertools

def is_triangle(a, b, c):
    """Return true iff either of (a, b, c) and (b, c, d) is a triangle.
    >>> is_triangle(3, 4, 5)
    True
    >>> is_triangle(10, 4, 5)
    False
    """
    return all(a <= b + c for a, b, c in itertools.permutations([a, b, c]))
    
doctest.run_docstring_examples(is_triangle, globals())
```
