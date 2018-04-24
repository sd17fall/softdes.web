---
date: 2018-02-06T13:11:49-05:00
source: notebooks/Day 4 Reading Journal Notes.ipynb
---

{% include toc %}


### Day 4 Reading Journal Notes

### Exercise 4  
Write a function called `middle` that takes a list and returns a new list that contains all but the first and last elements. So `middle([1,2,3,4])` should return `[2,3]`.

#### The most common answer


```python
def middle(s):
    return s[1:len(s)-1]

middle([1,2,3,4,])
```

{: class="nb-output"}




    [2, 3]




#### A more cumbersome method, but works?


```python
def middle(lst):
    new = []
    for x in range(0, len(lst)):
        new.append(lst[x])
    new.remove(new[0])
    new.remove(new[-1])
    return new
print(middle([1,2,3,4]))
print(middle([1,5,3,4]))
```

{: class="nb-output"}

    [2, 3]
    [5, 3]



#### Careful about return types: `[[2, 3]] != [2,3]`


```python
def middle (random_list):
    new_list = []
    for element in random_list:
        new_list = [random_list[1:-1]]
    return new_list

middle([1,2,3,4])
```

{: class="nb-output"}




    [[2, 3]]




### Improving readability

Variable names and a docstring.


```python
def middle(first_list):
    """
    Takes a list and returns all but the first and the last elements.
    """
    last_index = len(first_list) - 1
    new_list = first_list[1:last_index] #this all could be one line but I like readability
    return new_list

my_list = [1,2,3,4]
print(middle(my_list))
print(my_list)
```

{: class="nb-output"}

    [2, 3]
    [1, 2, 3, 4]



#### Is this one correct?

How can we write a unit test?


```python
def middle(Input):
    """
    Given a list, return a new list that contains all but the first and last elements.
    
    >>> L = [1, 2, 3, 4, 5]
    >>> print(L)
    [1, 2, 3, 4, 5]
    >>> print(middle(L))
    [2, 3, 4]
    >>> print(L)
    [1, 2, 3, 4, 5]
    """
    if len(Input)>1:

        List = Input
        del List[0]
        del List[-1]
    
        return List
    else:
        
        return "List is too short."

import doctest
doctest.run_docstring_examples(middle, globals(), verbose=False)

#middle(['a', 'b'])
#middle(['a'])
```

Quick fix: make a copy of the input list using a slice:  `List = Input[:]`

#### Using the copy module

Slices are another way to go, but this will work.


```python
original_list = [1, 2, 3, 4, 5]

import copy
def middle(original_list):
    copied_list = []
    copied_list = copy.copy(original_list)
    del copied_list[0]
    del copied_list[-1]
    
    print(original_list)
    print(copied_list)
    return copied_list
    
middle(original_list)
```

{: class="nb-output"}

    [1, 2, 3, 4, 5]
    [2, 3, 4]





    [2, 3, 4]




#### Another correct solution, this one using pop


```python
def middle(l):
    new_list = l[:]
    new_list.pop(0)
    new_list.pop(len(new_list)-1)
    print(l)
    return new_list

middle([1,2,'ads',2,35,6,63])
```

{: class="nb-output"}

    [1, 2, 'ads', 2, 35, 6, 63]





    [2, 'ads', 2, 35, 6]




#### Careful with Variable Names


```python
def middle(list):
    new_list = list[1:len(list)-1]
    return new_list
print(middle([9,2,7,1,4]))
```

{: class="nb-output"}

    [2, 7, 1]



#### Another way to make a copy of a List???


```python
def middle(L):
    res = list(L)
    res.pop(0)
    res.pop(-1)
    return res

print(middle([1,2,3,4]))
print(middle([2,"hello",5,'Hi']))
```

### Exercise 5  
Write a function called `chop` that takes a list, modifies it by removing the first and last elements, and returns `None`.

What is the difference between `middle` and `chop`? Sketch out the program state or take a look at each in Python Tutor.

#### This looks okay, but we haven't really tested it yet

How can we see whether or not this is correct?


```python
def chop(lst):
    lst = lst[1:len(lst)-1]
L = [1, 2, 3, 4]
chop(L)
print(L)
```

{: class="nb-output"}

    [1, 2, 3, 4]



To better understand what is happening here we will draw some state diagrams and stack diagrams.

#### This seems better, is it correct?


```python
def chop(list):
    list.remove(list[0])
    list.remove(list[-1])
    return None
middle([1,2,3,4])
```

#### How about this one?

We have a minor quibble over variable names.


```python
def chop(list_numbers):
    del list_numbers[0]
    del list_numbers[-1]
    print(list_numbers)
    
chop([1,2,3,4])
```

{: class="nb-output"}

    [2, 3]



#### del can also handle list slices


```python
X = [3,6,3,8,0,2,5]
def chop(List):
    del List[:1]
    del List[-1:]
    
print(chop(X))
print(X)
```

{: class="nb-output"}

    None
    [6, 3, 8, 0, 2]



### Exercise 7  
Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function called `is_anagram` that takes two strings and returns `True` if they are anagrams.

#### Let's decide if each of these is correct

Minor issue with doctest here.  Let's run it with verbose = True


```python
def is_anagram(string_one, string_two):
    """
    Takes input two strings and returns True is they are anagrams
    
    >>> is_anagram("car", "arc")
    True
    >>> is_anagram("blah", "nope")
    False
    """
    if len(string_one) == len(string_two):  # words are the same length
        for letter in string_one:
            if letter in string_two:
                return True
        return False

import doctest
doctest.run_docstring_examples(is_anagram, globals(), verbose=False)
```

Passes tests, but we don't have enough coverage. For example, what if we add:

```
    >>> is_anagram("cat", "cap")
    False
    >>> is_anagram("ab", "aaaab")
    False
```


```python
def is_anagram(o,t):
    """
    >>> is_anagram("ab", "aaaab")
    False
    """
    if o.strip(t) == '':
        return True
    else:
        return False

is_anagram('banana','popcorn')
is_anagram('banana','nabana')

import doctest
doctest.run_docstring_examples(is_anagram, globals(), verbose=True)
```

{: class="nb-output"}

    Finding tests in NoName
    Trying:
        is_anagram("ab", "aaaab")
    Expecting:
        False
    **********************************************************************
    File "__main__", line 3, in NoName
    Failed example:
        is_anagram("ab", "aaaab")
    Expected:
        False
    Got:
        True




```python
def is_anagram(string1, string2):
    """
    This function will use the split and sort command to check to see whether one string contains all the letters of the other string.
    
    >>> is_anagram('z', 'z')
    True
    >>> is_anagram('c', 'b')
    False
    >>> is_anagram('earth','heart')
    True
    >>> is_anagram('chicken','butt')
    False
    """
    
    string1_list = list(string1)
    string1_list.sort()
    string2_list = list(string2)
    string2_list.sort()
    
    for i in range(len(string1_list)):
        if not string1_list[i] == string2_list[i]:
            return False
    return True    



doctest.run_docstring_examples(is_anagram, globals(),verbose=True)  
```

{: class="nb-output"}

    Finding tests in NoName
    Trying:
        is_anagram('z', 'z')
    Expecting:
        True
    ok
    Trying:
        is_anagram('c', 'b')
    Expecting:
        False
    ok
    Trying:
        is_anagram('earth','heart')
    Expecting:
        True
    ok
    Trying:
        is_anagram('chicken','butt')
    Expecting:
        False
    ok




```python
def anagrams(first, second):
    """
    >>> anagrams("ab", "aaaab")
    False
    """

    if len(first) == len(second):
        for i in range(0,len(second)):
            if first[i] in second:
                continue
            else:
                return False
    else:
        return False 
    return True

doctest.run_docstring_examples(anagrams, globals(),verbose=True)  
#anagrams('apple', 'paple')
```

{: class="nb-output"}

    Finding tests in NoName
    Trying:
        anagrams("ab", "aaaab")
    Expecting:
        False
    ok




```python
def is_anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    for letter in string1:
        if letter not in string2:
            return False
    for letter in string2:
        if letter not in string1:
            return False
    return True

print(is_anagram('dog', 'god'))
print(is_anagram('dog', 'cat'))
print(is_anagram('dogg', 'doog')) #lolnope
```


```python
def is_anagram (x, y): 
    list_a = []   #Converting from a string to a list
    list_b = []   #For both x and y. 
    
    for i in x:
        list_a.append(i) #Putting the elements of the string x into list a.
    
    for i in y:
        list_b.append(i) #Putting the elements of the string y into list b.
        
    #This part was checked with a print statement.
 
    list_a.sort() #Modifies the list itself, does not return a value. 
    list_b.sort() #But for both, this function arranges the letters so that if it were an anagram they would be in the same order, which is from least to greatest in terms of their place in the alphabet.
    
    if list_a == list_b: #Rhis if statement compares the resulting lists from list sort. If they are the same, they contain the same letters, which would mean the words are anagrams. 
        ret`urn True 
    else:
        return False
    
is_anagram ('love','vole')
```


```python
def is_anagram (x,y):
    x = list(x)
    y = list(y)
    x.sort()
    y.sort()
    if x == y:
        return True


is_anagram('bat', 'tab')
```


```python
def anagrams(String1, String2):
    """
    Given two string inputs, checks to see if they are anagrams.
    >>>anagrams('tab', 'bat')
    True
    >>>anagrams('lad', 'bad')
    False
    """
    for letter in String1:
        if letter in String2:
            return True
        else:
            return False
        
anagrams('tab', 'bad')
import doctest
doctest.run_docstring_examples(chop, globals())
```


```python
def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    l2 = list(s2)
    for letter in s1:
        if letter in l2:
            l2.remove(letter)
        else:
            return False
    if len(l2) == 0:
        return True
    else:
        return False

is_anagram('iceman    ', 'cinema')
```

#### Based on these answers, what is a good comprehensive list of unit tests?

### Exercise 8  
The (so-called) Birthday Paradox:
1. Write a function called `has_duplicates` that takes a list and returns `True` if there is any element that appears more than once. It should not modify the original list.
2. If there are 23 students in your class, what are the chances that two of you have the same birthday? You can estimate this probability by generating random samples of 23 birthdays and checking for matches. Hint: you can generate random birthdays with the randint function in the [random module](https://docs.python.org/2/library/random.html).

You can read about this problem at http://en.wikipedia.org/wiki/Birthday_paradox, and you can download Allen's solution from http://thinkpython.com/code/birthday.py.

Most of the interesting differences here were in the has_duplicates function.  Let's start there, and then look at a few people's complete code.


```python
def has_duplicates(lst):
    newlist = []
    for e in lst:
        if e in newlist:
            return True
        else:
            newlist.append(e)
    return False
```


```python
def has_duplicates(g):
    number = 0
    for birthday in g:   #run through every birthday
        for others in g:    #run throguh the other birthdays
            if birthday == others:   #how many bdays does it match?
                number += 1
        #print number
    if number > len(g):     #if the number is greater than 23
        return True         #then there was at least one duplicate
    else:
        return False
```


```python
def has_duplicates(input_list):
    check = []
    for i in input_list:
        if i not in check:
            check.append(i)
    if len(check) < len(input_list):
        return True
    else:
        return False
```


```python
def has_duplicates(list_things):
    list_things.sort()
    flag = False
    for index in range(1, len(list_things)):
        flag = flag or list_things[index] == list_things[index-1]
    return flag
            
has_duplicates([0,1,2,4, 3, 3, 3])
```

Careful with variable scope.


```python
def has_duplicates(random_list):
    birthdays_sorted = sorted(birthdays)
    for i in range(1,len(random_list)):
        if random_list[i-1] == random_list[i]:
            return True
    return False
```


```python
def has_duplicates(my_list):
    """
    Checks for duplicates in a list
    """
    for i in range(len(my_list)):
        if my_list[i] in my_list[i + 1:]:
            return True
    return False
```


```python
def has_duplicates(birthdays):
    """
    >>> has_duplicates([1,2,3,3,4])
    True
    >>> has_duplicates(["one","two","banana"])
    False
    """
    for i in range(0,len(birthdays)):
        for j in range(0,i):
            if birthdays[i] == birthdays[j]:
                return True
    return False
```

What do we think about the line `items = l[:]`


```python
import random

def has_duplicates(l):
    """
    Tests if a list contains duplicate values. Returns True if so.
    
    >>> has_duplicates([1,2,3,4,5])
    False
    >>> has_duplicates([1,2,3,4,2])
    True
    
    """
    items = l[:]
    items.sort()
    i = 1
    while i < len(items):
        if items[i] == items[i-1]:
            return True
        i += 1
    return False

def generate_birthdays(length):
    """
    Generates a list of random integers between 1 and 365.
    """
    result = []
    for i in range(length):
        result.append(random.randint(1, 365))
    return result

def probability_of_duplicates(n):
    """
    Empirically estimates the chance that a group of n people will
    contain at least one pair with the same birthday.
    """
    count = 0
    for i in range(1000):
        birthdays = generate_birthdays(n)
        if has_duplicates(birthdays):
            count += 1
    return count/1000.

print(probability_of_duplicates(23))

import doctest
doctest.testmod()
```

{: class="nb-output"}

    0.511





    TestResults(failed=0, attempted=2)





```python
import random

def has_duplicates(t):
    element_tracker = []
    for item in t:
        if item in element_tracker:
            return True
        element_tracker.append(item)
    return False

i = 0
j = 0
birthdays = []
duplicates = []

while i < 100:
    while j < 23:
        birthdays.append(random.randint(0,365)) #birthday represented as one of 365 days
        j += 1
    
    duplicates.append(has_duplicates(birthdays))
    birthdays = []
    i += 1
    j = 0

print(duplicates.count(True)) #Should be ~50
```
