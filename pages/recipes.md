---
title: Recipes
permalink: resources/recipes/
redirect_from: resources/git/
---

{% include toc %}

This page is a companion to the [Resources]({% link pages/resources.md %}) page.

## Python Recipes

### Install PyGame

Linux:

```bash
$ apt-get build-dep python-pygame
$ apt-get install mercurial python-dev python-numpy ffmpeg libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev
$ pip install pygame
```

macOS:

Install [Home Brew](https://brew.sh). Then:

```bash
$ brew install sdl sdl_image sdl_mixer sdl_ttf portmidi
$ pip install pygame
```

Windows:

First, try this:

```bash
$ pip install pygame
```
The above worked on one test machine.
If it doesn't work on your laptop, tell us on Slack and try the following:

```bash
$ conda install -c cogsci pygame
```

### Fix "NameError: name 'math' is not defined"

Fix "NameError: name 'math' is not defined" (or another module):

```python
import math
```

### [macOS] Pygame doesn't receive keyboard events

Problem: The Pygame window doesn't get focus.
Keyboard events go to the last previously focussed windows (e.g. editor window or terminal)
instead of Pygame.

Once:

    $ source deactivate
    $ brew install python3
    $ pip3 install pygame
    $ python3 [yourscript.py]

Each time you create a terminal window:

    $ source deactivate
    $ python3 [yourscript.py]

If this doesn't work, repeat these instructions with `/usr/local/bin/python3` for `python3`.

### Fix "RecursionError: maximum recursion depth exceeded"

Your recursive function is either missing a base case, or is somehow not executing it (for example, it is calling itself with the same arguments that it was called with – TBD illustrated in the Recursion notes).

### Using doctest

Run all the doctests in a module (file, script): `doctest.testmod()`

Run the doctests with verbose output: `doctest.testmod(verbose=True)`

Test a single function: `doctest.run_docstring_examples(get_complement, globals())`

Test a single function with verbose output: `doctest.run_docstring_examples(get_complement, globals(), verbose=True)`

### Working with Turtles

```python
import turtle

t = turtle.Turtle()
# …
turtle.mainloop()
```

## Atom Recipes

### Enable autosave

Enable autosave, to avoid ever seeing the workflow bug that the code you're running or committing doesn't include your latest change(s):

1. Select Atom Preferences (<kbd>cmd+,</kbd>)
2. Click "Packages"
3. Find the "autosave" package
4. Click "Settings"
5. Enable "Enabled"

### Use multiple cursors

Use [multiple cursors and selections](http://flight-manual.atom.io/using-atom/sections/editing-and-deleting-text/#multiple-cursors-and-selections) to edit several places at once.

### Make Hydrogen work with Anaconda
Make the Hydrogen plugin work with Anaconda Python:

* The easy way: always launch atom by running `atom` in the Anaconda Command Prompt.
* The harder way (Windows): run `where python` in the Anaconda Command Prompt to find the path to your Python.
Follow [these instructions](https://stackoverflow.com/questions/17872234/how-to-add-python-to-windows-registry)
to add this path to your Windows registry. **Warning**: Neither the NINJAs nor IT will necessarily be able to
restore your machine if editing the registry goes awry.
* The hardest way: Edit the Hydrogen “Kernel Specs” setting to specify the path to something like this: `{"kernelspecs":{"python3":{"resource_dir":"/Users/osteele/anaconda3/lib/python3.5/site-packages/ipykernel/resources","spec":{"env":{},"argv":["/Users/osteele/anaconda3/lib/python3.5","-m","ipykernel","-f","{connection_file}"],"display_name":"Python 3","language":"python"}}}}`, and restart Atom.
**Warning**: I wasn't able to get this to work. It's easy to clear this setting and restart Atom to fix it again, though.

## Git Recipes

### Working with Reading Journals

This material is now on the [Reading Journal]({% link pages/reading-journal.md %}) page.

### `.gitignore`: Ignoring Files

* [GitHub documentation](https://help.github.com/articles/ignoring-files/)
* [Tutorial from Atlassian](https://www.atlassian.com/git/tutorials/gitignore)
* [`.gitignore` templates](https://www.gitignore.io)

### Get stuff from my computer to GitHub

```bash
$ git add <filename>
$ git commit -m "<commit-message>"
$ git push
```

You can alternatively use `git commit -am '<commit-message>'` to both add all
of the files in your folder and put a message on them, all in one command!

If you forget to include `-m` in your commit, git will open a text-editor called
vim so that you can enter a commit message there. To write your commit message
in vim, first press “i”, then write your message, then type <kbd>:wq</kbd> for write-
quit. Alternatively, if you just want to escape from vim's interface without
saving a message, just enter “:q” for quit.

### Pull changes from GitHub

`$ git pull`

-or-

`$ git pull origin master`

If you get merging errors telling you that you need to merge or 'stash' before
you can pull, see the 'stashing' section below. Also, a quick note on pulling,
what pulling means is that you're taking the code that others have pushed to
your repository and matching what you have on your computer with that, so it
incorporates their changes.

### How to stash (and what is stashing?)

`$ git stash`

Stashing stores the copy of your current version of the repository on your
computer, so you can keep that copy there before you pull changes that others
have made. Often, you'll be prompted to stash before pulling or merging with
others. Now that you've stashed, how do you get your stuff back? You'll
probably do the following:

```bash
$ git stash
$ git pull
$ git stash pop
```

Git stash will store your changes locally, git pull will download the changes
other have made to the repository, and git stash pop puts the changes that you
made locally that conflict directly in the code. If there's anything to merge,
do it in the file and then commit and push your changes.

### Fix a Git detached head

`$ git checkout master`

If this doesn't work, try:

`$ git checkout origin/master`

### What is branching on Git?

Branches on Git are very similar to branches on trees. The tree trunk is
represented as the `master` branch and the branches that come off of the
master branch you can name whatever you want. These branches will start at
whatever state master was at the time you made the branch. The master branch
can continue changing independently of the branch that you created. You can
combine the changes that you make in separate branches by 'merging' them
together. For more on merging, look at the sections that will follow. Also,
you can view all of the branches in your repository by doing:

`$ git branch -a`

And you can tell what branch you're on by doing the command:

`$ git branch`

### Make a new branch

`$ git fetch origin`

`$ git checkout -b <your-branch-name> origin/master`

This branch will exist on your computer, in order to push it to git and have
it be visible by others, you'll have to push your local branch to be a remote
branch (see below)

### Push your local branch to be a remote branch

`$ git push -u origin <your-branch-name>`

### Checkout a branch

'Checking out' a branch is when you pull another person's branch (or teleport
to another branch), you do it by doing:

```bash
$ git fetch origin
$ git checkout <branch-name>
```

### Merge changes

If you get to a point where you are merging changes, you'll see something in
your code like the following:

    <<<<<<<HEAD
    sarah_strohkorb = pick_the_coolest_ninja(input_1, input_2)
    =======
    sarah_strohkorb = pick_the_coolest_ninja()
    >>>>>>><my-branch-name>

The `sarah_strohkorb = pick_the_coolest_ninja(input_1, input_2)` line is what
is represented on the `master` branch and `sarah_strohkorb = pick_the_coolest_ninja()` line is what is represented on the '&lt;my-branch-name&gt;' branch. You'll have to pick one of them and then delete the rest of
the information. So if I want `sarah_strohkorb = pick_the_coolest_ninja()`,
I'll rearrange the code to get the following:

    sarah_strohkorb = pick_the_coolest_ninja()

### Merge one branch into another

Let's say that you've been working on a branch called `dev` and you have also
been modifying the `master` branch. You want to merge your changes in the
`master` branch into the `dev` branch, so that your `dev` branch is up to
date. What you want to do is first get into the `dev` branch, then:

```bash
$ git fetch origin
$ git merge origin/master
```

If you have any conflicts, deal with them, commit and push your changes, and
you're good to go!
