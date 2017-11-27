---
date: 2017-11-27T15:53:48-05:00
source: notebooks/complexity-and-halting-teaser.ipynb
---

{% include toc %}


# Order of Growth


```python
def f1(n):
    """Return the sum of 0..(n-1)."""
    s = 0
    for i in range(n):
        s += i
    return s

%timeit f1(10)
%timeit f1(100)
%timeit f1(1000)
```

{: class="nb-output"}

    1000000 loops, best of 3: 853 ns per loop
    100000 loops, best of 3: 5.28 µs per loop
    10000 loops, best of 3: 56.2 µs per loop




```python
def f2(n):
    """Return the sum of 0..(n-1)."""
    return n * (n + 1) / 2

%timeit f2(10)
%timeit f2(100)
%timeit f2(1000)
```

{: class="nb-output"}

    The slowest run took 8.10 times longer than the fastest. This could mean that an intermediate result is being cached.
    10000000 loops, best of 3: 161 ns per loop
    The slowest run took 6.92 times longer than the fastest. This could mean that an intermediate result is being cached.
    10000000 loops, best of 3: 182 ns per loop
    The slowest run took 6.06 times longer than the fastest. This could mean that an intermediate result is being cached.
    10000000 loops, best of 3: 191 ns per loop




```python
def f3(n):
    """A shorter implementation of a program with many longer and less intentional implementations."""
    while True:
        pass
```


```python
def f4(fname):
    """Count the newlines in the file. (This may be one less than the number of lines.)"""
    source = open(fname).read()
    s = 0
    for c in source:
        if c == '\n':
            s += 1
    return s
```


```python
def f5(fname):
    """
    Return true if and only if fname is a Python source file that halts when run.
    
    This could more mnemonically be named 'halts'.
    
    >>> halts('f1.py') # f1.py is a file that defines f1 above, and calls `f1(100)`
    True
    >>> halts('f2.py') # f2.py is a file that defines f2 above, and calls `f2(100)`
    True
    >>> halts('f3.py') # f3.py is a file that defines f2 above, and calls `f3(100)`
    False
    >>> halts('f4.py') # f3.py is a file that defines f2 above, and calls `f4('f4.py')`
    True
    """
    source = open(fname).read()
    # TODO replace following line by code that sets `halts` to True
    # if and only if source is a python program that halts when run.
    halts = False
    return halts
```


```python
def f6(fname):
    """
    This could more mnemonically be named 'doesnt_halt'.

    >>> halts('f1.py') # f1.py is a file that defines f1 above, and calls `f1(100)`
    False
    >>> halts('f2.py') # f2.py is a file that defines f2 above, and calls `f2(100)`
    False
    >>> halts('f3.py') # f3.py is a file that defines f2 above, and calls `f3(100)`
    True
    >>> halts('f4.py') # f3.py is a file that defines f2 above, and calls `f4('f4.py')`
    False
    >>> halts('f6.py') # f6.py is a file that defines this function f6, and calls `f6('f6.py')`
    ???
    """
    return not f6(fname)
```
