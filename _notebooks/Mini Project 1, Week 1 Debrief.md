---
date: 2018-02-06T13:12:54-05:00
source: notebooks/Mini Project 1, Week 1 Debrief.ipynb
---

{% include toc %}


#  Debrief on Mini Project 1, Week 1

This notebook goes over some of the most common areas for improvement that we saw on the first half of the mini project.  Lots of folks had correct code, but we have some suggestions for making the code more succinct / clear / efficient.

##  When to use `for` versus `while` loops

Lots of folks are switching over to using the `for` loop instead of the `while` loop.  Both can be used to write correct code, however, the `for` loop's more structured nature generally makes it clearer.  For instance
```
for i in range(len(dna)):
    # some code
```
is more readable and less error prone than
```
i = 0
while i < len(dna):
    # some code
    i += 1
```

One instance where a lot of people used `while` loops in a way that was preferable to using `for` loops is in the `find_all_ORFs_oneframe`.  In that function you have to change the index you are iterating over based on the length of the last ORF you found.  Why would this be hard to do with a `for` loop?

## Iteration Tricks

We're already going to be learning some more iteration tricks today in class, however, two such tricks that came up repeatedly in the context of this assignment had to do with iterating through a collection in reverse order and striding through a collection in multiples of 3 (e.g., to read each codon).

### Iterating in reverse

Here are two approaches to iterating backwards through a string.
```
for i in range(len(dna)-1, -1, -1):
    # do something with dna[i]
```

The next one uses the handy `reversed` function, which reverses a collection.
```
for i in reversed(range(len(dna))):
    # do something with dna[i]
```

Why might the second approach be better?

### Using Slices

We saw a lot of cases where slices would have made the code much more readable.  For example,

```
for i in range(0, len(dna), len(dna)-2):
    if dna[i] == 'A' and dna[i+1] == 'T' and dna[i+2] == 'G':
        # found the start codon
```

A much more succinct way to do this is
```
for i in range(0, len(dna), len(dna)-2):
    if dna[i:i+3] == 'ATG':
        # found the start codon
```

### Make use of stride lengths

The issue of how to deal with looping through codons is a tricky one.  For one thing, you have to be sure that you are in frame when searching for stop or start codons.  This resulted in code like the following:

```
for i in range(len(dna)):
    if i % 3 == 0 and dna[i:i+3] == 'TAG':
        # found an in frame stop codon
```

By using the `range` function's built-in stride length parameter, you can avoid the unecessary check that `i` is a multiple of 3.

```
for i in range(0, len(dna), 3):
    if dna[i:i+3] == 'TAG':
        # found an in frame stop codon
```

## Careful with variables

There were quite instances of suboptimal practices with variables.

### Choosing good variable names

Some common pitfalls that we saw.
1.  Using the variable `i` in a way other than as an index being iterated over.
2.  Choosing one letter variable names that weren't semantically meaningful (e.g., `a = dna[1:]` instead of `shifted_dna = dna[1:]`).
3.  Using Hungarian notation by calling variables things like `list_1`, `list_2`, etc.
4.  Choosing variable names that conflict with built-in Python functions or types.

### Unnecessarily defining temporary variables

Lots of people defined temporary variables that were unnecessary.  A very common one that we saw was the following.

```
length = len(dna)
```
While this seems good at first blush, you have to ask yourself what the tradeoffs are for doing this.  On the positive side, you may think that this is more efficient computationally, however, that's not likely to be the case.  On the downside you have taken something that all Python programmers understand (that `len(dna)` is the number of elements in `dna`) and made it more difficult to understand (e.g., whenever you see `length` in the code, you will have to think through what length it is referring to).

## Careful with Commenting

While we gave you docstrings for all of the functions you had to implement, there were many cases where people could have used more inline commenting.  Of course there are many functions that are self-documenting (meaning that they are so clear that they wouldn't need comments explaining their structure).  However, there were some where the logical flow of the program was very hard to follow and no comments were given to help the reader.

## A note about computational efficiency and `get_reverse_complement`

There were quite a few approaches to getting the reverse complement of a DNA sequence.  The following approaches are both correct, but one is more computationally efficient than the other.  We will show some results of timing each of these approaches.


```python
import doctest

def get_complement(nucleotide):
    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'G':
        return 'C'
    if nucleotide == 'C':
        return 'G'

def reverse_complement_method_1(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
            dna: a DNA sequence represented as a string
            returns: the reverse complementary DNA sequence represented as a string
        >>> reverse_complement_method_1("ATGCCCGCTTT")
        'AAAGCGGGCAT'
        >>> reverse_complement_method_1("CCGCGTTCA")
        'TGAACGCGG'
    """
    reverse_complement = ''
    for n in dna:
        reverse_complement = get_complement(n) + reverse_complement
    return reverse_complement

def reverse_complement_method_2(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
            dna: a DNA sequence represented as a string
            returns: the reverse complementary DNA sequence represented as a string
        >>> reverse_complement_method_2("ATGCCCGCTTT")
        'AAAGCGGGCAT'
        >>> reverse_complement_method_2("CCGCGTTCA")
        'TGAACGCGG'
    """
    reverse_complement = []
    for n in reversed(dna):
        reverse_complement.append(get_complement(n))
    return ''.join(reverse_complement)

import doctest
doctest.testmod()
```

{: class="nb-output"}




    TestResults(failed=0, attempted=4)




We can now benchmark these against both short and long sequences of DNA.


```python
from random import choice

random_short_dna = [choice(['A','T','G','C']) for _ in range(100)]
%timeit reverse_complement_method_1(random_short_dna)
%timeit reverse_complement_method_2(random_short_dna)

random_long_dna = [choice(['A','T','G','C']) for _ in range(200000)]
%timeit reverse_complement_method_1(random_long_dna)
%timeit reverse_complement_method_2(random_long_dna)
```

{: class="nb-output"}

    25.1 µs ± 1.31 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    25.1 µs ± 908 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    1.37 s ± 52.9 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    48.8 ms ± 1.29 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)


