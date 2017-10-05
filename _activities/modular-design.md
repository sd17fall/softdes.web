---
title: Exploring modular design
description: Exploring modular design
---

In small groups, review the [solutions from the class](https://github.com/sd17fall/ReadingJournal-Solutions/blob/master/reading-journal-1-solutions.ipynb##Exercise-3.3) to the Exercise 3.3.

What aspects of these different designs:

* Increased / decreased the readability of code (readability means your ability to easily deduce what the code does, how it works, and whether or not it is correct).
* Increased / decreased the flexibility of the code (flexibility means the ability of this code to be easily modified to satisfy new requirements that may arise.

In groups, redo Chapter 3 Exercise 5 based on the design that your group
decides is most readable and most flexible.

In a surprise move, your manager has asked you to implement two new features
for your program.

1\. Write a function that draws the following grid

    + - - - - + - - - - + - - - - + - - - - + - - - - +
    |         |         |         |         |         |
    |         |         |         |         |         |
    |         |         |         |         |         |
    |         |         |         |         |         |
    + - - - - + - - - - + - - - - + - - - - + - - - - +
    |         |         |         |         |         |
    |         |         |         |         |         |
    |         |         |         |         |         |
    |         |         |         |         |         |
    + - - - - + - - - - + - - - - + - - - - + - - - - +
    |         |         |         |         |         |
    |         |         |         |         |         |
    |         |         |         |         |         |
    |         |         |         |         |         |
    + - - - - + - - - - + - - - - + - - - - + - - - - +

2\. Modify your function to take in two additional inputs that specify the
dimensions of width and height (in characters) of each of the boxes that
compose the grid. For instance,

`grid(6, 3)` produces

    + - - + - - + - - + - - + - - +
    |     |     |     |     |     |
    |     |     |     |     |     |
    + - - + - - + - - + - - + - - +
    |     |     |     |     |     |
    |     |     |     |     |     |
    + - - + - - + - - + - - + - - +
    |     |     |     |     |     |
    |     |     |     |     |     |
    + - - + - - + - - + - - + - - +
