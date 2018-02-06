---
date: 2017-09-24T16:06:29-04:00
source: notebooks/iteration-patterns.ipynb
---

{% include toc %}


# Iteration Patterns – map, filter, and reduce

You've learned three **ways** to iterate:

1. Using a `while` loop:
    ```python
    i = 0
    while i < len(lst):
        // do something with lst[i]
    ```
2. Using a `for` loop with `range`:
    ```python
    for i in range(len(lst)):
        // do something with lst[i]
    ```
3. Using a `for` loop *without* `range`:
    ```python
    for item in lst:
        // do something with item
    ```

This page discusses three **uses** for iteration:

**Mapping**

To apply a transformation to every item in a list, and collect the transformed elements. This operation is called **map**.

For example, mapping the operation "add ten" across every item in the list \[2, 4, 6\] produces the list \[12, 14, 16\].

**Filter**

To narrow the list down to only those items that meet a certain criterion. This operation is called **filter** or **select**, or (if the criterion is expressed as which items *not* to include) **reject**.

For example, filtering or selecting the list \[2, 4, 6, 8\] against the criterion "is greater than 5" produces the list \[6, 8\]. *Rejecting* the items of \[2, 4, 6, 8\] that match the criterion "is greater than 5" produces the list \[2, 4\].

**Reduce**

Combining the items in a list into a single value. This operation is called **reduce** or **fold**.

For example, using addition to reduce \[2, 4, 6\] produces the result $2 + 4 + 6 = 12$. Using multiplication produces $2 \times 4 \times 6 = 24$.

Note 1: If you want to show off, you can also call this a [catamorphism](https://en.wikipedia.org/wiki/Catamorphism).

Note 2: *In general*, it can matter whether you reduce left-to-right or right-to-left – whether you use a **left fold** or a **right fold**. With addition, and with multiplication of integers, it doesn't: $(2 + 4) + 6 = 2 + (4 + 6)$. Reduce and fold generally go left-to-right, unless otherwise specified.

There are other reasons to iterate, but these three are so common that they have names. (In fact, more than one, as you can see.)

# Map

*Mapping* applies a modification to each element in a list.

There's two ways to do this:
1. modify the original list
2. return a new list.

These correspond to `chop` and `middle` from first reading journal.

### A map that modifies its argument

This function modifies its argument:


```python
def add_ten(ns):
    """Add ten to each of the numbers in a list.
    This function modifies its argument."""
    i = 0
    while i < len(ns):
        ns[i] = ns[i] + 10
        i = i + 1

lst = [2, 4, 6]
print('add_ten returns', add_ten(lst))  # `add_one` is a fruitless function. It returns None.
print('lst =', lst)                     # lst has been modified.
```

{: class="nb-output"}

    add_ten returns None
    lst = [12, 14, 16]



Here's an implementation of the same specification, that uses `for` and `range`:


```python
def add_ten(ns):
    for i in range(len(ns)):
        ns[i] = ns[i] + 10

lst = [2, 4, 6]
print('add_ten returns', add_ten(lst))  # `add_one` is a fruitless function. It returns None.
print('lst =', lst)                     # lst has been modified.
```

{: class="nb-output"}

    add_ten returns None
    lst = [12, 14, 16]



A third implementation, with `for` and `enumerate`:


```python
def add_ten(ns):
    for i, n in enumerate(ns):
        ns[i] = n + 10

lst = [2, 4, 6]
print('add_ten returns', add_ten(lst))  # `add_one` is a fruitless function. It returns None.
print('lst =', lst)                     # lst has been modified.
```

{: class="nb-output"}

    add_ten returns None
    lst = [12, 14, 16]



### A map that creates a new list

`add_ten`, above, modifies its argument. It's like `chop` from the reading journal, or like `lst.sort()` from the Python standard library.

`added_ten`, below, constructs a new list. It's like `middle` from the reading journal, or like `sorted(lst)` from the Python standard library.

Code that constructs a new list generally uses an *accumulator* to collect the new values into,
and includes these stages:
* *Initializing* the accumulator
* *Modifying* the accumulator (adding or extending it with new values)
* *Returning* the accumulated values

These stages are labelled below.


```python
def added_ten(ns):
    """Add ten to each of the numbers in the list of numbers `xs`.
    This function returns a new list."""
    result = []                # initialize the accumulator
    for n in ns:
        result.append(n + 10)  # modify the accumulator
    return result              # return the accumulated value

lst = [2, 4, 6]
print('added_ten returns', added_ten(lst))  # `add_one` returns a new list
print('lst =', lst)                         # lst is unchanged
```

{: class="nb-output"}

    added_ten returns [12, 14, 16]
    lst = [2, 4, 6]



### The `map` function

Mapping is such a common operation that the Python library provides a standard function for it.

This function takes another function as its argument.

First, let's see what looks like to separate the code that adds ten out from the code that iterates over the items in the list. (We have **factored** `increment_by_ten` out from `added_ten`.)


```python
def increment_by_ten(n):
    return n + 10

def added_ten(ns):
    result = []                             # initialize the accumulator
    for n in range(len(ns)):
        result.append(increment_by_ten(n))  # modify the accumulator
    return result                           # return the accumulated value

lst = [2, 4, 6]
print('added_ten returns', added_ten(lst))
```

{: class="nb-output"}

    added_ten returns [10, 11, 12]



Now, we'll replace the accumulator and the `for` loop by `map`. (We're using the definition of `increment_by_ten` from above.)


```python
def added_ten(ns):
    return list(map(increment_by_ten, ns))

print('added_ten returns', added_ten(lst))  # `add_one` returns a new list
```

{: class="nb-output"}

    added_ten returns [12, 14]



(You may recall that `range` returns a list-like value, that we apply the `list` function to it in order to turn it into an actual list so that we can see its values. Similarly, `map` returns a list-like value. We apply the `list` function to it in order to see its values.)

#### `for` and `map`: a connection

The `for` statement replaces a number of different statements: that initialize, test, use, and increment the *loop variable*. With `for`, Python handles this for us automatically.

Similarly, the `map` function replaces a number of different statements: that initialize, modify, and return the *accumulator variable*.

### List Comprehensions

You may be familiar with ["set builder" notation](https://en.wikipedia.org/wiki/Set-builder_notation) from math:

$$\{n + 10 \mid n \in \{2, 4, 6\}\}$$
$$\{n + 10 : n \in \{2, 4, 6\}\}$$

These are two different ways of writing: the set of numbers $\{n + 10\}$, for $n$ from $\{2, 4, 6\}$. (This set is equal to $\{12, 14, 16\}$.)

Python provides **set comprehensions** (we'll learn about Python sets later). The following set comprehension is equal to the Python set `{12, 14, 16}`: 

```python
{n + 10 for n in {2, 4, 6}}
```

The Python list **list comprehension** is similar, but produces a list instead of a set:

```python
[n + 10 for n in {2, 4, 6}]
```

Here's an implementation of `map` using a list comprehension:


```python
def added_ten(ns):
    return [n + 10 for n in ns]

print(added_ten([10, 20, 30, 40]))
```

{: class="nb-output"}

    [20, 30, 40, 50]



# Filter

*Filtering* returns a list that contains only some items from the original list.

We will only work with implementations that create a new list. See [this Stack Overflow question](https://stackoverflow.com/questions/10665591/how-to-remove-list-elements-in-a-for-loop-in-python) for a discussion of some of the pitfalls with trying to delete items from a list from inside a `for` loop.

Note: you will need to implement your own `is_even` function that returns `True` or `False`


```python
def evens(ns):
    result = []              # initialize the accumulator
    for n in ns:
        if is_even(n):
            result.append(n)  # modify the accumulator
    return result             # return the accumulated value

evens([1, 2, 3, 4])
```

{: class="nb-output"}




    [2, 4]




Like mapping and `map`, Python provides a built-in function for filtering.


```python
def evens(ns):
    return list(filter(is_even, ns))

evens([1, 2, 3, 4])
```

{: class="nb-output"}




    [2, 4]




There is also a list comprehension form of filter.

Compare:

* Math set builder notation: $\{n : n \in \{2, 4, 6\}, \text{is_even}(n)\}$
* Python set comprehension: `{n for n in {2, 4, 6} if is_even(n)}`
* Python list comprehension:  `[n for n in [2, 4, 6] if is_even(n)]`


```python
def evens(ns):
    return [n for n in ns if is_even(n)]

evens([1, 2, 3, 4])
```

{: class="nb-output"}




    [2, 4, 6]




## Reduce

The _reduce_ pattern combines the items in a list into a single value.


```python
def my_sum(ns):
    a = 0          # initialize accumulator
    for n in ns:
        a = a + n  # modify the accumulator
    return a       # return the accumulated value

my_sum([2, 4, 6])
```

{: class="nb-output"}




    12




Unlike mapping and filtering, reduction does not have a list comprehension equivalent.

Also, you have to import the `reduce` function from the [functools module](https://docs.python.org/3/library/functools.html).

Like `map` and `filter`, `reduce` takes a function argument. We'll create an `add` helper function to pass to it.


```python
import functools

def add(a, b):
    return a + b

def my_sum(ns):
    return functools.reduce(add, ns)

my_sum([2, 4, 6])
```

{: class="nb-output"}




    12




Instead of writing our implementation of `add`, we could use the [operator module](https://docs.python.org/3.5/library/operator.html) to get a Python *function* that acts like the `+` *operator*.


```python
import functools
import operator

def my_sum(ns):
    return functools.reduce(operator.add, ns)

my_sum([2, 4, 6])
```

{: class="nb-output"}




    12



