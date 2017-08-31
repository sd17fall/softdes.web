# Activity 1.2 – Jupyter

## 1. Create a new directory

In a terminal window, create a new directory: `mkdir notebooks`.

Set the **terminal session** to use that directory: `cd notebooks`.

Now this terminal session is “in” the `notebooks` directory.

* Enter `pwd` (Linux, macOS) or `cd` (Windows) into a shell to find out the current directory for that terminal session. Try this now.
* Enter `ls` (Linux, macOS) or `dir` (Windows) to see a list of files in the current directory. Try this now – there should be no files, because you are in a newly-created, empty, directory.

## 2. Launch Jupyter

In the same terminal window, enter `jupyter notebook`. This should open a new window or tab in your web browser. The page in this window or tab will show a list of files in the directory. Since the `notebooks` directory is empty, it should show an empty list.

## 3. Create a Notebook

In the New menu, select `Python 3`. (Your Python may have a slightly different name, such as `Python [default]` or `Python [conda root]`.)

Type `40 + 2` into the cell.

Using the icons and the “cell type” popup menu (`Code`, to the right of the icons) at the top of the page to do the following:

* Run the Python code (the “Play”, or right triangle, icon). You should see a line `Out[1]: 42`.
* Modify the text to read `40 * 2`, and run it again.
* Create a new cell. Enter `40 - 2` into this cell, and run it.
* Create a new cell. Use the cell type menu to change its type to “Markdown”. Enter the text `Some *italic* and **bold**`. What does running this cell do?
* Create a new cell. *Leave it as a “Code” cell.* Enter the text `Some *italic* and **bold**` into this cell too. What does running this cell do?

## 4. Quit Jupyter

Press the Save icon (the leftmost icon, that looks like a floppy disk from the 90's) to save your Jupyter notebook. Close the tab or window.

Find the terminal session that is running `jupyter notebook`. Press control-c. (Hold the control key down, and while it is down press `c`. Then release them in either order.)

You will see some messages, including `Shutdown this notebook server (y/[n])?`. This is another *prompt*. Answer it by typing `y`, and then return.

(Control-c requests that a program that you have started from the terminal, stop. It works on more programs than just `jupyter`.)

In the terminal, enter `ls` (Linux or macOS) or `dir` (Windows). You now see a file named `Untitled.ipynb`. The file suffix `.ipynb` standards for "iPython Notebook" (“iPython” was the original name for “Jupyter”). It means that the file is a Jupyter notebook.

## Going Beyond

* Take the Jupyter tour. Select “User Interface Tour” from the Jupyter “Help” menu.
* Rename your notebook. Verify that the file name changed.
* Select “Keyboard Shortcuts” from the Jupyter “Help” menu. These are alternatives to using the icons and popup menu. Repeat the steps in “Make a notebook” using the keyboard instead of the icons and the cell type menu.
* Read the Markdown cheatsheet (linked to from the course site). Try out different Markdown features.
* Create a new Markdown cell. Try entering `$a^2$`,`$$a^2$$`, and `$a^2+b^2=c^2$`. What happens if you include these in a paragraph of text?