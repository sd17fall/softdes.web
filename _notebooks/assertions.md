---
date: 2018-04-10T12:30:00-05:00
source: notebooks/assertions.ipynb
---

{% include toc %}


# Assertions


```python
def apply_penalty(assignment, penalty):
    grade = float(assignment['score'] * (1.0 - penalty))
    assert 0 <= grade <= assignment['score']
    return grade
```

This should guarantee that the grade is never lower than zero
and that the penalty did not generate a higher score.

This example should work fine to produce a penalized grade.

```python
# an example of a final project with a perfect score
>>> final = {'assignment': 'final project', 'score': 100}

# late by one day for a 10% penalty
>>> apply_penalty(final, 0.10)
90.0
```
That runs as expected.

But how about an 11 day late penalty for %110 percent off?

```python
# late by eleven days for a 110% penalty
>>> apply_penalty(final, 1.10)
Traceback (most recent call last):
  File "<input>", line 12, in <module>
    apply_penalty(final, 1.10)
  File "<input>", line 5, in apply_penalty
    assert 0 <= grade <= assignment['score']
AssertionError

# late by two days but a negative penalty input of -20%
>>> apply_penalty(final, -0.20)
Traceback (most recent call last):
  File "<input>", line 12, in <module>
    apply_penalty(final, -0.20)
  File "<input>", line 5, in apply_penalty
    assert 0 <= grade <= assignment['score']
AssertionError
```

The issues above fail as expected.

This example won't work for a different reason

```Python
def apply_penalty(assignment, penalty):
    grade = float(assignment['score'] * (1.0 - penalty))
    assert(0 <= grade <= assignment['score'], 'invalid grade')
    return grade
```

The parentheses give the assert statement a tuple.
It will not behave as expected.
