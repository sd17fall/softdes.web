---
omit_title: true
---

{% include toc %}


# GeneFinder solutions – Going Beyond

This notebook contains solutions for *some* of the Going Beyond extension to the GeneFinder project. It is a supplement to [GeneFinder solutions](/notes/genefinder-solutions.md).

## Metagenomics


```python
from load import load_nitrogenase_seq, load_metagenome

def find_longest_common_substring_length(s1, s2):
    """Return the length of the longest common substring of `s1` and `s2`.

    Examples
    --------
    >>> find_longest_common_substring_length('abc', 'xaz')
    1
    >>> find_longest_common_substring_length('abc', 'xabz')
    2
    >>> find_longest_common_substring_length('abc', 'xabcz')
    3
    >>> find_longest_common_substring_length('abc', 'xyabcz')
    3
    >>> find_longest_common_substring_length('abc', 'abcz')
    3
    >>> find_longest_common_substring_length('abc', 'xyabc')
    3
    >>> find_longest_common_substring_length('abc', 'xyz')
    0
    """

    longest_len = 0
    for i1 in range(len(s1)):
        for i2 in range(len(s2)):
            offset = 0
            while i1 + offset < len(s1) and i2 + offset < len(s2) and s1[i1 + offset] == s2[i2 + offset]:
                offset += 1
            longest_len = max(longest_len, offset)
    return longest_len

def find_snippet_with_greatest_overlap(target_sequence, snippets):
    """Return the name of the snippet whose sequence has the greatest overlap with target_sequence.

    Arguments
    ---------
    snippets : list
        A list of tuples of (snippet_name, sequence).
    target_sequence : str
        The nucleotide sequence

    Examples
    --------
    >>> snippets = [('1', 'AG'), ('2', 'AGAGAG'), ('3', 'ATAGA')]
    >>> find_snippet_with_greatest_overlap('TAG', snippets)
    '3'
    >>> find_snippet_with_greatest_overlap('AGAG', snippets)
    '2'
    """
    snippet_name, _ = max(snippets, key=lambda snippet: find_longest_common_substring_length(snippet[1], target_sequence))
    return snippet_name


def main():
    nitrogenase = load_nitrogenase_seq()
    metagenome = load_metagenome()
    print find_snippet_with_greatest_overlap(nitrogenase, metagenome)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        import doctest
        doctest.testmod()
    else:
        main()
```

## Multiprocessing

This section includes variant implementations of `longest_ORF_noncoding`. From top to bottom, they increase in concision, and make increasing use of list comprehensions.


```python
from multiprocessing import Pool

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
    p = Pool()
    shuffles = []
    for _ in range(num_trials):
        shuffles.append(shuffle_string(dna))
    orfs = p.map(longest_ORF, shuffles)
    n = 0
    for orf in orfs:
        if len(orf) > n:
            n = len(orf)
    return n
```


```python
from multiprocessing import Pool

def longest_ORF_noncoding(dna, num_trials):
    """
    >>> random.seed(1)
    >>> longest_ORF_noncoding("ATGCGAATGTAGCATCAAA", 100)
    19
    """
    p = Pool()
    shuffles = []
    for _ in range(num_trials):
        shuffles.append(shuffle_string(dna))
    n = 0
    for orf in p.map(longest_ORF, shuffles):
        if orf:
            n = max(n, len(orf))
    return n
```


```python
from multiprocessing import Pool

def longest_ORF_noncoding(dna, num_trials):
    """
    >>> random.seed(1)
    >>> longest_ORF_noncoding("ATGCGAATGTAGCATCAAA", 100)
    19
    """
    p = Pool()
    shuffles = [shuffles.append(shuffle_string(dna)) for _ in range(num_trials)]
    lengths = [orf
               for orf in p.map(longest_ORF, shuffles)
               if orf]
    return max(lengths, default=0)
```


```python
from multiprocessing import Pool

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
    p = Pool()
    return max(len(orf)
               for orf in p.map(longest_ORF, (shuffle_string(dna) for _ in range(num_trials)))
               if orf)
```
