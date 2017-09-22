---
permalink: resources/
title: Resources
---

{% include toc %}

This page lists web sites, PDF documents, Jupyter notebooks, and
Python packages that have been mentioned during the course.

It's not an attempt to list everything related to each of those topics; just
to collect those resources that have already been mentioned into one place.

## General

[Stack Overflow](http://stackoverflow.com) is a community of programmers, and a knowledge base of programming questions and answers. You can search it directly from its site; it also shows up in Google search.

## Python

### Reference

* [Think Python, by Allen Downey](http://greenteapress.com/wp/think-python-2e/) – the class text
* [Python 3.5 Documentation](https://docs.python.org/3.5/)
* [Python 3.5 Standard Library](https://docs.python.org/3.5/library/index.html)
* [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/), especially [Writing Great Python Code](http://docs.python-guide.org/en/latest/#writing-great-python-code)
* [Python Tutor](http://www.pythontutor.com) interactive visualization

### Learn

* [HackerRank Python Introduction](https://www.hackerrank.com/domains/python/py-introduction)
* [How to Think Like a Computer Scientist](https://runestone.academy/runestone/static/thinkcspy/index.html) interactive course. Register [here](https://runestone.academy/runestone/default/user/register#) and enter "thinkcspy" as the course name.
* [Google's Python Class](https://developers.google.com/edu/python/)
* [Automate the Boring Stuff with Python](http://automatetheboringstuff.com) (includes video tutorials)
* [Practice Python](http://www.practicepython.org) exercises
* [Official Python Tutorial](https://docs.python.org/3/tutorial/index.html)
* [Spring 2014 NINJA tutorial: Python exercises](https://docs.google.com/document/d/1k-JU9cPokJ58ur4ubpbhLAxC26aAx9bCUcianobBLFE/edit)

### Style

* [PEP 8 – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* [PEP 257 – Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
* [Google Style Guide](https://google.github.io/styleguide/pyguide.html)
* [GeneFinder in Google Style](https://github.com/sd17fall/GeneFinder/blob/formatted/gene_finder.py) (see how it compares to master [here](https://github.com/sd17fall/GeneFinder/pull/2/files#diff-3941f5c15920a6b919f1db7864a6d2c7))

## Atom

* [Atom Flight Manual](http://flight-manual.atom.io)
* [Atom Keyboard Shortcuts](https://github.com/nwinkler/atom-keyboard-shortcuts)

### Tips

* **Enable autosave**, to avoid ever seeing the workflow bug that the code you're running or committing doesn't include your latest change(s):
  1. Select Atom Preferences (<kbd>cmd+,</kbd>)
  2. Click "Packages"
  3. Find the "autosave" package
  4. Click "Settings"
  5. Enable "Enabled"
* **Edit several places at once** using [multiple cursors and selections](http://flight-manual.atom.io/using-atom/sections/editing-and-deleting-text/#multiple-cursors-and-selections)
* **Make the Hydrogen plugin work with Anaconda Python**:
  * The easy way: always launch atom by running `atom` in the Anaconda Command Prompt.
  * The harder way (Windows): run `where python` in the Anaconda Command Prompt to find the path to your Python.
    Follow [these instructions](https://stackoverflow.com/questions/17872234/how-to-add-python-to-windows-registry)
    to add this path to your Windows registry. **Warning**: Neither the NINJAs nor IT will necessarily be able to
    restore your machine if editing the registry goes awry.
  * The hardest way: Edit the Hydrogen “Kernel Specs” setting to specify the path to something like this: `{"kernelspecs":{"python3":{"resource_dir":"/Users/osteele/anaconda3/lib/python3.5/site-packages/ipykernel/resources","spec":{"env":{},"argv":["/Users/osteele/anaconda3/lib/python3.5","-m","ipykernel","-f","{connection_file}"],"display_name":"Python 3","language":"python"}}}}`, and restart Atom.
    **Warning**: I wasn't able to get this to work. It's easy to clear this setting and restart Atom to fix it again, though.

## Command Line

### Bash (Linux / macOS)

* [Linux at Olin](https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxzZDE1c3ByaW5nfGd4OmMyNzcyOTBjYThlMTM1Mg)

### Windows Command Prompt

* [Introduction to the Windows Command Prompt](https://www.bleepingcomputer.com/tutorials/windows-command-prompt-introduction/)
* [Windows Command Prompt in 15 Minutes](http://www.cs.princeton.edu/courses/archive/spr05/cos126/cmd-prompt.html). (Where it says `java`, think `python` :smile:.)
* [How to use the Windows command line](https://www.computerhope.com/issues/chusedos.htm)
* [DOS (Windows command prompt) / Linux equivalents](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/4/html/Step_by_Step_Guide/ap-doslinux.html)

## Git

* [Git Help]({% link pages/git-help.md %}) on this site contains links and information.

## Markdown

* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Jupyter

* [How to use Jupyter Notebooks](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook##UseJupyter)
* [Jupyter Keyboard Shortcuts](https://www.cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/) (compact)
* [Jupyter Keyboard Shortcuts](https://gist.github.com/kidpixo/f4318f8c8143adee5b40) (longer)
* [28 Jupyter Notebook tips, tricks and shortcuts](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)
