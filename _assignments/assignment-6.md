---
title: Assignment 6
due: 2017-09-25 10:50:00 -04:00
---

* Read *Think Python* [Chapter 5.8-5.14](http://www.greenteapress.com/thinkpython2/html/thinkpython2006.html)
* Study the diagnostic code below:

You should understand why the following script prints what it does by Monday.
Study it with Python Tutor, a classmate, or a NINJA.

```python
def fn1(a):
    print("inside fn1, a =", a)

def fn2(a):
    print("inside fn2, a =", a)
    fn1("from fn2")

a = "global"
print("at the top level, before the function calls, a =", a)
fn1("from top-level call to fn1")
fn2("from top-level call to fn2")
print("at the top level, after the function calls, a =", a)
```
