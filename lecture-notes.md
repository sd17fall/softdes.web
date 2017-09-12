---
permalink: /notes
title: Lecture Notes
---

{% include toc %}

## Day 3

### Specification and implementation

* The specification is what it does.
* The implementation is how it does it; in software, this is realized as code.
* Sometimes the specification is in your head.
* It can be useful to draw out the specification in order to check the implementation against it, without holding as much in your head.
* It can also be easier to compare the specification to the requirements, and then the implementation to the specification, than to compare the implementation directly against the requirements.
* A formal development methodology might include analysis -> requirements -> specification -> implementation. This is a modified [waterfall model](https://en.wikipedia.org/wiki/Waterfall_model), which is in turn a kind of “Big Design Up Front” (BDUF).
* Alternatives to BDUF include [exploratory programming](https://en.wikipedia.org/wiki/Exploratory_programming), [Iterative design](https://en.wikipedia.org/wiki/Iterative_design), and [incremental build](https://en.wikipedia.org/wiki/Incremental_build_model) In all of these the process of building or using an incomplete implementation leads to new ideas about how to refine it. This ties into the “start small” bullet point from “Holding a Program in One's Head”.

### Who's reading your code?

* The computer (via the Python interpreter) reads your code in order to run or “execute”, or “evaluate” it), in order to produce behavior.
* Humans read your code in order to debug or extend it.
* One feedback loop is: coder -> code -> computer -> behavior -> coder (who compares the behavior to specification)
* Variable names, doc strings, comments are for humans.
* For a run-once program, writing for humans isn't important.
* For a long-lived source base, or one with several collaborators, a readable (by humans) code with some bugs can be more useful than an functionally correct but obfuscated program.
* Naming variables and functions:
  - Prefer longer names, the longer the distance between where a thing is defined and where it's used.
  - Where the code translates a domain such as math or physics, and the people working on the code understand this domain, it's common practice to use names from the domain, even if they're short.
  - Where the code implements a formula or algorithm, it's common practice to comment the source of the formula, and use the same names. In this case the formula is the specification, and using the same names makes it easier to see whether the implementation matches.
* Programming conventions don't make a difference to the computer, but make it easier for the human reader. For example, `import` statements go at the beginning of a file.

### Testing

* Testing is difficult because (among other reasons) you have to switch from “how can I make it work” to “how can I break it”.
* There's a convention for recording test examples into a doc string.
* doctest runs these examples
* `if __name__ == '__main__'` is an idiom (a kind of figure of speech) – you can use the whole without understanding how it's built from the parts. Cf. “Who let the cat out of the bag?”. (This is a better example than the one I used in class.)
* There's more about doctest in the reading journal and on the assignment page.
* The handout suggested creating the test cases without using a computer:
  * Breaking “coding” or “programming” into different activites can give you variety to switch between. (“My desert stomach isn't full.”)
  * Switching activities or media can give you a fresh perspective / allow you to slip into a different persona (writer vs. reader; builder vs. breaker)
* [`hello.py`](https://github.com/sd17fall/softdes.web/blob/master/files/day3/hello.py) is the final version of the code I typed in class

### Recognizing bugs

* Part of becoming proficient involves recognizing symptoms of failure, and associating them with causes.
* Analogy: recognize 56 as the result of 7 x 8. Now we know how to factor 56: we recognize “I've been here before; how did I get here?”
* Example: changed the code but the behavior didn't change -> didn't save the file. (See “autosave”, below.)
* Example: `NameError: name 'doctest' is not defined` -> forgotten `import`

### Atom tricks

* Enable autosave:
  - Use <kbd>Cmd+,</kbd> to open the Settings
  - Click on Packages in the sidebar
  - Find Autosave
  - Click Settings
  - Click Enabled
* [Multiple selection](http://flight-manual.atom.io/using-atom/sections/editing-and-deleting-text/#multiple-cursors-and-selections)

### Genetics

* DNA -> RNA -> nucleotides -> proteins. DNA and RNA are themselves proteins, and the machinery that implements the arrows is made of proteins. This is how DNA can code for organisms that copy themselves and transcribe the DNA.
* People mentioned:
  * Gregor Mendel (not Mendelson) figured out that traits of an organism or inherited in a less linear way than just mixing their quantiites
  * [Rosalind Franklin](https://en.wikipedia.org/wiki/Rosalind_Franklin) lead the work that provided the evidence for the structure of DNA; died too young to collect the Nobel prize.
  * Watson and Crick used this data to discover the structure of DNA.
  * Sydney Brenner figured out that nucleotide triples make codons.
* Genetics is another *domain* – that is built (partly) on strings, instead of numbers.
* Everything else covered in class is on the assignment page or pages it links to.

### Other

* Now we have four ways to run code: Jupyter, `python` prompt, Python Tutor web site, `python` + filename
* concept -> syntax -> action, vs. syntax -> action.

## Day 2

Top answers from reading prompt:

| Already Doing     | Would Like        | Don't Believe In |
| ----------------- | ----------------- | ---------------- |
| Stretches         | Stretches         | Stretches        |
| Avoid distraction | Avoid distraction |                  |
| Work in groups    | Work in groups    |                  |

### Types

- Types are easier understood by example (extension) than definition (intension).
- Some types are integer, float, string, boolean; we haven't covered list, function.
- Some definitions of type are: a set of values; a category of values; how a value is stored; what you can do to a value.

### Coding, math, and domains

Programming isn't math, but it starts out very math-y

- Lots of programming is *about* something (a "domain"). All of you know some math, so we can use that as a domain.
- Lots of other domains include a component that's modeled with math. So learning how to code about math gives you tools for working in those domains.
- Programming was invented as part of math and split off, so lots of its basics are math-y.
- If you continue in *computer science* (FOCS, data structures and algorithms), you'll see more math. If you continue in *software engineering*, you'll see more principles that are more similar to other engineering disciplines.

### Git

- [TODO diagram from class]
- At this point, we're using git to distribute and collect assignments.
- Later, you'll use git to collaborate with each other.
- For where we are in the course, you don't need to understand git; you can type in the commands.
- It's acknowledged that this can be uncomfortable, so we're happy to teach you as much git as you have tolerance for.
- A repo lives on your laptop or in the cloud.
- A repo contains a set of files, and a set of commits. They cross-cut each other. [TODO picture from class]
- The files in a repo on your laptop relate to files that you can see on your disk. You can update one from the other.
- The repo on your notebook can know which other repos it's related to (where to pull changes from, and where to push them to).
- Git is complex.
  - Collaboration, versions, and sychronization are complex
  - The complexity can either go in a complex tool, or a complex workflow that uses a simper tool.

## Day 1

### Course Themes

Some other course themes, some illustrated (advertently or inadvertently) in class:

* Software design includes the study and manipulation (recording, replay, debugging, improvement) of processes.
  Some of the ideas and techniques are therefore applicable outside of software.

* Many things you do in your life are processes.

* Some ways to optimize a process:
  - Do steps at the same time (in parallel)
  - Switch the order of two steps that don't depend on each other

* A workflow is a process. You can debug and optimize this.

* Make for easier debugging by making one change at a time.
  (We made two – working in Windows, and using Anaconda.)

* Ask for help. Don't waste too much of your time on being stuck.

### Programming Languages

Some languages some of us in class know include C, C++, C#, Haskell, MATLAB, Java, and Swift.

Learning a programming language is like learning a (non-native) natural language. The first one is difficult. Each new one is easier, with a speed bump if it's not in the same family as the ones you know. (Going from French to Spanish to Italian is easier than going from French to German to Russian to Japanese.)

### Why Python?

* It's at the intersection of teachable and useful.
* It's useful both within software engineering (popular for tools, system adminstration, web servers, and big data), and as a tool within the sciences.

On the other hand, Python is slower than most of these (although including its libraries makes this comparison harder),
doesn't run on mobile, doesn't run on resource-constrained devices (such as the Arduino), and doesn't run in the browser.

Deciding which language to use is an example of a tradeoff, given a context and constraints.
This is an engineering idea.

### Theory and Practice

This course teaches several levels:

- *Tools* such as `git`, GitHub, the **Atom** text editor, the command line.
- *Concepts* such as variables, functions, recursion, and iteration.
- *Skills* – how to use the tools against a background of concepts to get stuff done.
- *Practices* – approaching mastery

The course frontloads *tools*, continues to a bolus of *concepts*, and settles into learning *skills* and *practices*.

### Materials

* Our web site is on olin.build.
* This is built using the same tools you have access to.
* It will be developed iteratively over the semester, like your projects (after the first one).
* We will use Slack as a communications channel.

### Experiments

* This course changes because the context (coding and Python technology and community) march on.
* Previous changes 
* This semester's changes include allowing Windows; and using Anaconda.
* A good practice (for making code changes, as well as science experiments) is to change one factor at a time. Otherwise it's difficult to attribute symptoms to their causes.
* We're not doing that because one change a semester doesn't keep up with the world.