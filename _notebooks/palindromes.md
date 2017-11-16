---
date: 2017-09-28T18:11:27-04:00
source: notebooks/palindromes.ipynb
---

{% include toc %}


# Palindrome Notes

## Iterative strategy


```python
import doctest

def is_palindrome(s):
    """
    >>> is_palindrome('divide')
    False
    >>> is_palindrome('redivider')
    True
    """
    for i in range(len(s)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

doctest.run_docstring_examples(is_palindrome, globals())
```

Abbreviate `s[len(s) - n]` as `s[-m]`:


```python
import doctest

def is_palindrome(s):
    """
    >>> is_palindrome('divide')
    False
    >>> is_palindrome('redivider')
    True
    """
    for i in range(len(s)):
        if s[i] != s[-1 - i]:
            return False
    return True

doctest.run_docstring_examples(is_palindrome, globals())
```

Stop at the middle. (More efficient; same functionality.)


```python
import doctest

def is_palindrome(s):
    """
    >>> is_palindrome('divide')
    False
    >>> is_palindrome('redivider')
    True
    """
    for i in range(len(s) // 2):
        if s[i] != s[len(s) -1 - i]:
            return False
    return True

doctest.run_docstring_examples(is_palindrome, globals())
```

It's good to have test cases for special and extreme cases. (In this case, the empty string.)


```python
import doctest

def is_palindrome(s):
    """
    >>> is_palindrome('')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('divide')
    False
    >>> is_palindrome('redivider')
    True
    """
    for i in range(len(s) // 2):
        if s[i] != s[len(s) -1 - i]:
            return False
    return True

doctest.run_docstring_examples(is_palindrome, globals())
```

### Iterative strategy – ignoring case

Add a test case we wished passed, and replace `=` by the function we wish we had (`eq_ignores_case`).


```python
import doctest

def palindrome(s):
    """Returns true iff s is a palindrome.
    
    A palindrome is a string that is the same reversed, ignoring capitalization.
    
    >>> is_palindrome('')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('divide')
    False
    >>> is_palindrome('redivider')
    True
    >>> is_palindrome('Bob')
    True
    """
    for i in range(len(s)):
        if not eq_ignores_case(s[i], s[-1-i]):
            return False
    return True

doctest.run_docstring_examples(is_palindrome, globals())
```

Now write `eq_ignores_case`:


```python
def eq_ignores_case(a, b):
    """
    >>> eq_ignores_case('a', 'a')
    True
    >>> eq_ignores_case('a', 'A')
    True
    >>> eq_ignores_case('A', 'a')
    True
    >>> eq_ignores_case('A', 'A')
    True
    >>> eq_ignores_case('a', 'b')
    False
    """
    if a == b:
        return True
    if a.islower() and b.isupper() and a.upper() == b:
        return True
    if b.islower() and a.isupper() and b.upper() == a:
        return True
    return False

doctest.run_docstring_examples(eq_ignores_case, globals())
```

Can be simplified to:


```python
def eq_ignores_case(a, b):
    """
    >>> eq_ignores_case('a', 'a')
    True
    >>> eq_ignores_case('a', 'A')
    True
    >>> eq_ignores_case('A', 'a')
    True
    >>> eq_ignores_case('A', 'A')
    True
    >>> eq_ignores_case('a', 'b')
    False
    """
    if a == b:
        return True
    if a.upper() == b:
        return True
    if b.upper() == a:
        return True
    return False

doctest.run_docstring_examples(eq_ignores_case, globals())
```

Can be simplified to:


```python
def eq_ignores_case(a, b):
    """
    >>> eq_ignores_case('a', 'a')
    True
    >>> eq_ignores_case('a', 'A')
    True
    >>> eq_ignores_case('A', 'a')
    True
    >>> eq_ignores_case('A', 'A')
    True
    >>> eq_ignores_case('a', 'b')
    False
    """
    if a == b:
        return True
    if a.upper() == b.upper():
        return True
    return False

doctest.run_docstring_examples(eq_ignores_case, globals())
```

Can be simplified to:


```python
def eq_ignores_case(a, b):
    """
    >>> eq_ignores_case('a', 'a')
    True
    >>> eq_ignores_case('a', 'A')
    True
    >>> eq_ignores_case('A', 'a')
    True
    >>> eq_ignores_case('A', 'A')
    True
    >>> eq_ignores_case('a', 'b')
    False
    """
    if a.upper() == b.upper():
        return True
    return False

doctest.run_docstring_examples(eq_ignores_case, globals())
```

Can be simplified to:


```python
def eq_ignores_case(a, b):
    """
    >>> eq_ignores_case('a', 'a')
    True
    >>> eq_ignores_case('a', 'A')
    True
    >>> eq_ignores_case('A', 'a')
    True
    >>> eq_ignores_case('A', 'A')
    True
    >>> eq_ignores_case('a', 'b')
    False
    """
    return a.upper() == b.upper()

doctest.run_docstring_examples(eq_ignores_case, globals())
```

Now the tests pass:


```python
import doctest

def is_palindrome(s):
    """Returns true iff s is a palindrome.
    
    A palindrome is a string that is the same reversed, ignoring capitalization.
    
    >>> is_palindrome('')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('divide')
    False
    >>> is_palindrome('redivider')
    True
    >>> is_palindrome('Bob')
    True
    """
    for i in range(len(s)):
        if not eq_ignores_case(s[i], s[-1-i]):
            return False
    return True

doctest.run_docstring_examples(is_palindrome, globals())
```

### Iterative strategy – ignoring punctuation

First, unpack the `for i` in the previous definition of `is_palindrome`, for more control over its iteration than `for i in range` allows.

We will add test cases for the new functionality (ignoring punctation) that we want to test, but these test cases won't pass.


```python
import doctest

def is_palindrome(s):
    """Returns true iff s is a palindrome.
    
    A palindrome is a string that is the same reversed, ignoring punctuation and capitalization.
    
    >>> is_palindrome('')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('divide')
    False
    >>> is_palindrome('redivider')
    True
    >>> is_palindrome('Re-divider')
    True
    >>> is_palindrome('Bob')
    True
    >>> is_palindrome('A man, a plan, a canal – Panama!')
    True
    """
    i = 0
    while i < len(s):
        if not eq_ignores_case(s[i], s[-1-i]):
            return False
        i += 1
    return True

doctest.run_docstring_examples(palindrome, globals())
```

Now introduce a distinct variable for iterating from the end of the loop. This still doesn't make the tests pass, but it's one step closer.


```python
import doctest

def is_palindrome(s):
    """Returns true iff s is a palindrome.
    
    A palindrome is a string that is the same reversed, ignoring punctuation and capitalization.
    
    >>> is_palindrome('')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('divide')
    False
    >>> is_palindrome('redivider')
    True
    >>> is_palindrome('Re-divider')
    True
    >>> is_palindrome('Bob')
    True
    >>> is_palindrome('A man, a plan, a canal – Panama!')
    True
    """
    i = 0
    j = len(s) - 1
    while i < len(s):
        if not eq_ignores_case(s[i], s[j]):
            return False
        i += 1
        j -= 1
    return True

doctest.run_docstring_examples(is_palindrome, globals())
```

{: class="nb-output"}

    **********************************************************************
    File "__main__", line 16, in NoName
    Failed example:
        is_palindrome('Re-divider')
    Expected:
        True
    Got:
        False
    **********************************************************************
    File "__main__", line 20, in NoName
    Failed example:
        is_palindrome('A man, a plan, a canal – Panama!')
    Expected:
        True
    Got:
        False



Step over punctuation. The following uses a slightly different approach from in class: defining a function `is_punct` instead of using `c in punct` each time.

It also changes the loop test to `i < j` to detect when the left and right indices meet in the middle. This avoids the need for more complicated `while` statements to avoid running the indices off the end of the string while skipping over punctuation.


```python
import doctest

def is_punct(c):
    return c in ' -–.,!'

def is_palindrome(s):
    """Returns true iff s is a palindrome.
    
    A palindrome is a string that is the same reversed, ignoring punctuation or capitalization.
    
    >>> is_palindrome('')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('divide')
    False
    >>> is_palindrome('redivider')
    True
    >>> is_palindrome('Re-divider')
    True
    >>> is_palindrome('Bob')
    True
    >>> is_palindrome('A man, a plan, a canal – Panama!')
    True
    >>> is_palindrome('Doc, note I dissent. A fast never prevents a fatness. I diet on cod.')
    True
    """
    i = 0
    j = len(s) - 1
    while i < j:
        while is_punct(s[i]):
            i += 1
        while is_punct(s[j]):
            j -= 1
        if not eq_ignores_case(s[i], s[j]):
            return False
        i += 1
        j -= 1
    return True

doctest.run_docstring_examples(is_palindrome, globals())
```

{: class="nb-output"}

    **********************************************************************
    File "__main__", line 15, in NoName
    Failed example:
        is_palindrome('divide')
    Exception raised:
        Traceback (most recent call last):
          File "/Users/osteele/anaconda3/lib/python3.5/doctest.py", line 1321, in __run
            compileflags, 1), test.globs)
          File "<doctest NoName[2]>", line 1, in <module>
            is_palindrome('divide')
          File "<ipython-input-1-397877bcfdf1>", line 35, in is_palindrome
            if not eq_ignores_case(s[i], s[j]):
        NameError: name 'eq_ignores_case' is not defined
    **********************************************************************
    File "__main__", line 17, in NoName
    Failed example:
        is_palindrome('redivider')
    Exception raised:
        Traceback (most recent call last):
          File "/Users/osteele/anaconda3/lib/python3.5/doctest.py", line 1321, in __run
            compileflags, 1), test.globs)
          File "<doctest NoName[3]>", line 1, in <module>
            is_palindrome('redivider')
          File "<ipython-input-1-397877bcfdf1>", line 35, in is_palindrome
            if not eq_ignores_case(s[i], s[j]):
        NameError: name 'eq_ignores_case' is not defined
    **********************************************************************
    File "__main__", line 19, in NoName
    Failed example:
        is_palindrome('Re-divider')
    Exception raised:
        Traceback (most recent call last):
          File "/Users/osteele/anaconda3/lib/python3.5/doctest.py", line 1321, in __run
            compileflags, 1), test.globs)
          File "<doctest NoName[4]>", line 1, in <module>
            is_palindrome('Re-divider')
          File "<ipython-input-1-397877bcfdf1>", line 35, in is_palindrome
            if not eq_ignores_case(s[i], s[j]):
        NameError: name 'eq_ignores_case' is not defined
    **********************************************************************
    File "__main__", line 21, in NoName
    Failed example:
        is_palindrome('Bob')
    Exception raised:
        Traceback (most recent call last):
          File "/Users/osteele/anaconda3/lib/python3.5/doctest.py", line 1321, in __run
            compileflags, 1), test.globs)
          File "<doctest NoName[5]>", line 1, in <module>
            is_palindrome('Bob')
          File "<ipython-input-1-397877bcfdf1>", line 35, in is_palindrome
            if not eq_ignores_case(s[i], s[j]):
        NameError: name 'eq_ignores_case' is not defined
    **********************************************************************
    File "__main__", line 23, in NoName
    Failed example:
        is_palindrome('A man, a plan, a canal – Panama!')
    Exception raised:
        Traceback (most recent call last):
          File "/Users/osteele/anaconda3/lib/python3.5/doctest.py", line 1321, in __run
            compileflags, 1), test.globs)
          File "<doctest NoName[6]>", line 1, in <module>
            is_palindrome('A man, a plan, a canal – Panama!')
          File "<ipython-input-1-397877bcfdf1>", line 35, in is_palindrome
            if not eq_ignores_case(s[i], s[j]):
        NameError: name 'eq_ignores_case' is not defined
    **********************************************************************
    File "__main__", line 25, in NoName
    Failed example:
        is_palindrome('Doc, note I dissent. A fast never prevents a fatness. I diet on cod.')
    Exception raised:
        Traceback (most recent call last):
          File "/Users/osteele/anaconda3/lib/python3.5/doctest.py", line 1321, in __run
            compileflags, 1), test.globs)
          File "<doctest NoName[7]>", line 1, in <module>
            is_palindrome('Doc, note I dissent. A fast never prevents a fatness. I diet on cod.')
          File "<ipython-input-1-397877bcfdf1>", line 35, in is_palindrome
            if not eq_ignores_case(s[i], s[j]):
        NameError: name 'eq_ignores_case' is not defined



A more robust implementation of `is_punct`:


```python
import string

def is_punct(c):
    return c not in string.ascii_letters
```

## Compare to Reversed String

This is a more direct implementation of “A palindrome is a string that is the same reversed”.
The following three implementations use three different methods to reverse a string.


```python
import doctest

def is_palindrome(s):
    """
    >>> is_palindrome('divide')
    False
    >>> is_palindrome('redivider')
    True
    """
    r = ''
    for i in range(len(s)):
        r += s[-1-i]
    return s == r

doctest.run_docstring_examples(is_palindrome, globals())
```


```python
import doctest

def is_palindrome(s):
    """
    >>> is_palindrome('divide')
    False
    >>> is_palindrome('redivider')
    True
    """
    r = ''.join(reversed(s))
    return s == r

doctest.run_docstring_examples(is_palindrome, globals())
```


```python
import doctest

def is_palindrome(s):
    """
    >>> is_palindrome('divide')
    False
    >>> is_palindrome('redivider')
    True
    """
    r = s[::-1]
    return s == r

doctest.run_docstring_examples(is_palindrome, globals())
```

### Ignore case


```python
import doctest

def is_palindrome(s):
    """
    >>> palindrome('divide')
    False
    >>> palindrome('redivider')
    True
    >>> palindrome('Bob')
    True
    """
    r = s[::-1]
    return s.upper() == r.upper()

doctest.run_docstring_examples(is_palindrome, globals())
```

### Ignore punctuation

This implementation is slightly different from the version in class.


```python
import doctest

def is_palindrome(s):
    """
    >>> is_palindrome('divide')
    False
    >>> is_palindrome('redivider')
    True
    >>> is_palindrome('Bob')
    True
    >>> is_palindrome('Re-divider')
    True
    """
    # Remove each punctuation character from s, and assign the new value to s.
    for c in set(s):
        if is_punct(c):
            s = s.replace(c, '')
    r = s[::-1]
    return s.upper() == r.upper()

doctest.run_docstring_examples(is_palindrome, globals())
```

## Using Recursion


```python
import doctest

def palindrome(s):
    """
    >>> is_palindrome('divide')
    False
    >>> is_palindrome('redivider')
    True
    """
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

doctest.run_docstring_examples(is_palindrome, globals())
```

### Recursion – ignoring case


```python
import doctest

def is_palindrome(s):
    """
    >>> is_palindrome('divide')
    False
    >>> is_palindrome('redivider')
    True
    >>> is_palindrome('Bob')
    True
    """
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True
    if s[0].upper() != s[-1].upper():
        return False
    return palindrome(s[1:-1])

doctest.run_docstring_examples(is_palindrome, globals())
```

### Recursion – ignore punctuation


```python
import doctest

def is_palindrome(s):
    """
    >>> is_palindrome('divide')
    False
    >>> is_palindrome('redivider')
    True
    >>> is_palindrome('Bob')
    True
    >>> is_palindrome('Re-divider')
    True
    """
    if len(s) <= 1:
        return True
    if is_punct(s[0]):
        return is_palindrome(s[1:])
    if is_punct(s[-1]):
        return is_palindrome(s[:-1])
    if s[0].upper() != s[-1].upper():
        return False
    return is_palindrome(s[1:-1])

doctest.run_docstring_examples(is_palindrome, globals())
```
