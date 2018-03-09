---
date: 2018-03-09T11:35:58-05:00
source: notebooks/Inheritance Counters and PMFs.ipynb
---

{% include toc %}


# Inheritance

This notebook demonstrates the use of inheritance to extend Python's `Counter` class to implement Multisets, PMFs, and suites of Bayesian hypotheses.


```python
from __future__ import print_function, division

from collections import Counter
import numpy as np
```

### Counter

A `Counter` is a map from values to their frequencies.  If you initialize a `Counter` with a string, you get a map from each letter to the number of times it appears.  If two words are anagrams, they yield equal Counters, so you can use Counters to test anagrams.


```python
def is_anagram(word1, word2):
    """Checks whether the words are anagrams.

    word1: string
    word2: string

    returns: boolean
    """
    return Counter(word1) == Counter(word2)
```


```python
is_anagram('tachymetric', 'mccarthyite')
```


```python
is_anagram('banana', 'peach')
```

**Exercise:** The `Counter` class inherits from `dict` so all methods and functions that work with a dictionary will also work with a `Counter`.

Read [the documentation of Counter](https://docs.python.org/3/library/collections.html#collections.Counter), then use a `Counter` to find the three most common letters in the word "pneumonoultramicroscopicsilicovolcanoconiosis".


```python
# Solution goes here
```

### Multisets

A `Counter` is a natural representation of a multiset, which is a set where the elements can appear more than once.
You could use multisets for a game like Scrabble to see if a given set of tiles can be used to spell a given word.

**Exercise:** Write a definition for a class called `Multiset` that inherits from `Counter` and defines an additional method called `is_subset`, which should take `self` and `other` as parameters, where `other` is another `Multiset`.

It should check whether `self` is a subset of `other`; for multisets, that means that every element of `self` appears in `other` with at least the same frequency.  For example, `aa` is a subset of `aaab`, but `aabb` is not.


```python
# Solution goes here
```

The following function uses `Multiset.is_subset` to check whether a particular word can be spelled using a particular set of tiles.


```python
def can_spell(word, tiles):
    """Checks whether a set of tiles can spell a word.

    word: string
    tiles: string

    returns: boolean
    """
    return Multiset(word).is_subset(Multiset(tiles))
```


```python
can_spell('SYZYGY', 'AGSYYYZ')
```


```python
can_spell('omelette', 'breaking a few eggs')
```

**Optional Exercise:**  If you change the name of `is_subset` to `__le__`, you can use the `<=` operator to test whether one `Multiset` is a subset of another.

### Probability Mass Functions

You can also extend `Counter` to represent a probability mass function (PMF).  A PMF is a map from possible outcomes to their probabilities.  The probabilities in a PMF are "normalized" if they add up to 1 (and they are all non-negative).

The following `PMF` class inherits from `Counter` and adds the following methods:

* `normalize` computes the total of the frequencies and divides through, yielding probabilities that add to 1.

* `__add__` enumerates all pairs of outcomes and returns a new Pmf that represents the distribution of the sum.

* `render` returns the outcomes and probabilities in a form ready for plotting.


```python
class Pmf(Counter):
    """A Counter with probabilities."""

    def normalize(self):
        """Normalizes the PMF so the probabilities add to 1."""
        total = sum(self.values())
        for key in self:
            self[key] /= total

    def __add__(self, other):
        """Adds two distributions.

        The result is the distribution of sums of outcomes from the
        two distributions.
        
        Note that this method is only correct if the selections from
        the two distributions are independent; that is, if the outcome
        of the first selection does not affect the probabilities of
        the outcomes for the second selection.

        other: Pmf

        returns: new Pmf
        """
        pmf = Pmf()
        for key1, prob1 in self.items():
            for key2, prob2 in other.items():
                pmf[key1 + key2] += prob1 * prob2
        return pmf

    def render(self):
        """Returns outcomes and their probabilities, suitable for plotting."""
        return zip(*sorted(self.items()))
```

As an example, we can make a Pmf object that represents a 6-sided die.


```python
d6 = Pmf([1,2,3,4,5,6])
d6.normalize()
d6.name = 'one die'
print(d6)
```

Using the add operator, we can compute the distribution for the sum of two dice.


```python
d6_twice = d6 + d6
d6_twice.name = 'two dice'

for key, prob in d6_twice.items():
    print(key, prob)
```

Using `sum` or `np.sum`, we can compute the distribution for the sum of three dice.


```python
# if we use the built-in sum we have to provide a Pmf additive identity
pmf_ident = Pmf([0])
d6_thrice = sum([d6]*3, pmf_ident)
```


```python
# with np.sum, we don't need an identity
d6_thrice = np.sum([d6]*3)
d6_thrice.name = 'three dice'
```

And then plot the results (using Pmf.render)


```python
import matplotlib.pyplot as plt
%matplotlib inline
```


```python
for die in [d6, d6_twice, d6_thrice]:
    xs, ys = die.render()
    plt.plot(xs, ys, label=die.name, linewidth=3, alpha=0.5)
    
plt.xlabel('Total')
plt.ylabel('Probability')
plt.legend()
plt.show()
```

**Exercise:** Suppose you are fighting an orc who will die if he suffers 9 or more hit points of damage.  You attack successfully with [short sword](https://roll20.net/compendium/dnd5e/Shortsword#content) and [dagger](https://roll20.net/compendium/dnd5e/Dagger#content), so you can roll a d6 and a d4 for total damage.  What is the probability that you kill the orc?


```python
# Solution goes here
```


```python
# Solution goes here
```

### Bayesian statistics

A `Suite` is a `Pmf` that represents a set of hypotheses and their probabilities; it provides `bayesian_update`, which updates the probability of the hypotheses based on new data.

`Suite` is an abstract parent class; child classes should provide a `likelihood` method that evaluates the likelihood of the data under a given hypothesis.  `update_bayesian` loops through the hypotheses, evaluates the likelihood of the data under each hypothesis, and updates the probabilities accordingly.  Then it re-normalizes the PMF.


```python
class Suite(Pmf):
    """Map from hypothesis to probability."""

    def bayesian_update(self, data):
        """Performs a Bayesian update.
        
        Note: called bayesian_update to avoid overriding dict.update

        data: result of a die roll
        """
        for hypo in self:
            like = self.likelihood(data, hypo)
            self[hypo] *= like

        self.normalize()
        
    def print_probs(self):
        for hypo in sorted(self):
            print(hypo, self[hypo])
```

As an example, I'll use `Suite` to solve the "Dice Problem," from Chapter 3 of <i>Think Bayes</i>.

"Suppose I have a box of dice that contains a 4-sided die, a 6-sided die, an 8-sided die, a 12-sided die, and a 20-sided die. If you have ever played Dungeons & Dragons, you know what I am talking about.  Suppose I select a die from the box at random, roll it, and get a 6. What is the probability that I rolled each die?"


I'll start by defining `DiceSuite`, which inherits `bayesian_update` from Suite and provides `likelihood`.

`data` is the observed die roll, 6 in the example.

`hypo` is the hypothetical number of sides on the die.

If `data > hypo`, that means the outcome exceeds the number of sides on the die; that's impossible, so it has probability 0.

Otherwise, the probability of any outcome is `1/hypo`, where `hypo` is the number of sides on the die.


```python
class DiceSuite(Suite):
    
    def likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.

        data: result of a die roll
        hypo: integer number of sides on the die
        """
        if data > hypo:
            return 0
        else:
            return 1/hypo
```

Now we can make a `DiceSuite` object that represents the possible number of sides on the die. By default, all dice have the same prior probability.

Then I update the distribution with the given outcome and print the results:


```python
dice_suite = DiceSuite([4, 6, 8, 12, 20])
dice_suite.normalize()

dice_suite.print_probs()
```


```python
dice_suite.bayesian_update(6)

dice_suite.print_probs()
```

As expected, the 4-sided die has been eliminated; it now has 0 probability.  The 6-sided die is the most likely, but the 8-sided die is still quite possible.

Now suppose I roll the die again and get an 8.  We can update the Suite again with the new data.


```python
dice_suite.bayesian_update(8)

dice_suite.print_probs()
```

Now the 6-sided die has been eliminated, the 8-sided die is most likely, and there is less than a 10% chance that I am rolling a 20-sided die.


**Exercise:** Draw a UML class diagram that shows the relationships among all classes in this notebook, plus `Counter` and `dict`.

**Exercise:** Suppose you know that up to 100 sequentially-numbered raffle tickets have been sold, and you think it is equally likely that the number sold is anywhere from 1 to 100.  You find a randomly discarded ticket that is number 37.  What is the probability that it is the winning ticket?

Hint: Define a class named `TicketSuite` that inherits from `Suite` and provides an appropriate `likelihood` function.  It should also define a method that computes the average probability of winning, weighted by the probability of each outcome.

Note: This exercise is pretty challenging if you are not familiar with Bayesian statistics.  But if it intrigues you, consider taking Computational Bayesian Statistics.


```python
# Solution goes here
```


```python
# Solution goes here
```


```python
# Solution goes here
```
