---
date: 2017-11-27T16:14:33-05:00
source: notebooks/exceptions.ipynb
---

{% include toc %}


# Exceptions


```python
def complement(c):
    if c == 'A':
        return 'T'
    if c == 'T':
        return 'A'
    if c == 'C':
        return 'G'
    if c == 'G':
        return 'C'
```

is equivalent to:


```python
def complement(c):
    if c == 'A':
        return 'T'
    if c == 'T':
        return 'A'
    if c == 'C':
        return 'G'
    if c == 'G':
        return 'C'
    return None
```

`complement_seq` is a client of `complement`:


```python
def complement_seq(dna_seq):
    return ''.join(complement(b) for b in dna_seq[::-1])
```

Unfolded, to make debugging easier:


```python
def complement_seq(dna_seq):
    result = ''
    for b in dna_seq[::-1]:
        c = complement(b)
        result += c
    return result
```

Passing an invalid argument to `complement_seq` passes an invalid argument to `complement`, which raises an exception. The exception is downstream from the call to `complement`, and has an unrevealing name and message. This makes this difficult to debug.


```python
complement_seq('CAXT')
```

{: class="nb-output"}


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-46-cef160c3921b> in <module>()
    ----> 1 complement_seq('CAXT')
    

    <ipython-input-45-1a6d8e3928b2> in complement_seq(dna_seq)
          3     for b in dna_seq[::-1]:
          4         c = complement(b)
    ----> 5         result += c
          6     return result


    TypeError: Can't convert 'NoneType' object to str implicitly



## Return-value-as-error
One technique (frowned on in Python) is to represent an error by an “out-of-band” value. “Out-of-band” means not in the set of valid return values for the function.


```python
def complement(c):
    if c == 'A':
        return 'T'
    if c == 'T':
        return 'A'
    if c == 'C':
        return 'G'
    if c == 'G':
        return 'C'
    return 'error'
```

`complement` callers need to know about this. If they don't know how to recover from the error, they should return an out-of-band value too. Then *their* callers need to follow this convention as well.


```python
def complement_seq(dna_seq):
    result = ''
    for b in dna_seq[::-1]:
        c = complement(b)
        if c == 'error':
            return 'error'
        result += c
    return result
```


```python
def function_that_uses_complement_seq():
    # do some stuff that computes dna_seq
    # ...
    comp_seq = complement_seq(dna_seq)
    if comp_seq == 'error':
        return 'error'
    # now the case where comp_seq didn't return an error
```

## Exceptions

The alternative to *returning a value* is to *raise an *exception*:


```python
def complement(c):
    if c == 'A':
        return 'T'
    if c == 'T':
        return 'A'
    if c == 'C':
        return 'G'
    if c == 'G':
        return 'C'
    raise Exception('invalid nucleobase')

complement('X')
```

{: class="nb-output"}


    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    <ipython-input-47-6c045add2467> in <module>()
         10     raise Exception('invalid nucleobase')
         11 
    ---> 12 complement('X')
    

    <ipython-input-47-6c045add2467> in complement(c)
          8     if c == 'G':
          9         return 'C'
    ---> 10     raise Exception('invalid nucleobase')
         11 
         12 complement('X')


    Exception: invalid nucleobase



The exception is be thrown straight through `complement`'s callers – even if they don't know about exceptions. This makes for easier debugging.


```python
def complement_seq(dna_seq):
    result = ''
    for b in dna_seq[::-1]:
        c = complement(b)
        result += c
    return result

complement_seq('CAXT')
```

{: class="nb-output"}


    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    <ipython-input-49-2d23b82ff07b> in <module>()
          6     return result
          7 
    ----> 8 complement_seq('CAXT')
    

    <ipython-input-49-2d23b82ff07b> in complement_seq(dna_seq)
          2     result = ''
          3     for b in dna_seq[::-1]:
    ----> 4         c = complement(b)
          5         result += c
          6     return result


    <ipython-input-47-6c045add2467> in complement(c)
          8     if c == 'G':
          9         return 'C'
    ---> 10     raise Exception('invalid nucleobase')
         11 
         12 complement('X')


    Exception: invalid nucleobase



## Catching (or handling) exceptions

`pay_me_a_complement` is a client of `complement_seq`.

The straightforward implementation displays a stack trace when the user enters an invalid sequence.


```python
def pay_me_a_complement():
    seq = input()
    print('The complement is', complement_seq(seq))

pay_me_a_complement()
```

{: class="nb-output"}

    CAXT



    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    <ipython-input-50-0f7ab1192a67> in <module>()
          3     print('complement is', complement_seq(seq))
          4 
    ----> 5 pay_me_a_complement()
    

    <ipython-input-50-0f7ab1192a67> in pay_me_a_complement()
          1 def pay_me_a_complement():
          2     seq = input()
    ----> 3     print('complement is', complement_seq(seq))
          4 
          5 pay_me_a_complement()


    <ipython-input-49-2d23b82ff07b> in complement_seq(dna_seq)
          2     result = ''
          3     for b in dna_seq[::-1]:
    ----> 4         c = complement(b)
          5         result += c
          6     return result


    <ipython-input-47-6c045add2467> in complement(c)
          8     if c == 'G':
          9         return 'C'
    ---> 10     raise Exception('invalid nucleobase')
         11 
         12 complement('X')


    Exception: invalid nucleobase



Use `try…except` to handle exceptions.

The following code acts normally the same as the implementation above the code in the `try` block runs without exception.

If, however, there's an exception within the `try` block, then the program skips the rest of that block and picks up at the start of the `except` block instead.


```python
def pay_me_a_complement():
    seq = input()
    try:
        print('The complement is', complement_seq(seq))
    except:
        print('Invalid DNA sequence: {}'.format(seq))
    print('done')

pay_me_a_complement()
```

{: class="nb-output"}

    CAXT
    Invalid DNA sequence: CAXT
    done



## User-Defined Exception Class

The previous implementation indiscrimately turns all program errors into an "Invalid DNA sequence" message.

It's equivalent to the following function. `except Exception` means catch any exception that is an instance of the class `Exception` – but this is all exceptions.


```python
def pay_me_a_complement():
    seq = input()
    try:
        print('The complement is', complement_seq(seq))
    except Exception:
        print('Invalid sequence')
    print('done')

pay_me_a_complement()
```

We can write a more specific `except` clause, to handle a more specific exception:


```python
class InvalidNucleobaseException(Exception):
    pass

def complement(c):
    if c == 'A':
        return 'T'
    if c == 'T':
        return 'A'
    if c == 'C':
        return 'G'
    if c == 'G':
        return 'C'
    raise InvalidNucleobaseException('invalid nucleobase')
```


```python
def pay_me_a_complement():
    seq = input()
    try:
        print('The complement is', complement_seq(seq))
    except InvalidNucleobaseException:
        print('Invalid DNA sequence: {}'.format(seq))

pay_me_a_complement()
```

{: class="nb-output"}

    CAXT
    Invalid DNA sequence: CAXT


