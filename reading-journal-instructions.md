---
permalink: reading-journal/
---

# Reading Journals

## Submitting Completed Readings

Once you have completed your reading journal (not just the reading exercises, but also your notes as well as any comments you want to give to us), you can turn in your work by running the following commands. First, make sure you have saved the notebook by clicking "Save and checkpoint" in the browser window. Then, run the following. (Change “reading journal 1” to the day that you have completed.)

```
$ cd ReadingJournal
$ git add reading-journal-*.ipynb
$ git commit -m "Completed reading journal 1"
$ git push origin master
```

You will then be prompted to enter your GitHub username and password.  Assuming you followed all of the instructions outlined above, that's it!

## Downloading Future Notebooks

We will continue adding reading notebooks to the original upstream class repository. These will not show up in your forked copy unless you explicitly pull them in.

### One Time Setup: Add Upstream Remote

On your laptop, you should have a cloned copy of the ReadingJournal repository from your GitHub account. You can verify this by checking its remote repositories:

```
$ cd ReadingJournal
$ git remote -v

origin	git@github.com:focs17fall/ReadingJournal-myname.git (fetch)
origin	git@github.com:focs17fall/ReadingJournal-myname.git (push)
```

We want to keep `origin` (the cloned copy in your GitHub account) for you to push completed work to, but we also want to add the original upstream class master repository for you to pull new assignments from. We can add this additional remote by running:

```
$ git remote add upstream	https://github.com/sd17spring/ReadingJournal.git
```

If you run `git remote -v` now, you should see both `origin` and `upstream` listed.

### Pull New Notebooks from Upstream

Each time you want to grab the latest assignments, you should first first make sure all your recent work is committed. This is just to form good habits - each new reading journal assignment will be its own `.ipynb` file, so there should not be any conflicts. Next, run:

```
$ git pull upstream master
```

This should pull in the latest assignment notebook, which you can then complete and push to your `origin` repository by following the usual submission instructions above.