"""Import a shapes module from a directory based on the command line argument, and save it as an image.

Usage: python screenshot.py username

This runs and screenshots ReadingJournal-{username}/shapes.py, and screenshots
the resulting turtle window to images/{username}.ps.

Caveats:
* It relies on `import` to run the file, so it won't work if it uses the
  `if __name__ == '__main__'` idiom.
* It depends on the file ending with a call to `turtle.mainloop`, which it
  patches to call the screenshot instead of looping until the user closes the
  window.
"""
import sys
import os.path
import turtle

if len(sys.argv) != 3:
    print("usage: {} PATH USERNAME".format(sys.argv[0]))
    sys.exit(1)

fname = sys.argv[1]
login = sys.argv[2]
dirname = os.path.dirname(fname)


def save_screen_to_file():
    """Save the current turtle window ("screen") to a file.

l   The file name is based on the `login` global variable.
    """
    window = turtle.Screen()
    canvas = window.getcanvas()
    filename = os.path.join("images", login + '.ps')
    canvas.postscript(file=filename)
    print("saved", filename)


# Modify the turtle module so that calling mainlooop instead saves the
# screen to a file
turtle.mainloop = save_screen_to_file

sys.path.append(dirname)
try:
    import shapes
except ImportError:
    fname = os.path.join(dirname, 'shapes.py')
    if not os.path.exists(dirname):
        print("Missing directory:", dirname)
    elif not os.path.exists(fname):
        print('Missing file:', fname)
    else:
        print("Couldn't import", fname)
