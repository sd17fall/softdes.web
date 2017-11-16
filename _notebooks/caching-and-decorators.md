---
date: 2017-11-13T17:59:30-05:00
source: notebooks/caching-and-decorators.ipynb
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

`fib` is a *recursive* function. A single *external* call to `fib` can result in lots of *recursive* calls, where it calls itself.

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



The number of calls increases (exponentially) as a function of the argument:


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



The fact that it calls itself so many times has a direct affect on performance:


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

Let's instrument the function to print each time it's called. This way we that we can see more about what's going on.


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




This output shows that `fib` is called multiple times with the same arguments. For example, `fib(4)` is called a couple times. `fib(3)` is being called three times. `fib(2)` is called *five* times.

The modified instrumentation below report how many times `fib` is applied to each argument value. (This is also a chance to learn about [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict).)


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



### A Digression

You might notice an interesting pattern in the sequence of call counts, above. Reading from the bottom (`fib(6)`), and skipping `fib(1)`, the number of times `fib` is called with each argument value from $6$ down to $2$ is $1, 1, 2, 3, 5$.

Let's see if this holds up:


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



Note the sequence: `fib` applied to $12, 11, 10, \ldots, 4, 3, 2$ is $1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89$. What does this sequence remind you of? Harder: why does it happen?

## Caching

Instead of *instrumenting* the code, to simply record how many times the function was called, we can modify it to *cache* the computation, and use this cached value.

This is the same technique that we used to cache web requests, in the Text Mining project. There it avoided repeated *network requests*. Here it saves repeated *computation*. This reduces the function's **computational complexity**.


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

Let's separate the first instrumented `fib`, that counts how often it's been called, into two functions. The *inner* function, `fib_`, does the computation. The *outer* function, `fib`, *wraps* `fib_`. It adds the instrumentation.

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



We can change the outer function to add different instrumentation. We don't need to touch the inner function.


```python
from collections import defaultdict
counts = defaultdict(lambda: 0)

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



Now let's define a different outer function, that adds caching. (We'll also keep some instrumentation, so we can see that the cache is working.) It can use the same inner function.


```python
count = 0
fib_cache = {}

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

The various out functions above – all named `fib` – didn't need to know anything about `fib_` specifically. The *name* `fib_` was included in their definitions, but they otherwise could have wrapped any other (unary) function instead.

Let's extract `fib_` from the function definition, and instead supply it as a *parameter*:


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



Above, `def fib_` defined `fib`, `counting(fib)` used that value, and `fib = …` (on the same line) defined `fib`.

We don't need the value of `fib_` after we've used it as an argument to `counting`. We can therefore `def fib` instead of `def fib_`:


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

fib = counting(fib)

print("fib({}) = {}; fib was called {:,} times".format(10, fib(10), count))
```

{: class="nb-output"}

    fib(10) = 55; fib was called 109 times



This relieves us from have to come up separate names for `fib_` and `fib`.

It also eliminates the inelegance where `fib_` had to know to call `fib` (that hasn't been defined yet).

Previously, in order to recognize that `fib_` was actually recursive, we needed to know that `fib_` was going to be wrapped up and that the wrapped function would be called `fib`.

Now, you can read the functionality of `fib` straight from its definition. As a bonus, if we comment out the `fib = counting(fib)` line, `fib` still works – it just isn't instrumented.

We can wrap a function multiple times. `fib` below has been wrapped by a function (`counting`) that adds counting instrumentation ,and then wrapped in a function (`cached`) that adds caching. The final value of `fib` is a function that both records how many times it's been called, *and* is cached.


```python
count = 0

def cached(fn):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = fn(n)
        cache[n] = result
        return result
    return wrapper

def counting(fn):
    def wrapper(n):
        global count
        count += 1
        return fn(n)
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



Let's write one more wrapping function, for even more instrumentation:


```python
count = 0

def cached(fn):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = fn(n)
        cache[n] = result
        return result
    return wrapper

def counting(fn):
    def wrapper(n):
        global count
        count += 1
        return fn(n)
    return wrapper

def traced(fn):
    def wrapper(n):
        print('called {}({})'.format(fn.__name__, n))
        return fn(n)
    return wrapper

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

fib = traced(fib)
fib = counting(fib)
fib = cached(fib)

print("fib({}) = {}; fib was called {:,} times".format(10, fib(10), count))
```

{: class="nb-output"}

    called fib(10)
    called fib(8)
    called fib(6)
    called fib(4)
    called fib(2)
    called fib(3)
    called fib(1)
    called fib(5)
    called fib(7)
    called fib(9)
    fib(10) = 55; fib was called 10 times



Order matters! Above, the tracing wrapper is inside the wrapped the caching wrapper. Below, the tracing happens *outside* the cache.


```python
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

fib = cached(fib)
fib = counting(fib)
fib = traced(fib)

count = 0
print("fib({}) = {}; fib was called {:,} times".format(10, fib(10), count))
```

{: class="nb-output"}

    called wrapper(10)
    called wrapper(8)
    called wrapper(6)
    called wrapper(4)
    called wrapper(2)
    called wrapper(3)
    called wrapper(1)
    called wrapper(2)
    called wrapper(5)
    called wrapper(3)
    called wrapper(4)
    called wrapper(7)
    called wrapper(5)
    called wrapper(6)
    called wrapper(9)
    called wrapper(7)
    called wrapper(8)
    fib(10) = 55; fib was called 17 times



The functions that do the wrapping can be applied to any (unary) function. Here, we'll apply it to a version of the exponentiation function that's been modified to take a single argumen: a tuple of $(\textrm{base}, \textrm{exp})$: `pow((b, e))` $= b^e$.

(The forthcoming Appendix will show how to modify these wrappers for use on functions that take different numbers of arguments.)


```python
def pow(base_and_exp):
    base, exp = base_and_exp
    if exp == 0:
        return 1
    if exp == 1:
        return base
    half = exp // 2
    return pow((base, half)) * pow((base, exp - half))

pow = traced(pow)
pow = cached(pow)
print('exp({}, {}) = {}'.format(2, 15, pow((2, 15))))
```

{: class="nb-output"}

    called pow((2, 15))
    called pow((2, 7))
    called pow((2, 3))
    called pow((2, 1))
    called pow((2, 2))
    called pow((2, 4))
    called pow((2, 8))
    exp(2, 15) = 32768



### Terminology

A function that takes a function as an argument and returns a function as a value, is called a [**higher-order function**, **functor**, or **functional**](https://en.wikipedia.org/wiki/Higher-order_function).

Programming with higher-order functions is [**higher-order programming**](https://en.wikipedia.org/wiki/Higher-order_programming).

"Functor" and "functional" are also used in math, for meanings that aren't that different. For example, the (indefinite) integral $\int$ takes an function $x \rightarrow x^2 dx$ as an argument and returns another function $x \rightarrow 3/2 x^3$ as a value: $\int x^2 dx = 3/2 x^3$.

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

def cached(fn):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = fn(n)
        cache[n] = result
        return result
    return wrapper

def counting(fn):
    def wrapper(n):
        global count
        count += 1
        return fn(n)
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




```python
count = 0

def cached(fn):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = fn(n)
        cache[n] = result
        return result
    return wrapper

def counting(fn):
    def wrapper(n):
        global count
        count += 1
        return fn(n)
    return wrapper

def traced(fn):
    def wrapper(n):
        print('called {}({})'.format(fn.__name__, n))
        return fn(n)
    return wrapper

@cached
@counting
@traced
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print("fib({}) = {}; fib was called {:,} times".format(10, fib(10), count))
```

{: class="nb-output"}

    called fib(10)
    called fib(8)
    called fib(6)
    called fib(4)
    called fib(2)
    called fib(3)
    called fib(1)
    called fib(5)
    called fib(7)
    called fib(9)
    fib(10) = 55; fib was called 10 times



## Additional Reading

Glossary:

* [Python decorators](https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators)
* [Separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns)
* [Functional programming](https://en.wikipedia.org/wiki/Functional_programming)
* [Higher-order function](https://en.wikipedia.org/wiki/Higher-order_function)
* [Higher-order programming](https://en.wikipedia.org/wiki/Higher-order_programming)

Tutorials:

* [Primer on Python decorators](https://realpython.com/blog/python/primer-on-python-decorators/), _Real Python_.
* [A guide to Python's function decorators](https://www.thecodeship.com/patterns/guide-to-python-function-decorators/), _The Code Ship_, Ayman Farhat.
* [Decorators](http://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html), _Python 3 Patterns, Recipes and Idioms_.

## Appendix: Variadic Decorators

The following higher-order functions apply to functions that take any number of arguments.


```python
count = 0

def cached(fn):
    cache = {}
    def wrapper(*args):
        if n in cache:
            return cache[args]
        result = fn(*args)
        cache[args] = result
        return result
    return wrapper

def counting(fn):
    def wrapper(*args):
        global count
        count += 1
        return fn(*args)
    return wrapper

def traced(fn):
    def wrapper(*args):
        print('called {}({})'.format(fn.__name__, ', '.join(map(str, args))))
        return fn(*args)
    return wrapper
```

They can be used on `fib`, which has a single parameter:


```python
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

fib = traced(fib)
fib = counting(fib)
fib = cached(fib)

print("fib({}) = {}; fib was called {:,} times".format(10, fib(10), count))
```

{: class="nb-output"}

    called fib(10)
    called fib(8)
    called fib(6)
    called fib(4)
    called fib(2)
    called fib(3)
    called fib(1)
    called fib(2)
    called fib(5)
    called fib(3)
    called fib(1)
    called fib(2)
    called fib(4)
    called fib(2)
    called fib(3)
    called fib(1)
    called fib(2)
    called fib(7)
    called fib(5)
    called fib(3)
    called fib(1)
    called fib(2)
    called fib(4)
    called fib(2)
    called fib(3)
    called fib(1)
    called fib(2)
    called fib(6)
    called fib(4)
    called fib(2)
    called fib(3)
    called fib(1)
    called fib(2)
    called fib(5)
    called fib(3)
    called fib(1)
    called fib(2)
    called fib(4)
    called fib(2)
    called fib(3)
    called fib(1)
    called fib(2)
    called fib(9)
    called fib(7)
    called fib(5)
    called fib(3)
    called fib(1)
    called fib(2)
    called fib(4)
    called fib(2)
    called fib(3)
    called fib(1)
    called fib(2)
    called fib(6)
    called fib(4)
    called fib(2)
    called fib(3)
    called fib(1)
    called fib(2)
    called fib(5)
    called fib(3)
    called fib(1)
    called fib(2)
    called fib(4)
    called fib(2)
    called fib(3)
    called fib(1)
    called fib(2)
    called fib(8)
    called fib(6)
    called fib(4)
    called fib(2)
    called fib(3)
    called fib(1)
    called fib(2)
    called fib(5)
    called fib(3)
    called fib(1)
    called fib(2)
    called fib(4)
    called fib(2)
    called fib(3)
    called fib(1)
    called fib(2)
    called fib(7)
    called fib(5)
    called fib(3)
    called fib(1)
    called fib(2)
    called fib(4)
    called fib(2)
    called fib(3)
    called fib(1)
    called fib(2)
    called fib(6)
    called fib(4)
    called fib(2)
    called fib(3)
    called fib(1)
    called fib(2)
    called fib(5)
    called fib(3)
    called fib(1)
    called fib(2)
    called fib(4)
    called fib(2)
    called fib(3)
    called fib(1)
    called fib(2)
    fib(10) = 55; fib was called 218 times



But unlike the original higher-order functions, they can also be used with a more natural definition of `pow`, that has *two* parameters:


```python
def pow(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    half = exp // 2
    return pow(base, half) * pow(base, exp - half)

pow = traced(pow)
pow = counting(pow)
pow = cached(pow)

print('exp({}, {}) = {}'.format(2, 15, pow(2, 15)))
```

{: class="nb-output"}

    called pow(2, 15)
    called pow(2, 7)
    called pow(2, 3)
    called pow(2, 1)
    called pow(2, 2)
    called pow(2, 1)
    called pow(2, 1)
    called pow(2, 4)
    called pow(2, 2)
    called pow(2, 1)
    called pow(2, 1)
    called pow(2, 2)
    called pow(2, 1)
    called pow(2, 1)
    called pow(2, 8)
    called pow(2, 4)
    called pow(2, 2)
    called pow(2, 1)
    called pow(2, 1)
    called pow(2, 2)
    called pow(2, 1)
    called pow(2, 1)
    called pow(2, 4)
    called pow(2, 2)
    called pow(2, 1)
    called pow(2, 1)
    called pow(2, 2)
    called pow(2, 1)
    called pow(2, 1)
    exp(2, 15) = 32768



And like the original higher-order functions, these new functionals can also be used as decorators:


```python
@cached
@counting
@traced
def pow(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    half = exp // 2
    return pow(base, half) * pow(base, exp - half)

print('exp({}, {}) = {}'.format(2, 15, pow(2, 15)))
```

{: class="nb-output"}

    called pow(2, 15)
    called pow(2, 7)
    called pow(2, 3)
    called pow(2, 1)
    called pow(2, 2)
    called pow(2, 1)
    called pow(2, 1)
    called pow(2, 4)
    called pow(2, 2)
    called pow(2, 1)
    called pow(2, 1)
    called pow(2, 2)
    called pow(2, 1)
    called pow(2, 1)
    called pow(2, 8)
    called pow(2, 4)
    called pow(2, 2)
    called pow(2, 1)
    called pow(2, 1)
    called pow(2, 2)
    called pow(2, 1)
    called pow(2, 1)
    called pow(2, 4)
    called pow(2, 2)
    called pow(2, 1)
    called pow(2, 1)
    called pow(2, 2)
    called pow(2, 1)
    called pow(2, 1)
    exp(2, 15) = 32768


