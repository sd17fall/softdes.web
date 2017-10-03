---
omit_title: true
---

{% include toc %}


# Iteration Example

> **Detailed design ~ Control flow ~ `while` and `for` ~ `range` ~ Relating design to implementation ~ Nested loops ~ Functions – an alternative ~ `enumerate`**

Let's write a script that computes the number of letters in the words in a list. For example, if the list has the words "fabulous", "flying", and "phoenix", the number of letters is 8 + 6 + 7 = 21.

Here's a **detailed design** (or **low-level design**) that is intended to satisfy this specification:

1. For each word in the list:
  1. Count its letters
  2. Add that count to a running total
2. Return the total

Let's implement this design using `while` and `break`:


```python
words = ["fabulous", "flying", "phoenix"]

letter_count = 0
i = 0
while True:
    w = words[i]
    letter_count = letter_count + len(w)
    i = i + 1
    if i >= len(words):
        break
print("these words total", letter_count, "letters")
```

{: class="nb-output"}

    these words total 21 letters



Note how many *places* and *ways* the variable `i` is used. I've labelled these with comments below.


```python
words = ["fabulous", "flying", "phoenix"]

letter_count = 0
i = 0                    # <- initialize
while True:
    w = words[i]         # <- index
    letter_count = letter_count + len(w)
    i = i + 1            # <- increment
    if i >= len(words):  # <- test
        break
print("these words total", letter_count, "letters")
```

{: class="nb-output"}

    these words total 21 letters



Also note the **control flow** – which parts of the code decide how many times the loop is executed; equivalently in this case, for each line of code, what happens next.


```python
words = ["fabulous", "flying", "phoenix"]

letter_count = 0
i = 0
while True:              # <- loop for ever – but not really, because:
    w = words[i]
    letter_count = letter_count + len(w)
    i = i + 1
    if i >= len(words):
        break            # <- terminate the loop
print("these words total", letter_count, "letters")
```

{: class="nb-output"}

    these words total 21 letters



This implementation distributes a single idea ("for each word in the list") from the design, across a number of different places in the implementation. It makes it difficult to match the implementation to the specification, and see if they describe the same process.

"For each word" is split into pieces, and woven into different parts of the script.

It's also hard to read off where the `while` loop terminates. It looks from the `while` line like it goes on forever; you have to read to the end of its body to find the `break`, hidden inside of an `if`.

We can reduce the number of different places that the implementation of "For each word" pops up, and also making the control flow more readable, by moving the termination condition into the `while` test:


```python
words = ["fabulous", "flying", "phoenix"]

letter_count = 0
i = 0                  # <- initialize
while i < len(words):  # <- test and terminate
    w = words[i]       # <- index
    letter_count = letter_count + len(w)
    i = i + 1          # <- increment
print("these words total", letter_count, "letters")
```

{: class="nb-output"}

    these words total 21 letters



### `for` and `range`

We can go one step further by replacing `while`, with `for` and `range`.

First, let's review how `range` works.

`range` returns a sequence that acts like `[0, 1, 2, 3]`, except we don't have to know when we write the code how long the list should be.

(The value returned by `range` only acts behaves as a list, it isn't an actual list. This works fine in a `for` loop, but it means that `print` isn't completely helpful for learning about it. We'll work around this by applying the `list` function to the value returned by `range`. This creates the list that the range value behaves like.)


```python
print("len(words) =", len(words))
print("range(3) =", range(3))
print("range(3) behaves as", list(range(3)))
print("range(len(words)) behaves as", list(range(len(words))))
```

{: class="nb-output"}

    len(words) = 3
    range(3) = range(0, 3)
    range(3) behaves as [0, 1, 2]
    range(len(words)) behaves as [0, 1, 2]



`for` introduces a variable (just like `=` does), assigns it the first item in a sequence (just like `i = range(len(words))[0]` would), and runs the body of the loop (just like `while` does). Then it assigns the variable the *next* item in the sequence, and runs the loop again.

```python
for item in lst:
  # code
```

is just the same as:

```python
i = 0
while i < len(lst):
    # code
    i = i + 1
```

except that Python takes care of managing `i` for us.


```python
words = ["fabulous", "flying", "phoenix"]

letter_count = 0
for i in range(len(words)): # <- initialize, increment, test, and terminate
    w = words[i]            # <- index
    letter_count = letter_count + len(w)
print("these words total", letter_count, "letters")
```

{: class="nb-output"}

    these words total 21 letters



Now "For each word" only pops up in two places: in the `for` line where `i` is *assigned* etc., and in `w = words[i]` where we *use* it.

We can do one better. Instead of using `for` to iterate over the indices – which we only need in order to get the words of the list – we can iterate over the words themselves.


```python
words = ["fabulous", "flying", "phoenix"]

letter_count = 0
for w in words: # <- initialize, index, increment, test, and terminate
    letter_count = letter_count + len(w)
print("these words total", letter_count, "letters")
```

{: class="nb-output"}

    these words total 21 letters



Compare "For each word" from the *specification*, to `for w in words` from the *implementation*. This is a much closer match.

Something to strive for in your programs is an implementation whose structure matches the specification and the design. Sometimes this involves creating functions that matches words of the specification. (This is where "Growing a Language" comes in.) Sometimes it involves re-thinking the design – is there a clearer way to say the same thing, that lends itself better to coding.

## Nested Loops

The refinement above reduced the number of lines of code, and it reduced the number of "bookkeeping" variables.

Each line of code is a home for bugs to breed. Each place a variable is used, is an opportunity to use the wrong variable – and therefore introduce a bug.

The rest of this section illustrates this.

Consider this new specification:

> Given a list of words, compute the number of vowels in all the words.

This is very similar to the original specification, so we'll start with that.

Return for a moment to our *original* implementation of the letter counter:


```python
words = ["fabulous", "flying", "phoenix"]

letter_count = 0
i = 0                    # <- initialize
while True:
    w = words[i]         # <- index
    letter_count = letter_count + len(w)
    i = i + 1            # <- increment
    if i >= len(words):  # <- test
        break            # <- terminate
print("these words total", letter_count, "letters")
```

Here's code to count the vowels in a single word:


```python
word = "fabulous"

vowel_count = 0
i = 0
while i < len(word):
    c = word[i]
    if c in 'aeiouy':
        vowel_count = vowel_count + 1
    i = i + 1
print(word, "contains", vowel_count, "vowels")
```

{: class="nb-output"}

    fabulous contains 4 vowels



We can combine the previous two cells (sum the number of letters in all the word, count the number of vowels in a single word) into a single script:

There's a couple of gotchas:

1. The first script uses `w` for the word. The second script uses `word`. We need to either rename `w` to `word` in the first script, or `word` to `w` in the second script. (We'll do the second.)
2. The first script uses `i` to index into the list of words. The second script uses `i` to index into the characters within a single word. We need to rename one of these variables. (We'll rename `i` in the second script to `j`.) Be careful to rename *all* the occurrences of `i` in the second script.

The modified vowel-counter looks like this:


```python
w = "fabulous"

vowel_count = 0
j = 0
while j < len(w):
    c = w[j]
    if c in 'aeiouy':
        vowel_count = vowel_count + 1
    j = j + 1
print(w, "contains", vowel_count, "vowels")
```

And putting them together:


```python
words = ["fabulous", "flying", "phoenix"]

vowel_count = 0
i = 0                    # <- outer initialization
while i < len(words):    # <- outer test
    w = words[i]         # <- outer index
    j = 0                  # <- inner initialization
    while j < len(w):      # <- inner test
        c = w[j]           # <- inner index
        if c in 'aeiouy':
            vowel_count = vowel_count + 1
        j = j + 1          # <- inner increment
    i = i + 1            # <- outer increment
print("these words have", vowel_count, "vowels in all")
```

{: class="nb-output"}

    these words have 9 vowels in all



In practice, it's very hard to do this reliably. References to `i` are mixed with references to `j`, and it's easy to slip up.

See if you can spot the problem with the following script. This script never terminates.


```python
words = ["fabulous", "flying", "phoenix"]

vowel_count = 0
i = 0                    # <- outer initialization
while i < len(words):    # <- outer test
    w = words[i]         # <- outer index
    j = 0                  # <- inner initialization
    while j < len(w):      # <- inner test
        c = w[j]           # <- inner index
        if c in 'aeiouy':
            vowel_count = vowel_count + 1
        i = i + 1          # <- inner increment OR IS IT?
    i = i + 1            # <- outer increment
print("these words have", vowel_count, "vowels in all")
```

Now let's switch to our final implementation of the letter counter, that used `range`:


```python
words = ["fabulous", "flying", "phoenix"]

letter_count = 0
for w in words: # <- initialize, index, increment, test, and terminate
    letter_count = letter_count + len(w)
print("these words total", letter_count, "letters")
```

{: class="nb-output"}

    these words total 21 letters



Here's a vowel counter that also uses `range`:


```python
word = "fabulous"

vowel_count = 0
for c in word:
    if c in 'aeiouy':
        vowel_count = vowel_count + 1
print(word, "contains", vowel_count, "vowels")
```

{: class="nb-output"}

    fabulous contains 4 vowels



It's much easier to fuse these two cells. We still need to rename `word` in the vowel counter to `w`, but there's no colliding loop counters such as `i` and `j` the last time we tried this.


```python
words = ["fabulous", "flying", "phoenix"]

vowel_count = 0
for w in words: # <- outer initialize, index, increment, test, and terminate
    for c in w:
        if c in 'aeiouy': # <- inner initialize, index, increment, test, and terminate
            vowel_count = vowel_count + 1
print("these words have", vowel_count, "vowels in all")
```

{: class="nb-output"}

    these words have 9 vowels in all



### Another Approach: Functions

You might have noticed there's another way to compose *units of functionality*, such as "do something to each word in list" and "count vowels in a word". That's to compose *functions*.

Returning once again to our original implementations of "sum the lengths of the words" and "count the vowels in a single word", let's turn each of these scripts into a function:


```python
def count_letters_in_word_list(words):
    count = 0
    i = 0
    while True:
        w = words[i]
        count = count + len(w)
        i = i + 1
        if i >= len(words):
            break
    return count

print("these words total", count_letters_in_word_list(["fabulous", "flying", "phoenix"]), "letters")
```

{: class="nb-output"}

    these words total 21 letters




```python
def count_vowels(word):
    vowel_count = 0
    i = 0
    while i < len(word):
        c = word[i]
        if c in 'aeiouy':
            vowel_count = vowel_count + 1
        i = i + 1
    return vowel_count

print(word, "contains", count_vowels("fabulous"), "vowels")
```

{: class="nb-output"}

    fabulous contains 4 vowels



We combine them by changing `count_letters_in_word_list` to call `count_vowels` instead of `len`. (I've also renamed the function `count_letters_in_word_list` to `count_vowels_in_word_list`.)


```python
def count_vowels_in_word_list(words):  # <- renamed the function
    count = 0
    i = 0
    while True:
        w = words[i]
        count = count + len(w)   # <- this is the only other change
        i = i + 1
        if i >= len(words):
            break
    return count

print("these words have", count_vowels_in_word_list(["fabulous", "flying", "phoenix"]), "vowels in all")
```

{: class="nb-output"}

    these words have 21 vowels in all



We could change the implementation of `count_vowels` without changing `count_vowels_in_word_list`.

We could also change the implementation of `count_vowels_in_word_list` without changing `count_vowels`.

We can mix and match: any correct implementation `count_vowels` works with any correct implementation of `count_vowels_in_word_list`.

Separating these units of *functionality* into separate *functions* therefore insulates them from each other in a way that fusing them into a single script can't do.


```python
def count_vowels(word):
    vowel_count = 0
    for c in word:
        if c in 'aeiouy':
            vowel_count = vowel_count + 1
    return vowel_count

print(word, "contains", count_vowels("fabulous"), "vowels")
```

{: class="nb-output"}

    fabulous contains 4 vowels




```python
def count_vowels_in_word_list(words):
    count = 0
    for w in words:
        count = count + count_vowels(w)
    return count

print("these words have", count_vowels_in_word_list(["fabulous", "flying", "phoenix"]), "vowels in all")
```

{: class="nb-output"}

    these words have 9 vowels in all



## `enumerate` provides the index *and* the item

Let's return to the original brief – count the letters in all the words – and add a requirement:

Print the number of letters in each word, indexed by position.

For example, if the list has "fabulous", "flying", and "phoenix", the script should print:

    word #1 has 8 letters
    word #2 has 6 letters
    word #3 has 7 letters
    these words total 21 letters

Having seen the advantages of `for w in words`, 


```python
words = ["fabulous", "flying", "phoenix"]

letter_count = 0
for w in words:
    n = len(w)
    print("word #{} has {} letters".format(i + 1, n))
    letter_count = letter_count + n
print("these words total", letter_count, "letters")
```

{: class="nb-output"}


    ----------------------------------------------------------------------

    NameError                            Traceback (most recent call last)

    <ipython-input-54-7df716470494> in <module>()
          4 for w in words:
          5     n = len(w)
    ----> 6     print("word #", i + 1, "has", n, "letters")
          7     letter_count = letter_count + n
          8 print("these words total", letter_count, "letters")


    NameError: name 'i' is not defined



Oops! `for w in words` doesn't give us an index variable, just the item itself. This was an advantage because we didn't have to manage the index variable, but it's a disadvantage if we actually want it.

We could create our own index variable to keep track of where we are within the list:


```python
words = ["fabulous", "flying", "phoenix"]

letter_count = 0
i = 0
for w in words:
    n = len(w)
    print("word #{} has {} letters".format(i + 1, n))
    i = i + 1
    letter_count = letter_count + n
print("these words total", letter_count, "letters")
```

{: class="nb-output"}

    word #1 has 8 letters
    word #2 has 6 letters
    word #3 has 7 letters
    these words total 21 letters



But now we're using two different mechanisms to traverse the same list at the same pace: the `for` loop with `w`, and our own `i`. Maybe it's better to iterate over the indices instead of the words:


```python
words = ["fabulous", "flying", "phoenix"]

letter_count = 0
for i in range(len(words)):
    w = words[i]
    n = len(w)
    print("word #{} has {} letters".format(i + 1, n))
    letter_count = letter_count + n
print("these words total", letter_count, "letters")
```

{: class="nb-output"}

    word #1 has 8 letters
    word #2 has 6 letters
    word #3 has 7 letters
    these words total 21 letters



This is acceptable, but it's galling to have to go back to iterating over indices just to get to the words. And this is a very common requirement.

An alternative is the `enumerate` function, which generates a sequence of pairs: (index, item).

(The value `(0, 'fabulous')` is a *tuple*. It behaves the same as the list `[0, 'fabulous']`, for our purposes.)


```python
print("enumerate(words) =", enumerate(words))
print("enumerate(words) behaves as", list(enumerate(words)))
```

{: class="nb-output"}

    enumerate(words) = <enumerate object at 0x106a9f948>
    enumerate(words) behaves as [(0, 'fabulous'), (1, 'flying'), (2, 'phoenix')]




```python
words = ["fabulous", "flying", "phoenix"]

letter_count = 0
for index_and_word in enumerate(words):
    i = index_and_word[0]
    w = index_and_word[1]
    n = len(w)
    print("word #{} has {} letters".format(i + 1, n))
    letter_count = letter_count + n
print("these words total", letter_count, "letters")
```

{: class="nb-output"}

    word #1 has 8 letters
    word #2 has 6 letters
    word #3 has 7 letters
    these words total 21 letters



This can be simplified using the shortcut `a, b = pair`, which is equivalent to `a = pair[0]; b = pair[1]` if `pair` is a list or tuple with length 2.


```python
words = ["fabulous", "flying", "phoenix"]

letter_count = 0
for index_and_word in enumerate(words):
    i, w = index_and_word
    n = len(w)
    print("word #{} has {} letters".format(i + 1, n))
    letter_count = letter_count + n
print("these words total", letter_count, "letters")
```

{: class="nb-output"}

    word #1 has 8 letters
    word #2 has 6 letters
    word #3 has 7 letters
    these words total 21 letters



This can further be simplified by replacing `index_and_word` by `i, w`, instead of assigning them from it later.


```python
words = ["fabulous", "flying", "phoenix"]

letter_count = 0
for i, w in enumerate(words):
    n = len(w)
    print("word #{} has {} letters".format(i + 1, n))
    letter_count = letter_count + n
print("these words total", letter_count, "letters")
```

{: class="nb-output"}

    word #1 has 8 letters
    word #2 has 6 letters
    word #3 has 7 letters
    these words total 21 letters


