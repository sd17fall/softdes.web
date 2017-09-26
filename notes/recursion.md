

{% include toc %}


# Recursion Notes

## I. Counting Codons

How many codons are there? That, is how many nucleotide sequences have length three – how many ways are there of combining three nucleotides , each independently drawn from the set $\{A, C, T, G\}$. For example, `ATG`, `CAT`, and `GAG` are three-nucleotide codons; `DOG` is not (`D` and `O` are not nucleotides); neither is `CATATG` (it has length 6, not 3).

### Analysis

There are three positions. The nucleotide at each position is selected *independently* of the nucleotides at any other position. There's four ways of choosing the first position, and four ways of choosing the second position, and four ways of choosing the third position, so (handwave) there's $4 \times 4 \ times 4 = 64$ ways of filling all three positions.

More generally, there's $4^n$ ways of filling the $n$ positions in a $n$-nucleotide sequence.

(Quick check: is it $4^n$ or $n^4$? Which one works when $n = 1$?)


```python
def C(n):
    return 4 ** n

print(C(0))
print(C(1))
print(C(3))
```

{: class="nb-output"}

    1
    4
    64



Let's make this a bit less handwave-y:

There's four possibilities for the first position: `A`, `C`, `T`, `G`.

For each of these first-position possibilities, there's *another* four possibilities for the second position, for a total of $4 \times 4 = 16$. For example, `A` can be extended to `AA`, `AC`, `AT`, and `AG`, giving a total of four 2-nucleotide sequences just starting with `A`.

Each of these 2-nucleotide sequences can be extended in four different ways, for a total of $16 \times 4 = 64$. For example, `AT` extends to `ATA`, `ATC`, `ATG`, and `ATT`.

Generalizing this, there are $4^n$ $n$-nucleotide sequences.


```python
def C(n):
    a = 1
    for i in range(n):
        a = a * 4
    return a
    
print(C(0))
print(C(1))
print(C(3))
```

{: class="nb-output"}

    1
    4
    64




## Analysis, with Induction

Here's another way of analyzing the problem.

If you're already familiar with **induction** from math, this may help you relate recursion to what you already know.

if you're *not* familiar with induction from math, this is not the best introduction.

Let $C_n$ denote the number of $n$-length sequences.

There are four single-nucleotide sequences: the single-nucleotide sequences `A`, `C`, `T`, and `G`. Therefore $C_1 = 4$.

There are $C_2 = 16$ two-nucleotide sequences. There are four possibilities for the first nucleotide; independently, there are four possibiities for the second nucleotide. $4 \times 4 = 16$.

There are $C_3 = 64$ three-nucleotide sequences. A three-nucleotide sequence is a two-nucleotide subsequence followed by a single nucleotide. We already know there's 16 possible choices for the two-nucleotide subsequence. Each of those 16 possibilities can be followed by any of four nucleotides, for a total of $16 \times 4 = 64$.

In general, $C_{n+1} = C_n \times 4$.

We can go back a step, too. There's only one zero-nucleotide sequence: the empty sequence. Therefore, $C_0 = 1$. $C_1 = C_0 \times 4 = 1 C \times 4 = 4$ – the pattern works!

This gives us the following **recurrence** relation:

$$\begin{eqnarray}
C_0 &=& 0 \\
C_{n+1} &=& C_n \times 4
\end{eqnarray}$$

Here's four equivalent ways to implement (math) **recurrence** relationship, using (programming) **recursion**:


```python
def C(n):
    if n == 0:
        return 1
    return C(n - 1) * 4
    
print(C(0))
print(C(1))
print(C(3))
```

{: class="nb-output"}

    1
    4
    64




```python
def C(n):
    if n == 0:
        return 1
    else:
        return C(n - 1) * 4
    
print(C(0))
print(C(1))
print(C(3))
```

{: class="nb-output"}

    1
    4
    64




```python
def C(n):
    if n > 0:
        return C(n - 1) * 4
    return 1
    
print(C(0))
print(C(1))
print(C(3))
```

{: class="nb-output"}

    1
    4
    64




```python
def C(n):
    return 1 if n == 0 else C(n - 1) * 4
    
print(C(0))
print(C(1))
print(C(3))
```

{: class="nb-output"}

    1
    4
    64



And here's a couple of common mistakes, and their symptom. See if you can spot the problems in the code.


```python
def C(n):
    return C(n - 1) * 4

print(C(0))
print(C(1))
print(C(3))
```

{: class="nb-output"}


    ----------------------------------------------------------------------

    RecursionError                       Traceback (most recent call last)

    <ipython-input-5-936cf6aa9c0d> in <module>()
          2     return C(n - 1) * 4
          3 
    ----> 4 print(C(0))
          5 print(C(1))
          6 print(C(3))


    <ipython-input-5-936cf6aa9c0d> in C(n)
          1 def C(n):
    ----> 2     return C(n - 1) * 4
          3 
          4 print(C(0))
          5 print(C(1))


    ... last 1 frames repeated, from the frame below ...


    <ipython-input-5-936cf6aa9c0d> in C(n)
          1 def C(n):
    ----> 2     return C(n - 1) * 4
          3 
          4 print(C(0))
          5 print(C(1))


    RecursionError: maximum recursion depth exceeded




```python
def C(n):
    if n > 0:
        return C(n) * 4
    return 1


print(C(0))
print(C(1))
print(C(3))
```

{: class="nb-output"}

    1



    ---------------------------------------------------------------------------

    RecursionError                            Traceback (most recent call last)

    <ipython-input-5-779879d3e859> in <module>()
          6 
          7 print(C(0))
    ----> 8 print(C(1))
          9 print(C(3))


    <ipython-input-5-779879d3e859> in C(n)
          1 def C(n):
          2     if n > 0:
    ----> 3         return C(n) * 4
          4     return 1
          5 


    ... last 1 frames repeated, from the frame below ...


    <ipython-input-5-779879d3e859> in C(n)
          1 def C(n):
          2     if n > 0:
    ----> 3         return C(n) * 4
          4     return 1
          5 


    RecursionError: maximum recursion depth exceeded in comparison



## II. Binary Tree
`build_binary_tree` builds a [binary tree](https://en.wikipedia.org/wiki/Binary_tree) of depth (or height) $n$. You can look at the output to see what is meant by "binary tree", and how it's represented.


```python
def build_binary_tree(n):
    if n == 0:
        return 1
    return [build_binary_tree(n - 1), build_binary_tree(n - 1)]

print(build_binary_tree(0))
print(build_binary_tree(1))
print(build_binary_tree(2))
print(build_binary_tree(3))
```

{: class="nb-output"}

    1
    [1, 1]
    [[1, 1], [1, 1]]
    [[[1, 1], [1, 1]], [[1, 1], [1, 1]]]



Here's a slight variant, that makes *unbalanced* trees, where the left branch is deeper than the right branch.


```python
def build_binary_tree(n):
    if n == 0:
        return 1
    return [build_binary_tree(n - 1), build_binary_tree(max(n - 2, 0))]

print(build_binary_tree(0))
print(build_binary_tree(1))
print(build_binary_tree(2))
print(build_binary_tree(3))
```

{: class="nb-output"}

    1
    [1, 1]
    [[1, 1], 1]
    [[[1, 1], 1], [1, 1]]


