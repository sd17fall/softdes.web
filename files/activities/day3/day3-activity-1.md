## Q3. Fruitful functions

Modify `is_triangle` to *return* `"Yes"` and `"No"`, instead of *printing* these values.

``` python
def is_triangle_3(a, b, c):
    "Return "Yes" or "No", depending on whether the side lengths can form a triangle."
    …
```

For discussion: Where could `is_triangle_3` be used, that `is_triangle_2` could not be?

## Q4. Boolean values versus strings

Modify `is_triangle` to return boolean values `True` and `False` instead of string values `"Yes"` and `"No"`.

``` python
def is_triangle_4(a, b, c):
    "Return True or False, depending on whether the side lengths can form a triangle."
    …
```

For discussion: What (if any) is the advantage of `is_triangle_4` over `is_triangle_3` ?

### GB3. `ipython`

`ipython` is an alternative to the `python` <strong>REPL</strong> (Read-Event-Print Loop). Try it

### GB4. `lambda`

See if you can figure out what the following is doing. Is there a similar mechanism in other language you know?

``` python
def add(a, b):
    return a + b

add = lambda a, b: a + b
```
