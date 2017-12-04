---
date: 2017-12-04T17:06:26-05:00
source: notebooks/advent-of-code.ipynb
---

{% include toc %}


# Advent of Code sampler

Here are some solutions to [Advent of Code Day 4 part 1](http://adventofcode.com/2017/day/4):

> A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.
>
> To ensure security, a valid passphrase must contain no duplicate words.
>
> For example:
>
> aa bb cc dd ee is valid.<br/>
> aa bb cc dd aa is not valid - the word aa appears more than once.<br/>
> aa bb cc dd aaa is valid - aa and aaa count as different words.

## Solutions from Class

These use different data structs (`list`, `set`, `dict`) to keep track of what's been seen before.


```python
def valid(passphrase):
    seen = dict()
    for w in passphrase.split():
        if w in seen:
            return False
        seen[w] = True
    return True

def valid(passphrase):
    seen = set()
    for w in passphrase.split():
        if w in seen:
            return False
        seen.add(w)
    return True

def valid(passphrase):
    seen = []  # or seen = list(), for greater similarity with the above
    for w in passphrase.split():
        if w in seen:
            return False
        seen.append(w)
    return True

def valid(passphrase):
    words = passphrase.split()
    return len(words) == len(set(words))

print(valid('aa bb cc dd ee'), True)
print(valid('aa bb cc dd aa'), False)
print(valid('aa bb cc dd aaa'), True)
```

{: class="nb-output"}

    True True
    False False
    True True



## Other Approaches

The following approaches aren't used in class. They count the number of occurrences.

This is better if you think you might need to know the counts later; otherwise, it's extra work.


```python
def valid(passphrase):
    counts = dict()
    for w in passphrase.split():
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1
    for n in counts.values():
        if n > 1:
            return False
    return True

def valid(passphrase):
    counts = dict()
    for w in passphrase.split():
        counts[w] = counts.get(w, 0) + 1
    return not any(n > 1 for n in counts.values())

print(valid('aa bb cc dd ee'), True)
print(valid('aa bb cc dd aa'), False)
print(valid('aa bb cc dd aaa'), True)
```

{: class="nb-output"}

    True True
    False False
    True True



The last definition can be simplified by [defaultdict](https://docs.python.org/3/library/collections.html).


```python
from collections import defaultdict

def valid(passphrase):
    counts = defaultdict(lambda: 0)
    for w in passphrase.split():
        counts[w] += 1
    return all(n == 1 for n in counts.values())

print(valid('aa bb cc dd ee'), True)
print(valid('aa bb cc dd aa'), False)
print(valid('aa bb cc dd aaa'), True)
```

{: class="nb-output"}

    True True
    False False
    True True



The [defaultdict](https://docs.python.org/3/library/collections.html) class simplifies it further.


```python
from collections import Counter

def valid(passphrase):
    counts = Counter()
    for w in passphrase.split():
        counts.update([w])
    return not any(n > 1 for n in counts.values())

def valid(passphrase):
    counts = Counter()
    counts.update(passphrase.split())
    return all(n == 1 for n in counts.values())

def valid(passphrase):
    counts = Counter(passphrase.split())
    return all(n == 1 for n in counts.values())

def valid(passphrase):
    counts = set(Counter(passphrase.split()).values())
    return counts == {} or counts == {1}

print(valid('aa bb cc dd ee'), True)
print(valid('aa bb cc dd aa'), False)
print(valid('aa bb cc dd aaa'), True)
```

{: class="nb-output"}

    True True
    False False
    True True


