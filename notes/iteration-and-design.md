

{% include toc %}


# Iteration and Design

> An exploration of Python iteration constructs, in the context of software design.
>
> This page covers the same programming language constructs as [Iteration Basics](iteration-basics), but adds principles for choosing between them, and relates them to concepts of software engineering.
>
> Standard terms from software engineering are written in **bold**.

## I. Data-Shaped Code

Let's print all the characters of a string, one per line:


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



### Changes to the Data

This code runs fine on this exact data (and on any other four-character string, such as "fire" or "burn"), but it's *fragile* – a slight change to the data will break it.

\[Terminology: Fragile is the opposite of **robust**. "Robustness" is one of the **non-functional** properties, or **design considerations**, of a design.\]

To see, this let's replace "飛ぶ火鳥" by a longer string:


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



Oops, what happened? Now we are only seeing the first four characters of the text.

That word *four* in the previous sentence is a hint. That's how many characters the first string had. We changed the *data*, but not the *code*, but our design requires that the code be kept in sync with the data (the number of lines of code must match the number of characters in the string).

This (almost) fixes it:


```python
text = "火鳥が飛んでいる"

print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])
print(text[5])
print(text[7])
```

{: class="nb-output"}

    火
    鳥
    が
    飛
    ん
    で
    で
    る



Now we've printed eight characters, one for each character of the string.

The code above still isn't correct, though. Can you spot the mistake?

You can find it either (1) by inspecting the code, or (2) by comparing the *input* (the data – in this case, the value of `text`) to the *output*.

It's easy to *make* this kind of mistake – I copied the code, and forgot to change a `5` to a `6`. It's difficult to *spot* it.

\[Terminology: it's easy to **inject** this category of **defect**. It's expensive to **detect** it.\]

### Changes to the Specification

The original specification was:

> Print all the characters of a string, one per line.

The customer has changed this to:

> Print all the characters of a string, one per line. Parenthesize each character.
>
> For example, if the string is "飛ぶ火鳥", the program should print `(飛)` on the first line, `(ぶ)` on the second line, and so on.

\[Aside: You'll noticed that I've supplemented the specification with an example. This is good technique for verifying that the author and reader of the specification understand it the same way. It can also reveal potential defects in the specification – if the specification and the examples don't agree, at least one of them is wrong. Specification examples are like [doctest](https://en.wikipedia.org/wiki/Doctest), for specifications – and can be used as fodder for the actual code tests.\]

Here's the code from the first cell, again:


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



And here I've modified the code to match the modified specification:


```python
text = "飛ぶ火鳥"

print('(' + text[0] + ')')
print('(' + text[1] + ')')
print('(' + text[2] + ')')
print('(' + text[3] + ')')
```

{: class="nb-output"}

    (飛)
    (ぶ)
    (火)
    (鳥)



So – this *works* (it meets the **functional requirements**), but it's not *robust*, as we've seen above.

Also, making a small change to the specification (adding the statement "parenthesize each character") required making a large change to the code (editing every line).

Another small change to the specification (adding "there should be a space between the parentheses and the characters, *e.g.* `( 飛 )`") would require editing every line of the code again.

\[Terminology: the code has low **extensibility**.\]

## II. Specification-Shaped Code

The advantage of the `for` statement, from [Iteration Basics](iteration-basics), is that it shapes the *lines* of code to the specification, and the *behavior* of the code to the data. (The versions above shaped the *lines* of code to the data.)

### First difference: The lines of code do *not* line up against the data

The behavior of the code comes from the data, but the lines of code themselves do not line up against the lines of data.

This means the same lines of code can re-shape themselves to different data:


```python
text = "飛ぶ火鳥"

# Print all the characters of a string, one per line.
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

# Print all the characters of a string, one per line.
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



### Second difference: the implementation *does* match the specification

The lines of code correspond closely to the specification:

>Print all the characters of a string, one per line.

"Print" in the specification corresponds to `print` in the code. "all the characters of the string" corresponds to `for c in text` in the code. It's not a *mechanical* translation, but it is relatively easy to check the code against the specification.


```python
text = "飛ぶ火鳥"

# Print all the characters of a string, one per line.
for c in text:
    print(c)
```

{: class="nb-output"}

    飛
    ぶ
    火
    鳥



This also means that a simple (local) change to the specification requires only a local change to the implementation.


```python
text = "飛ぶ火鳥"

# Print all the characters of a string, one per line.
for c in text:
    print('(' + c + ')')
```

{: class="nb-output"}

    (飛)
    (ぶ)
    (火)
    (鳥)



## Appendix: Trade-Offs

The implementation that uses `for` is more **general** and more **abstract** than the implementation that uses a different line to write each character.

It's more *general* because it works on a wider variety of inputs, without change.

It's more *abstract* because the relationship between the data, the implementation, and the output is *less direct*. (That's what we give up by making the relationship between specification and the implementation *more* direct.) In the original implementation, a single line of code operated on a single piece of the input (a character) to produce a single piece of output (a line containing that character). In the final implementation, a single line operates on all the pieces of the input, behaving differently (printing a different character) on each piece. 

Generality and abstraction aren't all sunshine and roses. ("Engineering is the navigation of trade-offs.")

1. The relation between the *lines of code* and the *output* is more abstract. Which line in the original program (at the top of this page, without the `for` statement) was responsible for printing just the second character of the string? Which line in the final code program is?

2. It's more difficult to make exceptions. Consider the following specification. How would you change the original program to do this? How would you change the final program?

> Print all the characters of a string, one per line. Parenthesize each character except the second.
>
> For example, if the string is "飛ぶ火鳥", the program should print (飛) on the first line, ぶ on the second line, `(火)` on the third line, and so on.
