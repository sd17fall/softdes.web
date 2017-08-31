# Activity 1.1 – Get Started with Python

## 1. Install Python

Visit the class web site <http://sd17fall.olin.build>. (Bookmark this while you're there.)

Find the “Set Up” page.

Follow the instructions under “Step 1: Install Python”.

## 2. Open a Terminal Window

In this course you will make use of the **Terminal** program in Linux or macOS, or **Command Prompt** in Windows:

**Linux**: Press cmd+alt+T, or launch the Terminal from your Programs menu.

**macOS**: Open the Terminal application, in the Applications folder.

**Windows**: Open the Command Prompt. If this is unfamiliar to you, ask a classmate or NINJA, or search the web for “windows 10 command prompt”.

Launching Terminal or Command Prompt is called “creating a terminal session”.

Typing into a terminal session is called “in a terminal session”, “in a terminal”, or “in the shell”

 Typing some text – such as `ls` (Linux or macOS) or `dir` (Windows) – and then pressing the Enter or Return key, is called “entering *command*“ or “running *command*”, where *command* is the entered text.

## 3. Explore Python

Enter `python`. This starts the **python interpreter**.

You should see something like this:

```
Python 3.6.2 (default, Jul 17 2017, 16:44:45)
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Details such as the date, and the material inside brackets `[…]` will differ. The first line should say `Python 3.6.x` where `x` is some digit; if it says `Python 2.x.y` check in with a NINJA.

The chevron's `>>>` are Python's **prompt**. Python is waiting for you to type something. Type `42` and press Enter. You should see something like:

```
>>> 42
42
```

Now type `40 + 2`:

```
>>> 40 + 2
42
```

Try out using Python as a calculator:

* How many minutes are in a day?
* How many seconds are in a day?
* How many seconds are in a year?
* About how many minutes is 1000 seconds?
* How many minutes old are you?

## 3. Investigation

*Do this in groups of two.*

* Do parentheses `()` and brackets `[]` work the same way as in math notation?
* Does an expression need to be on one line? Does it matter whether it includes parentheses?
* Are spaces (“whitespace”) significant? Is there difference between `40+2`, `40 + 2`, and `40     +2` (where the long space is a tab)?
* What happens if you type something non-sensical, such as `40 + + 2`?
* Skim [this page on **PEMDAS**](https://www.mathsisfun.com/operation-order-pemdas.html). Use the interpreter to investigate whether Python follows PEMDAS. (Python uses `**` for exponentiation, e.g. $5^2$ is written `5 ** 2` .)

## 4. Quitting Python

To quit Python, enter `quit()` or press control+d (hold the control key; press the `d` key; and then release them in either order).

## Going Beyond

*We will get to these topics later in the course. You can try these now if you finish early.*

Here's some other things you can try:

* **Strings** begin and end with `'` or `"`: `'hello'`, or `"hello"`. Try entering a string at the Python prompt.
* What operations can you do with strings? Can you add, subtract, or multiply them? With strings and numbers?
* Use the web to find out whether you can enter complex numbers into Python.
* How many numbers can you make with the digits `0` through `9` (at most once each), and the arithmetic operators?
