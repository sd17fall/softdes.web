

{% include toc %}


# GeneFinder solutions

Topics discussed:

* Adding minimal test cases
* Coding convention for fruitful functions that can return `None`
* Docstring style conventions (*not* used in the code that was given you)
* Doctesting functions that return `None`
* Global variables – when to use, how to name
* Naming conventions for placeholder variables
* Validating parameter values
* Upcoming material:
  * Dictionaries
  * Exceptions
* Advanced and optional topics:
  * List comprehensions
  * Regular expressions
  * Using `random.seed` to test functions that call `random`
 
 Also see [GeneFinder – going beyond](/notes/genefinder-going-beyond.md).

## `get_complement`

This section discusses some implementations of `get_complement`, that use a variety of different techniques.

I've also corrected the *wording* of the docstring, which said "complementary nucleotide nucleotide"; and the *style* – it's been modified to conform to the [numpy docstring style guide](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html). You weren't expected to do that, but it was bugging me.


```python
import doctest

def get_complement(nucleotide):
    """Return the complementary nucleotide
    
    Parameters
    ----------
    nucleotide : string
        A nucleotide (A, C, G, or T) represented as a string.
    
    Returns
    -------
    string
        The complementary nucleotide.

    Examples
    -------
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    """
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'

doctest.run_docstring_examples(get_complement, globals())
```

Since each branch of the `if` executes a `return` statement, `elif` could be replaced by `if`. This is neither better nor worse than the preceding implementation.

\[In the following function definitions, parts of the docstring have been omitted.\]


```python
import doctest

def get_complement(nucleotide):
    """
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    """
    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'C':
        return 'G'
    if nucleotide == 'G':
        return 'C'

doctest.run_docstring_examples(get_complement, globals())
```

### Exceptions

What does `get_complement` do when passed an invalid value, say `X`? The specification doesn't say.

The above implementations return `None`.

This satisfies the specification, and the doctests pass.

However, a bug in code that *calls* `get_complement` won't produce a visible error until some distance from the point where `get_complement` is called. (I'll discuss this more in class on Monday.)

Here's a technique for detecting the problem within `get_complement`, and stopping immediately with a stack trace. We'll use a trick: `invalid_nucleotide` isn't defined, and it's an error to call an undefined function.


```python
import doctest

def get_complement(nucleotide):
    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'C':
        return 'G'
    if nucleotide == 'G':
        return 'C'
    invalid_nucleotide()

get_complement('X')
```

{: class="nb-output"}


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-29-b7752a309d67> in <module>()
         12     invalid_nucleotide()
         13 
    ---> 14 get_complement('X')
    

    <ipython-input-29-b7752a309d67> in get_complement(nucleotide)
         10     if nucleotide == 'G':
         11         return 'C'
    ---> 12     invalid_nucleotide()
         13 
         14 get_complement('X')


    NameError: name 'invalid_nucleotide' is not defined



Soon you'll read about [exceptions](https://docs.python.org/3/tutorial/errors.html#raising-exceptions). These allow you to say what you mean instead of using a trick. Note the final `Exception` line in the output from the following code:


```python
import doctest

def get_complement(nucleotide):
    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'C':
        return 'G'
    if nucleotide == 'G':
        return 'C'
    raise Exception('Invalid nucleotide: {}'.format(nucleotide))

get_complement('X')
```

{: class="nb-output"}


    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    <ipython-input-28-044bac9e6f3f> in <module>()
         12     raise Exception('Invalid nucleotide: {}'.format(nucleotide))
         13 
    ---> 14 get_complement('X')
    

    <ipython-input-28-044bac9e6f3f> in get_complement(nucleotide)
         10     if nucleotide == 'G':
         11         return 'C'
    ---> 12     raise Exception('Invalid nucleotide: {}'.format(nucleotide))
         13 
         14 get_complement('X')


    Exception: Invalid nucleotide: X



If you really want to show off your Python expertise, read up on Python's [built-in exception types](https://docs.python.org/3.4/library/exceptions.html#concrete-exceptions). You'll discover a more specific exception than `Exception`, that's perfect for this purpose:


```python
import doctest

def get_complement(nucleotide):
    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'C':
        return 'G'
    if nucleotide == 'G':
        return 'C'
    raise ValueError('Invalid nucleotide: {}'.format(nucleotide))

get_complement('X')
```

{: class="nb-output"}


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-27-0126a11762bc> in <module>()
         23 
         24 doctest.run_docstring_examples(get_complement, globals())
    ---> 25 get_complement('X')
    

    <ipython-input-27-0126a11762bc> in get_complement(nucleotide)
         20     if nucleotide == 'G':
         21         return 'C'
    ---> 22     raise ValueError('Invalid nucleotide: {}'.format(nucleotide))
         23 
         24 doctest.run_docstring_examples(get_complement, globals())


    ValueError: Invalid nucleotide: X



### `get_complement` – other approaches

The implementation techniques above used "data-shaped code". One of the pieces of data in this case is the list of nucleotides (`A`, `C`, `T`, and `G`). (The other is the nucleotide we're taking the complement of.) The function contains an `if` or `elif` statement for each nucleotide. If you were to add another nucleotide, you'd have to add aother `if` statement.

The following approaches put the list of nucleotides into values instead of `if` statements.


```python
def get_complement(nucleotide):
    """
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """
    nucleotides = 'ATCG'
    complements = 'TAGC'
    i = nucleotides.index(nucleotide)
    return complements[i]

doctest.run_docstring_examples(get_complement, globals())
```


```python
def get_complement(nucleotide):
    """
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """
    nucleotides = 'ACGT'
    i = nucleotides.index(nucleotide)
    return nucleotides[3 - i]

doctest.run_docstring_examples(get_complement, globals())
```


```python
def get_complement(nucleotide):
    """
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return complements[nucleotide]

doctest.run_docstring_examples(get_complement, globals())
```

### Global variables

`complements` is used as a **constant**. It's set to the same value each time we run the function, and is never modified.

We might therefore use a **global variable** (at **top level** or **module scope**), instead of a **local variable**, to hold this value. See the implementation below.

Note that I've renamed the variable from `complement` to `nucleotide_complements`. This follows the principle that the further the distance between a variable's **definition** and it's **use**, the more descriptive the name should be. It also keeps us from using up a good short variable name such as `complement`, and having to remember not to use it as a function parameter name or local variable.

Note that Python global variables, [by convention](https://www.python.org/dev/peps/pep-0008/#global-variable-names), are written in [snakecase](https://en.wikipedia.org/wiki/Snake_case) (*e.g.* `complement_table`). Other programming languages write global constant as `ComplementTable` or `COMPLEMENT_TABLE`.


```python
nucleotide_complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def get_complement(nucleotide):
    """
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """
    return nucleotide_complements[nucleotide]

doctest.run_docstring_examples(get_complement, globals())
```

## `get_reverse_complement`

This first implementation reverses the sequence (`dna[::-1]`), and then takes the complement of each nucleotide from that reversed sequence:


```python
def get_reverse_complement(dna):
    """Compute the reverse complementary sequence of DNA for the specified DNA sequence.

    Parameters
    ----------
    dna : string
        A DNA sequence.

    Returns
    -------
    string
        The reverse complementary DNA sequence.
    
    Examples
    --------
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    reversed_complement = ''
    for nucleotide in dna[::-1]:
        reversed_complement += get_complement(nucleotide)
    return reversed_complement

doctest.run_docstring_examples(get_reverse_complement, globals())
```

We could also turn this around: find the nucleotide complements *first*, and then reverse *that*:


```python
def get_reverse_complement(dna):
    """
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    complement = ''
    for nucleotide in dna:
        complement += get_complement(nucleotide)
    return complement[::-1]

doctest.run_docstring_examples(get_reverse_complement, globals())
```

### `get_reverse_complement` – list comprehension solution


```python
def get_reverse_complement(dna):
    """
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    return ''.join([get_complement(nucleotide) for nucleotide in dna[::-1]])

doctest.run_docstring_examples(get_reverse_complement, globals())
```

Since the list is only constructed in order to pass it as argument to `join`, we can instead use a [generator expression](https://nedbatchelder.com/blog/201605/generator_comprehensions.html).


```python
def coding_strand_to_AA(dna):
    """
    >>> coding_strand_to_AA("ATGCGA")
    'MR'
    >>> coding_strand_to_AA("ATGCCCGCTTT")
    'MPA'
    """
    return ''.join(aa_table[dna[i:i + 3]] for i in range(0, len(dna), 3))

doctest.run_docstring_examples(coding_strand_to_AA, globals())
```

## `rest_of_ORF`

I've added some examples, that test smaller sequences, to the starter code for `rest_of_ORF`. If there's a bug that shows up with these simpler tests, it will be easier to spot and debug, then looking at the original test.


```python
def rest_of_ORF(dna):
    """Return the open reading frame that starts at the start of the DNA sequence.
    
    The open return frame is the prefix up to but not including the first in-frame stop codon.
    If there is no in frame stop codon, returns the whole string.
    
    Arguments
    ---------
    dna : string
        A DNA sequence that begins with a start codon.

    Returns
    -------
    string
        The open reading frame.
    
    Examples
    --------
    >>> rest_of_ORF("ATG")
    'ATG'
    >>> rest_of_ORF("ATGCCC")
    'ATGCCC'
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    """
    for i in range(0, len(dna), 3):
        if dna[i:i+3] in ["TAA", "TAG", "TGA"]:
            return dna[0:i]
    return dna

doctest.run_docstring_examples(rest_of_ORF, globals())
```

### Regular Expression solution

The following technique use a [**regular expression**](https://docs.python.org/3/howto/regex.html) to match a repeated (`+?`) count of three-character (`...`) groups (`(...)`), followed by one of (`|`) `TAA`, `TAG`, or `TGA`.


```python
import re

def rest_of_ORF(dna):
    """
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    """
    m = re.match(r'((...)+?)(TAA|TAG|TGA)', dna)
    if m:
        return m.group(1)
    return dna

doctest.run_docstring_examples(rest_of_ORF, globals())
```

## `find_all_ORFs_oneframe`

This first approach doesn't work:


```python
def find_all_ORFs_oneframe(dna):
    """Find all non-nested open reading frames in the given DNA sequence.
    
    This function only finds ORFs that are in the default frame of the sequence
    (i.e. they start on indices that are multiples of 3).
    By non-nested we mean that if an ORF occurs entirely within
    another ORF, it should not be included in the returned list of ORFs.
    
    Arguments
    ---------
    dna : string
        A DNA sequence.
        
    Returns
    -------
    list[string]
        Non-nested ORFs.
    
    Examples
    --------
    >>> find_all_ORFs_oneframe("ATG")
    ['ATG']
    >>> find_all_ORFs_oneframe("CATGCC")
    []
    >>> find_all_ORFs_oneframe("ATGCCCTAGATGTTTTAG")
    ['ATGCCC', 'ATGTTT']
    >>> find_all_ORFs_oneframe("ATGATGCCCTAG")
    ['ATGATGCCC']
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """
    orfs = []
    for i in range(0, len(dna), 3):
        if dna[i:i+3] == 'ATG':
            orf = rest_of_ORF(dna[i:])
            orfs.append(orf)
            i += len(orf)
    return orfs

doctest.run_docstring_examples(find_all_ORFs_oneframe, globals())
```

{: class="nb-output"}

    **********************************************************************
    File "__main__", line 27, in NoName
    Failed example:
        find_all_ORFs_oneframe("ATGATGCCCTAG")
    Expected:
        ['ATGATGCCC']
    Got:
        ['ATGATGCCC', 'ATGCCC']



This implementation includes the nested ORFs in its result. This is because when it finds an ORF, it's not actually skipping to its end before looking for the next start codon. The line `i += len(orf)` changes the value of `i`, but the next time through the loop body, `for i in range` resets `i` to the next value from `range`, so the `i += len(orf)` line doesn't actually have a lasting effect.

We can't use a `for in range` loop, because sometimes we need to step the index forwards by three (when we *don't* find a start tag), and sometimes skip forwards by the length of the ORF (when we *do* find a start tag). “Unpack” the `for i in range` to `i = 0; while i < len` to get more access to `i`:


```python
def find_all_ORFs_oneframe(dna):
    """Find all non-nested open reading frames in the given DNA sequence.
    
    This function only finds ORFs that are in the default frame of the sequence
    (i.e. they start on indices that are multiples of 3).
    By non-nested we mean that if an ORF occurs entirely within
    another ORF, it should not be included in the returned list of ORFs.
    
    Arguments
    ---------
    dna : string
        A DNA sequence.
        
    Returns
    -------
    list[string]
        Non-nested ORFs.
    
    Examples
    --------
    >>> find_all_ORFs_oneframe("ATG")
    ['ATG']
    >>> find_all_ORFs_oneframe("CATGCC")
    []
    >>> find_all_ORFs_oneframe("ATGCCCTAGATGTTTTAG")
    ['ATGCCC', 'ATGTTT']
    >>> find_all_ORFs_oneframe("ATGATGCCCTAG")
    ['ATGATGCCC']
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """
    orfs = []
    i = 0
    while i < len(dna):
        if dna[i:i+3] == 'ATG':
            orf = rest_of_ORF(dna[i:])
            orfs.append(orf)
            i += len(orf)
        else:
            i += 3
    return orfs

doctest.run_docstring_examples(find_all_ORFs_oneframe, globals())
```

### Another approach

Did I say we can't use `for i in range`? We *can*, if we keep track of whether we're inside an ORF (in which case we want to *turn off* looking for start codons). The following code uses a boolean variable to keep track of whether we're inside an ORF, and another variable to count how many nucleotides of the ORF are left, so that we can tell when we've exited it.


```python
def find_all_ORFs_oneframe(dna):
    """
    >>> find_all_ORFs_oneframe("ATG")
    ['ATG']
    >>> find_all_ORFs_oneframe("CATGCC")
    []
    >>> find_all_ORFs_oneframe("ATGCCCTAGATGTTTTAG")
    ['ATGCCC', 'ATGTTT']
    >>> find_all_ORFs_oneframe("ATGATGCCCTAG")
    ['ATGATGCCC']
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """
    orfs = []
    inside_orf = False
    remaining_orf_len = None
    for i in range(0, len(dna), 3):
        if inside_orf:
            remaining_orf_len -= 3
            if remaining_orf_len == 0:
                inside_orf = False
        elif dna[i:i+3] == 'ATG':
            orf = rest_of_ORF(dna[i:])
            orfs.append(orf)
            inside_orf = True
            remaining_orf_len = len(orf) - 3
    return orfs

doctest.run_docstring_examples(find_all_ORFs_oneframe, globals())
```

Instead of maintaining *two* variables – `inside_orf` to remember if we're inside an ORF, and `remaining_orf_len` to track how much of the ORF is left – we can use just `remaining_orf_len` to serve both purposes. If this is greater than zero, we're in an ORF. If it's value 0, we're not.

On the one hand, it's simpler to track this through a single variable instead of two. Then we don't have to think so hard to prove that the variables won't get out of sync with each other. On the other, using the variable for two purposes is trickier.


```python
def find_all_ORFs_oneframe(dna):
    """
    >>> find_all_ORFs_oneframe("ATG")
    ['ATG']
    >>> find_all_ORFs_oneframe("CATGCC")
    []
    >>> find_all_ORFs_oneframe("ATGCCCTAGATGTTTTAG")
    ['ATGCCC', 'ATGTTT']
    >>> find_all_ORFs_oneframe("ATGATGCCCTAG")
    ['ATGATGCCC']
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """
    orfs = []
    remaining_orf_len = 0
    for i in range(0, len(dna), 3):
        if remaining_orf_len > 0:
            remaining_orf_len -= 3
        elif dna[i:i+3] == 'ATG':
            orf = rest_of_ORF(dna[i:])
            orfs.append(orf)
            inside_orf = True
            remaining_orf_len = len(orf) - 3
    return orfs

doctest.run_docstring_examples(find_all_ORFs_oneframe, globals())
```

We can further simplify the code by defining `remaining_orf_len >= 0` to mean we're in an ORF, and `remaining_orf_len < 0` to mean we're not. This lets us *always* decrement `remaining_orf_len`.


```python
def find_all_ORFs_oneframe(dna):
    """
    >>> find_all_ORFs_oneframe("ATG")
    ['ATG']
    >>> find_all_ORFs_oneframe("CATGCC")
    []
    >>> find_all_ORFs_oneframe("ATGCCCTAGATGTTTTAG")
    ['ATGCCC', 'ATGTTT']
    >>> find_all_ORFs_oneframe("ATGATGCCCTAG")
    ['ATGATGCCC']
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """
    orfs = []
    remaining_orf_len = 0
    for i in range(0, len(dna), 3):
        if remaining_orf_len <= 0 and dna[i:i+3] == 'ATG':
            orf = rest_of_ORF(dna[i:])
            orfs.append(orf)
            inside_orf = True
            remaining_orf_len = len(orf)
        remaining_orf_len -= 3
    return orfs

doctest.run_docstring_examples(find_all_ORFs_oneframe, globals())
```

## `find_all_ORFs`


```python
def find_all_ORFs(dna):
    """Find all non-nested open reading frames in the given DNA sequence in all 3 possible frames.
    
    Non-nested means the same thing here that it does in find_all_ORFs_oneframe.

    Arguments
    ---------
    dna : string
        A DNA sequence.
    
    Returns
    -------
    string
        A list of non-nested ORFs.

    Examples
    --------
    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """
    orfs = []
    for i in range(3):
        orfs.extend(find_all_ORFs_oneframe(dna[i:]))
    return orfs

doctest.run_docstring_examples(find_all_ORFs, globals())
```

### `find_all_ORFs` – list comprehension solution


```python
def find_all_ORFs(dna):
    """Find all non-nested open reading frames in the given DNA sequence in all 3 possible frames.
    
    Non-nested means the same thing here that it does in find_all_ORFs_oneframe.

    Arguments
    ---------
    dna : string
        A DNA sequence.
    
    Returns
    -------
    string
        A list of non-nested ORFs.

    Examples
    --------
    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """
    return [orf
            for i in range(3)
            for orf in find_all_ORFs_oneframe(dna[i:])]

doctest.run_docstring_examples(find_all_ORFs, globals())
```

## `find_all_ORFs_both_strands`

Here's a variety of different approaches. This is a matter of taste.


```python
def find_all_ORFs_both_strands(dna):
    """Find all non-nested open reading frames in the given DNA sequence on both strands.
    
    Arguments
    ---------
    dna : string
        A DNA sequence.
    
    Returns
    -------
    string
        A list of non-nested ORFs.
        
    Examples
    --------
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    other_strand = get_reverse_complement(dna)
    orfs = []
    orfs.extend(find_all_ORFs(dna))
    orfs.extend(find_all_ORFs(other_strand))
    return orfs

doctest.run_docstring_examples(find_all_ORFs_both_strands, globals())
```

{: class="nb-output"}

    **********************************************************************
    File "__main__", line 16, in NoName
    Failed example:
        find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    Expected:
        ['ATGCGAATG', 'ATGCTACATTCGCAT']
    Got:
        ['ATGCGAATG', 'ATG', 'ATGCTACATTCGCAT']




```python
def find_all_ORFs_both_strands(dna):
    """
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    orfs = []
    orfs.extend(find_all_ORFs(dna))
    orfs.extend(find_all_ORFs(get_reverse_complement(dna)))
    return orfs

doctest.run_docstring_examples(find_all_ORFs_both_strands, globals())
```


```python
def find_all_ORFs_both_strands(dna):
    """
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    orfs = find_all_ORFs(dna)
    orfs.extend(find_all_ORFs(get_reverse_complement(dna)))
    return orfs

doctest.run_docstring_examples(find_all_ORFs_both_strands, globals())
```


```python
def find_all_ORFs_both_strands(dna):
    """
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    return find_all_ORFs(dna) + find_all_ORFs(get_reverse_complement(dna))

doctest.run_docstring_examples(find_all_ORFs_both_strands, globals())
```


```python
def find_all_ORFs_both_strands(dna):
    """
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    orfs = []
    for strand in [dna, get_reverse_complement(dna)]:
        orfs += find_all_ORFs(strand)
    return orfs

doctest.run_docstring_examples(find_all_ORFs_both_strands, globals())
```

## `longest_ORF`

I've added two different examples to test that the function returns `None` when there's no ORF. (Normally you'd add one or the other.) This is to illustrate why you might want to use `print` when writing the doctest for a function that is expected to return `None`. Evaluating a function that returns `None` in the Python prompt (and therefore within a doctest example) doesn't print anything. This can be confusing to read.


```python
def longest_ORF(dna):
    """Find the longest ORF on both strands of the specified sequence.
    
    Arguments
    ---------
    dna : string
        A DNA sequence.
    
    Returns
    -------
    string
        The longest ORF
    
    Examples
    --------
    >>> print(longest_ORF("CCC"))
    None
    >>> longest_ORF("CCC")
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    best = None
    best_len = 0
    for orf in find_all_ORFs_both_strands(dna):
        if len(orf) > best_len:
            best = orf
            best_len = len(orf)
    return best

doctest.run_docstring_examples(longest_ORF, globals())
```

`len(string)` isn't very expensive, so we can also do this with one variable (`best`) instead of keeping two variables (`best` and `best_len`) in sync:


```python
def longest_ORF(dna):
    """
    >>> print(longest_ORF("CCC"))
    None
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    best = None
    for orf in find_all_ORFs_both_strands(dna):
        if not best or len(orf) > len(best):
            best = orf
    return best

doctest.run_docstring_examples(longest_ORF, globals())
```

The following two implementations are more expensive, but less code. It's more expensive because sorting is more work than keep track of the longer, and because `sorted` makes a list.


```python
def longest_ORF(dna):
    """
    >>> print(longest_ORF("CCC"))
    None
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    orfs = find_all_ORFs_both_strands(dna)
    if orfs:
        return sorted(orfs, key=len)[-1]
    return None

doctest.run_docstring_examples(longest_ORF, globals())
```


```python
def longest_ORF(dna):
    """
    >>> print(longest_ORF("CCC"))
    None
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    orfs = find_all_ORFs_both_strands(dna)
    if orfs:
        return sorted(orfs, key=len, reverse=True)[0]
    return None

doctest.run_docstring_examples(longest_ORF, globals())
```

The final line `return None` isn't necessary. A function that don't execute a `return` statement *implicitly* returns `None` anyway.

It is, however, standard practice to add an *explicit* return to a fruitful function, that returns `None` when called with some arguments and other values when called with other arguments. This makes it easier to tell by scanning the implementation whether a function is fruitful or fruitless.

Use the `max` function to regain the efficiency of the initial approaches.


```python
def longest_ORF(dna):
    """
    >>> print(longest_ORF("CCC"))
    None
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    orfs = find_all_ORFs_both_strands(dna)
    if orfs:
        return max(orfs, key=len)
    else:
        return None

doctest.run_docstring_examples(longest_ORF, globals())
```

## `longest_ORF_noncoding`

Use `random.seed` to test functions that use random numbers. This resets the “random” number sequence (which isn't really random), so that it produces the same values in the same order each time.

The variable named `_` (single underscore) is a **placeholder variable**, for a "don't care" value. It's used when the language syntax requires that we use a variable name, but we never read the value of the variable.


```python
import random

def shuffle_string(s):
    return ''.join(random.sample(s, len(s)))

def longest_ORF_noncoding(dna, num_trials):
    """Compute the maximum length of the longest ORF over num_trials shuffles of the specified sequence.
    
    Arguments
    ---------
    dna : string
        A DNA sequence.
    num_trials : int
        The number of random shuffles.
    
    Returns
    -------
    int
        The maximum length longest ORF
    
    Examples
    --------
    >>> random.seed(1)
    >>> longest_ORF_noncoding("ATGCGAATGTAGCATCAAA", 100)
    19
    """
    max_len = 0
    for _ in range(num_trials):
        orf = longest_ORF(shuffle_string(dna))
        if orf:
            max_len = max(max_len, len(orf))
    return max_len

doctest.run_docstring_examples(longest_ORF_noncoding, globals())
```


```python
def longest_ORF_noncoding(dna, num_trials):
    """
    >>> random.seed(1)
    >>> longest_ORF_noncoding("ATGCGAATGTAGCATCAAA", 100)
    19
    """
    lens = []
    for _ in range(num_trials):
        orf = longest_ORF(shuffle_string(dna))
        if orf:
            lens.append(len(orf))
    return max(lens)

doctest.run_docstring_examples(longest_ORF_noncoding, globals())
```


```python
### `longest_ORF_noncoding` using a list comprehension
```


```python
def longest_ORF_noncoding(dna, num_trials):
    """
    >>> random.seed(1)
    >>> longest_ORF_noncoding("ATGCGAATGTAGCATCAAA", 100)
    19
    """
    return max(len(longest_ORF(shuffle_string(dna)) or '') for _ in xrange(num_trials))
```

## `coding_strand_to_AA`


```python
def coding_strand_to_AA(dna):
    """Compute the protein encoded by a DNA sequence.
    
    This function does not check for start and stop codons.
    (It assumes that the DNA sequence represents a protein coding region).

    Parameters
    ----------
    dna : string
        A DNA sequence.
    
    Returns
    -------
    string
        The sequence of amino acids encoded by the input DNA fragment.
        
    Examples
    --------
    >>> coding_strand_to_AA("ATGCGA")
    'MR'
    >>> coding_strand_to_AA("ATGCCCGCTTT")
    'MPA'
    """
    aas = ''
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        aas += aa_table[codon]
    return aas

doctest.run_docstring_examples(coding_strand_to_AA, globals())
```

### `coding_strand_to_AA` – list comprehension solution


```python
def coding_strand_to_AA(dna):
    """
    >>> coding_strand_to_AA("ATGCGA")
    'MR'
    >>> coding_strand_to_AA("ATGCCCGCTTT")
    'MPA'
    """
    return ''.join([aa_table[dna[i:i + 3]] for i in range(0, len(dna), 3)])

doctest.run_docstring_examples(coding_strand_to_AA, globals())
```

Since the list is only constructed in order to pass it as argument to `join`, we can instead use a [generator expression](https://nedbatchelder.com/blog/201605/generator_comprehensions.html).


```python
def coding_strand_to_AA(dna):
    """
    >>> coding_strand_to_AA("ATGCGA")
    'MR'
    >>> coding_strand_to_AA("ATGCCCGCTTT")
    'MPA'
    """
    return ''.join(aa_table[dna[i:i + 3]] for i in range(0, len(dna), 3))

doctest.run_docstring_examples(coding_strand_to_AA, globals())
```

## `gene_finder`


```python
def gene_finder(dna):
    """Return the amino acid sequences that are likely coded by the specified DNA sequence.

    Parameters
    ----------
    dna : string
        A DNA sequence.
    
    Returns
    -------
    list[string]
        A list of all amino acid sequences coded by the DNA sequence.


    Examples:
    >>> random.seed(1)
    >>> gene_finder("ATGTCATTGCGTGTGAGACAGATTGATCGTCGCGAATGGCTATTGGCGCAAACCGCGACAGAATGCCAGCGCCATGGCCGGGAA" \
                    "GCGACGCTGGAATATCCGACGCGACAGGGAATGTGGGTTCGGTTGAGCGATGCAGAAAAACGGTGGTCGGCCTGGATTAAACCT" \
                    "GGGGACTGGCTTGAGCATGTCTCTCCCGCTCTGGCTGGGGCGGCGGTTTCTGCTGGCGCTGAGCACCTGGTCGTTCCCTGGCTT")
    ['MSLRVRQIDRREWLLAQTATECQRHGREATLEYPTRQGMWVRLSDAEKRWSAWIKPGDWLEHVSPALAGAAVSAGAEHLVVPWL']
    """
    threshold = longest_ORF_noncoding(dna, 1500)
    aas = []
    for orf in find_all_ORFs_both_strands(dna):
        if len(orf) > threshold:
            aas.append(coding_strand_to_AA(orf))
    return aas
```

### `gene_finder` – list comprehension solution


```python
def gene_finder(dna):
    """
    >>> random.seed(1)
    >>> gene_finder("ATGTCATTGCGTGTGAGACAGATTGATCGTCGCGAATGGCTATTGGCGCAAACCGCGACAGAATGCCAGCGCCATGGCCGGGAA" \
                    "GCGACGCTGGAATATCCGACGCGACAGGGAATGTGGGTTCGGTTGAGCGATGCAGAAAAACGGTGGTCGGCCTGGATTAAACCT" \
                    "GGGGACTGGCTTGAGCATGTCTCTCCCGCTCTGGCTGGGGCGGCGGTTTCTGCTGGCGCTGAGCACCTGGTCGTTCCCTGGCTT")
    ['MSLRVRQIDRREWLLAQTATECQRHGREATLEYPTRQGMWVRLSDAEKRWSAWIKPGDWLEHVSPALAGAAVSAGAEHLVVPWL']
    """
    threshold = longest_ORF_noncoding(dna, 1500)
    return [coding_strand_to_AA(orf)
            for orf in find_all_ORFs_both_strands(dna)
            if len(orf) > threshold]
```
