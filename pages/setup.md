---
title: Set Up Your Development Environment
permalink: activities/setup/
---

{% include toc %}

## Keep Calm and SoftDes On

Before we can get down to the business, we need to make sure we have the right tools for the job. If you follow these instructions (with help from our amazing NINJA team), your computer will be primed and ready to do some serious computational work.

Initially, the amount of new stuff here may seem intimidating. Please do not let this discourage you! We (NINJAs and faculty) will provide lots of help and guidance along the way to help you setup, and then gain comfort with your new toolset. The process will start at the end of the first class, and will continue with additional NINJA / faculty office hours to help you complete the process successfully. Additionally, you will gain familiarity and comfort with this toolset as the semester progresses. In other words, you should think of learning the toolset as a process and not something that you need to do all at once.

### A note about variations on the instructions

The instructions below will allow you to setup the “officially supported” environment for SoftDes. Some deviations from the setup below are okay while others are not (when in doubt please ask). That being said, it will likely be more difficult for us to help you debug problems with your setup if you have a nonstandard environment.

## Step 1: Install Python

[Adapted from _Modeling and Simulation in Python_, by Allen Downey.]

You might already have Python installed on your computer, but you might not have the latest version. To use the materials in this course, you need Python 3.6, or later. Even if you have the latest version, you probably don’t have all of the libraries we need.

You could update Python and install these libraries, but I strongly recommend that you don’t go down that road. I think you will find it easier to use **Anaconda**, which is a free Python distribution that includes many of the libraries you need in this course (and lots more).

Anaconda is available for Linux, macOS, and Windows. By default, it puts all files in your home directory, so you don’t need administrator (root) permission to install it, and if you have a version of Python already, Anaconda will not remove or modify it.

To install Anaconda, visit the [Anaconda install page](http://docs.continuum.io/anaconda/install.html).

## Step 2: Verify Jupyter

Run `jupyter -h` verify that Jupyter is installed.

When you install Anaconda, you should get Jupyter by default, but if not, run

    conda install jupyter

## Step 3: Get Started with Git

We will make heavy use of Git (and GitHub in this class). Haven’t heard of Git? That’s totally fine (and totally expected)! Before we do some course specific Git stuff, take some time to read [Chapter 1](https://github.com/AllenDowney/amgit/blob/master/en/01-introduction/01-chapter1.markdown) of Allen’s excellent online book called AmGit.

### Install Git

Git may already be installed on your system. Enter `git --version` into a terminal window to test. If this prints something like `git version 2.14.1`, you are good to go. (The exact number doesn't matter, so long as it's 2.something.)

Otherwise, download and install git from the [git download page](https://git-scm.com/download/).

If you are a macOS user and you are using [homebrew](https://brew.sh), you can run `brew install git` instead of download  git from the download page. If you don't know what this means, use the download page.

### Create a GitHub Account

Now that you have the basic idea of what version control is and what it is good for, you are going to take the next step and sign up for an account on a website called [GitHub](https://github.com/). The second chapter of Allen’s book has a nice description of GitHub, and how to make an account.

> GitHub is a web-based hosting service for Git users. In general a hosting service provides storage space on remote servers, network access, and tools and applications for interacting with stored data. GitHub provides storage for Git repositories and tools for interacting with them.
>
> There are other hosting services for Git, but GitHub is one of the most popular. It is so popular that people sometimes say “GitHub” when they mean “Git”, so just to be clear:
>
> * Git is an application that runs on your computer and helps you manage repositories.
> * You can use Git to manage repos stored on your own computer or on any computer configured as a Git server.
> * Anybody can set up and run a Git server. A company that runs Git servers professionally is a Git hosting service.
> * GitHub is one of many Git hosting services.
>
> Ok, go to [https://github.com](https://github.com/). If you already have an account, log in. Otherwise, you will have to create one.
>
> You can choose any available username you like, but there are a few things you might want to think about:
>
> 1. Working on GitHub involves interacting with other people. They will see your username, so choose wisely.
> 2. Some people, like `AllenDowney`, use their full names, but the most common schema seems to be one-word lower-case usernames. For example, Scott Chacon is `schacon`.
> 3. If you want to be anonymous, you can choose a username unrelated to your real name; however,
> 4. Many software engineers use GitHub as part of their professional portfolio. If a potential employer wants to check out your skills, they might look at your GitHub repositories.
>
> It is probably a good idea to think of everything you do on GitHub as part of your public professional reputation.

### Step 4. Get the Reading Journal

We will be using GitHub for a number of use cases in the class.

* Turning in pre-class reading exercises
* Turning in mini-projects
* Distributing materials for in-class exercises

Since there’s reading due next class, you will need to perform the steps below to setup your personal `ReadingJournal` repository.

1. Click on the invitation link <https://classroom.github.com/a/XrWDBCx2>
2. Click the green button “Accept this assignment”.
3. Follow the remaining instructions until you get to your repository page. It will looks something like this <https://github.com/sd17fall/ReadingJournal-myname>, except with your GitHub user id instead of `myname`.
4. ***Clone the repository*** by typing the following into your terminal program. Replace `myname` with your GitHub user id.

```bash
$ git clone git@github.com:sd17fall/ReadingJournal-myname.git ReadingJournal
```

Now you have a copy of the ReadingJournal folder (directory) on your drive. Use the terminal, macOS Finder, Windows Explorer, or Ubuntu File Manager to verify that it is present.

Next, you can fire up Jupyter notebook and load the reading journal for day X.

```bash
$ cd ReadingJournal
$ jupyter notebook reading-journal-1.ipynb
```

If all goes well, this should bring up a web-browser with the reading questions.

## Step 5. Install Atom

1. [Download and install](http://flight-manual.atom.io/getting-started/sections/installing-atom/) the [Atom text editor](https://atom.io) onto your computer.
2. Follow the [Atom Basics](http://flight-manual.atom.io/getting-started/sections/atom-basics/) instructions to create a text file and save it.
3. Follow the [Atom Packages](http://flight-manual.atom.io/using-atom/sections/atom-packages/) instructions to find and install the following packages: `python-tools`, `trailing-spaces`, `Hydrogen`.

On Windows, if you see an error like this:

![](/images/setup/error_python-tools_480.jpg)

Then do the following:

1. In a terminal, enter `where atom`. This should report a *path* such as  `C:\Users\MYNAME\AppData\Local\Continuum\Anaconda3\python.exe`, where MYNAME is your Windows login.
2. In Atom:
  * Use <kbd>Cmd+,</kbd> to open the Settings
  * Click on Packages in the sidebar
  * Find the "python-tools" package
  * Click Settings.
  * In the “Path to python directory” setting, paste the path from 1., *without* the final `python.exe`: for example, `C:\Users\MYNAME\AppData\Local\Continuum\Anaconda3\python.exe`
