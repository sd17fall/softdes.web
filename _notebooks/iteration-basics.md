---
date: 2017-09-24T13:11:14-04:00
source: notebooks/iteration-basics.ipynb
---

{% include toc %}


# Iteration Basics

> From copy/paste to `for`

## Replacing Repeated Code by `for`

The following code prints all the characters of a string, one per line:


```python
text = "飛ぶ火鳥"

print(text[0])
print(text[1])
print(text[2])
print(text[3])
```

{: class="nb-output"}

    飛
    ぶ
    火
    鳥



Now let's replace "飛ぶ火鳥" by a longer string:


```python
text = "火鳥が飛んでいる"

print(text[0])
print(text[1])
print(text[2])
print(text[3])
```

{: class="nb-output"}

    火
    鳥
    が
    飛



This didn't quite work. It only printed the first four characters.

We added characters to the data, so we need to add lines to the code:


```python
text = "火鳥が飛んでいる"

print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])
print(text[6])
print(text[7])
```

{: class="nb-output"}

    火
    鳥
    が
    飛
    ん
    で
    い
    る



This is inconvenient. Each time we change the data, we have to change the code.

A `for` loop lets you write code that works with different lengths of data. Note that the code in the following two cells is the same. When it's run, it "re-shapes" itself to the data.


```python
text = "飛ぶ火鳥"

for c in text:
    print(c)
```

{: class="nb-output"}

    飛
    ぶ
    火
    鳥




```python
text = "火鳥が飛んでいる"

for c in text:
    print(c)
```

{: class="nb-output"}

    火
    鳥
    が
    飛
    ん
    で
    い
    る



## An Equivalence

`for c in text` is the same as doing this:


```python
text = "飛ぶ火鳥"

c = text[0]
print(c)
c = text[1]
print(c)
c = text[2]
print(c)
c = text[3]
print(c)
```

{: class="nb-output"}

    飛
    ぶ
    火
    鳥



except that with the `for` loop, Python figures out, while the program is running, how many times to repeat the

```python
c = text[…]
print(c)
```

block based on the length of `text`.

## From `while` to `for`

The following three programs are functionally equivalent.

See "Iteration Example" for an explanation of `range`, and discussion of the advantages of `for` over `while`.


```python
text = "飛ぶ火鳥"

i = 0
while i < len(text):
    c = text[i]
    print(c)
    i = i + 1
```

{: class="nb-output"}

    飛
    ぶ
    火
    鳥



Replacing `while` by `for`:


```python
text = "飛ぶ火鳥"

for i in range(len(text)):
    c = text[i]
    print(c)
```

{: class="nb-output"}

    飛
    ぶ
    火
    鳥



Iterating directly over the characters, instead of over the indices:


```python
text = "飛ぶ火鳥"

for c in text:
    print(c)
```

{: class="nb-output"}

    飛
    ぶ
    火
    鳥



## Using `enumerate` to read both the index and the item

The following programs are all functionally equivalent.

See "Iteration Example" for an explanation of `enumerate`.


```python
text = "飛ぶ火鳥"

i = 0
while i < len(text):
    c = text[i]
    print(i, c)
    i = i + 1
```

{: class="nb-output"}

    0 飛
    1 ぶ
    2 火
    3 鳥




```python
text = "飛ぶ火鳥"

for i in range(len(text)):
    c = text[i]
    print(i, c)
```

{: class="nb-output"}

    0 飛
    1 ぶ
    2 火
    3 鳥




```python
text = "飛ぶ火鳥"

for i_c in enumerate(text):
    i = i_c[0]
    c = i_c[1]
    print(i, c)
```

{: class="nb-output"}

    0 飛
    1 ぶ
    2 火
    3 鳥




```python
text = "飛ぶ火鳥"

for i_c in enumerate(text):
    i, c = i_c
    print(i, c)
```

{: class="nb-output"}

    0 飛
    1 ぶ
    2 火
    3 鳥




```python
text = "飛ぶ火鳥"

for i, c in enumerate(text):
    print(i, c)
```

{: class="nb-output"}

    0 飛
    1 ぶ
    2 火
    3 鳥


