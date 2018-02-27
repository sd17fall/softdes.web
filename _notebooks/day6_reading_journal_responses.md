---
date: 2018-02-13T12:12:54-05:00
source: notebooks/day6_reading_journal_responses.ipynb
---

{% include toc %}


### Exercise 6  

A palindrome is a word that is spelled the same backward and forward, like “noon” and “redivider”. Recursively, a word is a palindrome if the first and last letters are the same and the middle is a palindrome.

You can use the `first`, `last`, and `middle` helper functions defined in Think Python, or do the string slices inside your function directly. Be sure to think about your base cases.
    
Write a function called `is_palindrome` that takes a string argument and returns `True` if it is a palindrome and `False` otherwise. Remember that you can use the built-in function `len` to check the length of a string.

Write some unit tests for your function (optionally using doctest) to show that it works as intended.


```python
def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
```


```python
# Palindrome Solution 1

def is_palindrome(word):
    if first(word)==last(word):
        if len(word)<=2:
            return True
        else:
            return is_palindrome (middle(word)) 
    else:
        return False
```


```python
# Palindrome Solution 2

def is_palindrome(x):
    if len(x) >= 3: 
        if x[0] == x[-1]:
            return is_palindrome(x[1:-1])
        else:
            return False
    elif x[0] == x[-1]:
        return True
    else:
        return False        
```


```python
# Palindrome Solution 3

def is_palindrome (x):
    """
>>> is_palindrome("cart")
False
>>> is_palindrome("bobob")
True
>>> is_palindrome("kayak")
True
    """
    for i in range(len(x)):
        if x == x[::-1]:
            return True
    return False
```


```python
# Palindrome Solution 4

def is_pallindrome(string):
    string = string.lower()
    if len(string)>1:
        if string[0] == string[len(string)-1]:
            string = string[1:len(string)-1]
            return True
        if string[0] != string[len(string)-1]:
            return False
    return is_pallindrome(string)
```


```python
# Palindrome Solution 5

def is_palindrome(s):
    """
    >>> is_palindrome("Go hand a salami Im a lasagna hog") # even palindrome
    True
    >>> is_palindrome("Ah Satan sees Natasha")
    True
    >>> is_palindrome("No melons no lemon") # odd palindrome
    True
    >>> is_palindrome("Now I see bees I lost") # not a palindrome
    False
    """
    s = s.strip().lower()
    if len(s) <= 1:
        return True
    if s[0] == s[len(s)-1]:
        return is_palindrome(s[1::len(s)-1])
    else:
        return False
```


```python
# Palindrome Solution 6

def is_palindrome(word):
    flag = True
    if len(word) == 1:
        return True
    if len(word) < 3: #when len == 2
        return first(word) == last(word)
    return (first(word) == last(word) and is_palindrome(middle(word)))
```


```python
# Palindrome Solution 7

def is_palindrome(WoRd):
    """ Returns True/False for if input is a palindrome.
    >>> is_palindrome('word')
    False
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('Racecar')
    True
    >>> is_palindrome('redivider')
    True
    >>> is_palindrome('l')
    True
    """
    word = WoRd.lower()
    if len(word) < 3:
        if first(word) == last(word):
            return True
        else:
            return False
    if len(word) >= 3:
        if first(word) == last(word):
            return is_palindrome(middle(word))
        else:
            return False
```


```python
# Palindrome Solution 8

def palindrome(word):
    """
    Recursively looks through a string and determines if it is a palindrome.
    
    >>> palindrome('racecar')
    True
    
    >>> palindrome('abba')
    True
    
    >>> palindrome('palindrome')
    False
    
    """
    if len(word) < 2:
        return True
    elif word[0] == word[-1]:
        return palindrome(word[1:-1])
    return False
```


```python
# Palindrome Solution 9

def is_palindrome(word):
    '''
>>> is_palindrome("redivider")
True
>>> is_palindrome("bob")
True
>>> is_palindrome("ttta")
False
>>> is_palindrome("aaaaaaa")
True

'''
    mid = middle(word)
    if first(word) == last(word):    
        if mid[:] == mid[::-1]:
            return True
    return False
```


```python
# Palindrome Solution 10

def is_palindrome(word):
    word_list = list(word)
    length = len(word_list)
    if length <= 2:
        return False
    elif length > 2:
        for letters in word_list:
            if word_list[0] == word_list[-1]:
                del(word_list[0])
                del(word_list[-1])
    if len(word_list)== 0:
        return True
    else:
        return False
```


```python
# Palindrome Solution 11

def is_palindrome(word):
    forward = word
    backward = word[::-1]
    if forward == backward:
        return True
    return False
```


```python
# Palindrome Solution 12

def palindrome(a):
    """
    Returns Boolean assignment True or False to determine if word is palindrome.
    
    >>> palindrome('DogGOD')
    True
    >>> palindrome('RACE car')
    True
    >>> palindrome('allen')
    False
    >>> palindrome('PAul ruvOLo')
    False
    >>> palindrome('stanley YELnats')
    True
    """
    a = a.lower() #converts all characters in a to lowercase
    a = a.rstrip() #strips all spaces from a
    if len(a) <= 1:
        return True
    elif first(a) != last(a):
        return False
    return palindrome(middle(a))

#what do you know, it works
#fun with palindromes
palindrome('Borrow or Rob') #a moral dilemma
palindrome('Murder for a jar of red rum') #creepiest childhood game
palindrome('Yo Banana Boy') #it's Gabe
palindrome('satan oscillate my metallic sonatas') #that's unfortunate
palindrome('SolO GIGOLOS') #I am having altogether to much fun with this
palindrome('dammit Im mad')#lol not really but I bet whoever's reading this is
```

{: class="nb-output"}




    True




### Exercise 6.4  

A number $a$ is a power of $b$ if it is divisible by $b$ and $a/b$ is a power of $b$. Write a function called `is_power` that takes parameters `a` and `b` and returns `True` if `a` is a power of `b`. Note: you will have to think about the base case.


```python
# is_power solution 1

def is_power(a, b):
     if a < b: 
        return False
     if a == b: 
        return True
     else:
        return is_power(a / b, b)
```


```python
# is_power solution 2

def is_power(a,b):
    if a == b:
        return True
    elif a > b:
        if a%b == 0:
            return is_power(a//b,b)
        else:
            return False
    else:
        return False
```


```python
# is_power solution 3

def is_power(a,b):
    if a>b:
        if a%b == 0:
            return True
        if a%b != 0:
            return False
    return is_power(a/b,b)
```


```python
# is_power solution 4

def is_power(a,b):
    if a is b:
        return True
    elif a%b == 0:
        return is_power(a//b,b)
    else:
        return False
```


```python
# is_power solution 5

def is_power(a,b):
    """
    >>> is_power(4,2)
    True
    >>> is_power(3,2)
    False
    """
    if a == 1:
        return True
    return a%b == 0 and is_power(a/b, b)
```


```python
# is_power solution 6

def is_power(a,b):
    """returns whether a is a power of b.
    doctests test for a is zeroeth power, a is first power, a is nth power, and a is not power.
    >>> is_power(1, 70)
    True
    >>> is_power(5, 5)
    True
    >>> is_power(128, 2)
    True
    >>> is_power(132, 2)
    False
    """
    if a == 1:
        return True
    elif a % b == 0:
        return is_power(a//b,b)
    else:
        return False
```


```python
# is_power solution 7

def is_power(a,b):
    """ Returns True/False for if a is a power of b.
    >>> is_power(3,2)
    True
    >>> is_power(1,5)
    True
    >>> is_power(6,6)
    True
    >>> is_power(2,0)
    False
    >>> is_power(6,1)
    False
    >>> is_power(6,3)
    False
    """
    if a == 0 or b == 0:
        return False
    elif b == 1:
        if a == 1:
            return True
        else:
            return False
    
    if a==1 or (a/b)==1:
        result = True
    elif a % b == 0 and a!=0:
        result = is_power((a//b),b)
    else:
        result = False
  
    return result
```


```python
# is_power solution 8

def is_power(a, b):
    """
    Returns if A is a power of b. 
    
    >>> power(10, 2)
    False
    
    >>> power(32, 2)
    True
    
    """
    if not (a % b == 0):
        return False
    if a//b == 1:
        return True
    else:
        return power(a//b, b)
```


```python
# is_power solution 9

def is_power(a,b):
    if a == b:
        return True
    test1 = a%b
    a = a//b
    if test1 == 0 and is_power(a,b):
        return True
    else:
        return False
```


```python
# is_power solution 10

def is_power(a, b):
    if a % b == 0:
        if (a//b) % b == 0:
            return True
    return False
```


```python
# is_power solution 11

def is_power(a, b):
    if a%b != 0:
        return False
    else:
        return True
    c = a//b
    return is_power(c, b)
```


```python
# is_power solution 12

def is_power(a,b):
    if a%b == 0:
        if a == b:
            return True
        a = a//b
        return is_power(a,b)
    else:
        return False
```
