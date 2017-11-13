---
date: 2017-11-13T17:59:30-05:00
omit_title: true
---

{% include toc %}


# Caching and Decorators

## Instrumentation

Consider the lowly Fibonacci function:


```python
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

fib(10)
```

{: class="nb-output"}




    55




This function is a straightforward translation of

$$F(n)=\left\{
                \begin{array}{ll}
                  1&n <= 2\\
                  F_{n-2} + F_{n-1}&n>2
                \end{array}
              \right.$$

`fib` is a recursive function, so a single *external* call to `fib` can result in lots of *recursive* calls, where it calls itself.

Let's **instrument** `fib`, to report how many calls result from a single external call:


```python
count = 0

def fib(n):
    global count
    count += 1
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print("fib({}) = {}; fib was called {:,} times".format(10, fib(10), count))
```

{: class="nb-output"}

    fib(10) = 55; fib was called 109 times



The number of calls increases (exponentially) as a function of the argument.:


```python
count = 0

def fib(n):
    global count
    count += 1
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

for i in [1, 2, 3, 4, 5, 10, 20, 30]:
    count = 0
    print("fib({}) = {}; fib was called {:,} times".format(i, fib(i), count))
```

{: class="nb-output"}

    fib(1) = 1; fib was called 1 times
    fib(2) = 1; fib was called 1 times
    fib(3) = 2; fib was called 3 times
    fib(4) = 3; fib was called 5 times
    fib(5) = 5; fib was called 9 times
    fib(10) = 55; fib was called 109 times
    fib(20) = 6765; fib was called 13,529 times
    fib(30) = 832040; fib was called 1,664,079 times



This large number of calls has a direct affect on performance:


```python
%timeit fib(10)
%timeit fib(20)
%timeit fib(30)
```

{: class="nb-output"}

    10000 loops, best of 3: 25.9 µs per loop
    100 loops, best of 3: 3.22 ms per loop
    1 loop, best of 3: 414 ms per loop



Note the microseconds (µs) and milliseconds (ms) per loop. 500 ms is half a second, so it's getting pretty slow.

Let's **instrument** the function to print each time it's called, so that we can see more about what's going on:


```python
def fib(n):
    print("Calling fib({})".format(n))
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

fib(6)
```

{: class="nb-output"}

    Calling fib(6)
    Calling fib(4)
    Calling fib(2)
    Calling fib(3)
    Calling fib(1)
    Calling fib(2)
    Calling fib(5)
    Calling fib(3)
    Calling fib(1)
    Calling fib(2)
    Calling fib(4)
    Calling fib(2)
    Calling fib(3)
    Calling fib(1)
    Calling fib(2)





    8




This output shows that `fib` is called multiple times with the same arguments. `fib(4)` is called a couple times. `fib(3)` is being called three times. `fib(2)` is called *five* times.

Here's modified instrumentation (and a chance to learn about [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict)), to report how many times `fib` is applied to each argument value:


```python
from collections import defaultdict
counts = defaultdict(lambda: 0)

def fib(n):
    counts[n] += 1
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

fib(6)

for n, count in sorted(counts.items()):
    print("fib({}) was called {} times".format(n, count))
```

{: class="nb-output"}

    fib(1) was called 3 times
    fib(2) was called 5 times
    fib(3) was called 3 times
    fib(4) was called 2 times
    fib(5) was called 1 times
    fib(6) was called 1 times



(A digression: you might notice an interesting pattern in the sequence of call counts. Let's see if it holds up:)


```python
counts = defaultdict(lambda: 0)
fib(12)
for n, count in sorted(counts.items()):
    print("fib({}) was called {} times".format(n, count))
```

{: class="nb-output"}

    fib(1) was called 55 times
    fib(2) was called 89 times
    fib(3) was called 55 times
    fib(4) was called 34 times
    fib(5) was called 21 times
    fib(6) was called 13 times
    fib(7) was called 8 times
    fib(8) was called 5 times
    fib(9) was called 3 times
    fib(10) was called 2 times
    fib(11) was called 1 times
    fib(12) was called 1 times



## Caching

Instead of *instrumenting* the code, to simply record how many times the function was called, we can modify it to *cache* the computation, and use this cached value.

This is exactly the same technique as caching web requests, for Text Mining. Here it saves repeated *computation*. (There it avoided repeated *network requests*.) This reduces the function's **computational complexity**.


```python
fib_cache = {}
count = 0

def fib(n):
    global count
    if n in fib_cache:
        return fib_cache[n]
    count += 1
    if n <= 2:
        return 1
    else:
        result = fib(n-2) + fib(n-1)
        fib_cache[n] = result
        return result

print("fib({}) = {}; fib was computed {} times".format(10, fib(10), count))
```

{: class="nb-output"}

    fib(10) = 55; fib was computed 11 times



Compare this to the uncached `fib`, where `fib(10)` resulted in *109* calls to `fib`.

Savings are (exponentially) greater for greater values of $n$.

Let's re-run the timings. We'll time a wrapper for the cached `fib`, that resets `fib`'s cache each time.


```python
def rfib(n):
    global fib_cache
    fib_cache = {}
    return fib(n)

%timeit rfib(10)
%timeit rfib(20)
%timeit rfib(30)
```

{: class="nb-output"}

    100000 loops, best of 3: 5.04 µs per loop
    100000 loops, best of 3: 10.8 µs per loop
    100000 loops, best of 3: 17.6 µs per loop



For reference, the un-cached timings looked like this:

    10000 loops, best of 3: 25.9 µs per loop
    100 loops, best of 3: 3.22 ms per loop
    1 loop, best of 3: 414 ms per loop

## Separating concerns

The code above takes a step *forwards* in terms of performance, but *backwards* in legibility. Half of it is concerned with doing the math, and half of it is concerned with caching. It violated **separation of concerns**.

Let's separate the first instrumented `fib`, that counts how often it's been called, into two functions. `fib_` does the computation. `fib` *wraps* `fib_`, to add the instrumentation.

(The underscore in `fib_` is used in Python the same way a prime $'$ is used in math. `fib_` corresponds to $\textrm{fib}'$ or $F'$.)


```python
count = 0

def fib_(n):
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def fib(n):
    global count
    count += 1
    return fib_(n)

print("fib({}) = {}; fib was called {:,} times".format(10, fib(10), count))
```

{: class="nb-output"}

    fib(10) = 55; fib was called 109 times



We can change the wrapper to add different instrumentation, without changing the underlying function:


```python
from collections import defaultdict
counts = defaultdict(lambda: 0)

def fib_(n):
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def fib(n):
    global count
    counts[n] += 1
    return fib_(n)

fib(10)
for n, count in sorted(counts.items()):
    print("fib({}) was called {} times".format(n, count))
```

{: class="nb-output"}

    fib(1) was called 21 times
    fib(2) was called 34 times
    fib(3) was called 21 times
    fib(4) was called 13 times
    fib(5) was called 8 times
    fib(6) was called 5 times
    fib(7) was called 3 times
    fib(8) was called 2 times
    fib(9) was called 1 times
    fib(10) was called 1 times



Now let's define a wrapper that adds caching. (We'll also keep some instrumentation, so we can see that the cache is working.)


```python
count = 0
fib_cache = {}

def fib_(n):
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def fib(n):
    if n in fib_cache:
        return fib_cache[n]
    global count
    count += 1
    result = fib_(n)
    fib_cache[n] = result
    return result

print("fib({}) = {}; fib was called {:,} times".format(10, fib(10), count))
```

{: class="nb-output"}

    fib(10) = 55; fib was called 10 times



## Higher-Order Programming

The various wrapper `fib`s above didn't need to know anything about `fib_` specifically. They were written to know the name `fib_`, but they could have wrapped any other (unary) function instead.

Let's give these wrapper functions a parameter, which is the function to wrap:


```python
count = 0

def fib_(n):
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def counting(fn):
    def wrapper(n):
        global count
        count += 1
        return fn(n)
    return wrapper

fib = counting(fib_)

print("fib({}) = {}; fib was called {:,} times".format(10, fib(10), count))
```

{: class="nb-output"}

    fib(10) = 55; fib was called 109 times



Instead of defining `fib_` via `def`, and then defining `fib` via `fib = …`, we can define the function `def fib` and then replace its value.

This relieves us from have to come up with a separate name (`fib_`) for the unwrapped `fib`.

It also eliminates the inelegance where `fib_` had to know to call `fib` (that hasn't been defined yet), so that you needed to know that it was going to be wrapped before you could recognize that it was actually recursive.


```python
count = 0

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def counting(fn):
    def wrapper(n):
        global count
        count += 1
        return fn(n)
    return wrapper

fib = counting(fib_)

print("fib({}) = {}; fib was called {:,} times".format(10, fib(10), count))
```

{: class="nb-output"}

    fib(10) = 55; fib was called 109 times



We can wrap a function multiple times. `fib` below has been wrapped by the counting instrumentation, and then wrapped in a cache, so that it both collects its call count *and* is cached.


```python
count = 0

def counting(fn):
    def wrapper(n):
        global count
        count += 1
        return fn(n)
    return wrapper

def cached(fn):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = fn(n)
        cache[n] = result
        return result
    return wrapper

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

fib = counting(fib)
fib = cached(fib)

print("fib({}) = {}; fib was called {:,} times".format(10, fib(10), count))
```

{: class="nb-output"}

    fib(10) = 55; fib was called 10 times



## Decorator Syntax

`fib = counting(fib)` *after* `fib` has been defined, is equivalent to `@counting` written immediately *before* the function definition.

This is the [Python decorator](https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators) construct.


```python
count = 0

def counting(fn):
    def wrapper(n):
        global count
        count += 1
        return fn(n)
    return wrapper

@counting
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print("fib({}) = {}; fib was called {:,} times".format(10, fib(10), count))
```

{: class="nb-output"}

    fib(10) = 55; fib was called 109 times




```python
count = 0

def counting(fn):
    def wrapper(n):
        global count
        count += 1
        return fn(n)
    return wrapper

def cached(fn):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = fn(n)
        cache[n] = result
        return result
    return wrapper

@cached
@counting
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print("fib({}) = {}; fib was called {:,} times".format(10, fib(10), count))
```

{: class="nb-output"}

    fib(10) = 55; fib was called 10 times



## Additional Reading

* [Separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns)
* [Python decorators](https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators)
* [Primer on Python decorators](https://realpython.com/blog/python/primer-on-python-decorators/), _Real Python_.
* [A guide to Python's function decorators](https://www.thecodeship.com/patterns/guide-to-python-function-decorators/), _The Code Ship_, Ayman Farhat.
* [Decorators](http://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html), _Python 3 Patterns, Recipes and Idioms_.
