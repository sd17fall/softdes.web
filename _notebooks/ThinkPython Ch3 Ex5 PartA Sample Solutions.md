---
date: 2018-01-25T16:32:51-05:00
source: notebooks/ThinkPython Ch3 Ex5 PartA Sample Solutions.ipynb
---

{% include toc %}


## Chapter 3

### Exercise 5

This exercise can be done using only the statements and other features we have learned so far.

(a) Write a function that draws a grid like the following:
```
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
```
**Hint:** to print more than one value on a line, you can print a comma-separated sequence:
print '+', '-'
If the sequence ends with a comma, Python leaves the line unfinished, so the value printed next appears on the same line.
print '+', 
print '-'
The output of these statements is '+ -'.
A print statement all by itself ends the current line and goes to the next line.


```python
def grid():
    print('+','-','-','-','-','+','-','-','-','-','+')
    print('|', ' '*7,'|', ' '*7,'|')
    print('|', ' '*7,'|', ' '*7,'|')
    print('|', ' '*7,'|', ' '*7,'|')
    print('|', ' '*7,'|', ' '*7,'|')
    print('+','-','-','-','-','+','-','-','-','-','+')
    print('|', ' '*7,'|', ' '*7,'|')
    print('|', ' '*7,'|', ' '*7,'|')
    print('|', ' '*7,'|', ' '*7,'|')
    print('|', ' '*7,'|', ' '*7,'|')
    print('+','-','-','-','-','+','-','-','-','-','+')
grid()
```

{: class="nb-output"}

    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +




```python
def print_4(a):
    print(a)
    print(a)
    print(a)
    print(a)
def window_grid():
    rail='+'+' -'*4+' + '+'- '*4+'+'
    stile='|'+' '*9+'|'+' '*9+'|'
    print(rail)
    print_4(stile)
    print(rail)
    print_4(stile)
    print(rail)

window_grid()

```

{: class="nb-output"}

    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +




```python
def pIntersec():
    # prints an intersection point
    print('+',end=' ')
    
def pHLine():
    # prints a horizontal line segment
    print('- - - -', end=' ')
    
def newLine():
    print()
    
def pVerLine():
    # prints a vertical line
    print('|', end=' ')
    
def pEmptySpace():
    # creates the inner empty space
    print('       ', end=' ')
    
def gridRow(f,g):
    # prints one row of the grid
    f()
    g()
    f()
    g()
    f()
    newLine()
    
def insideCell():
    gridRow(pVerLine,pEmptySpace)
    gridRow(pVerLine,pEmptySpace)
    gridRow(pVerLine,pEmptySpace)
    gridRow(pVerLine,pEmptySpace)

def printGrid():
    gridRow(pIntersec,pHLine)
    insideCell()
    gridRow(pIntersec,pHLine)
    insideCell()
    gridRow(pIntersec,pHLine)
    
printGrid()
```

{: class="nb-output"}

    + - - - - + - - - - + 
    |         |         | 
    |         |         | 
    |         |         | 
    |         |         | 
    + - - - - + - - - - + 
    |         |         | 
    |         |         | 
    |         |         | 
    |         |         | 
    + - - - - + - - - - + 




```python
def line():
  return '+ '+'- '*4
    
def space():
  return '|'+' '*9

def full_line():
  return line()*2+'+\n'

def full_space():
  return space()*2+'|\n'

def grid():
  print((full_line()+full_space()*4)*2+full_line())

  
grid()
```

{: class="nb-output"}

    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    




```python
def gridtwo():
    print('+ - - - - + - - - - +')
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')
    print('+ - - - - + - - - - +')
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')
    print('+ - - - - + - - - - +')
 
gridtwo() 
```

{: class="nb-output"}

    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +




```python
def print_plus():
    print('+', end=' ')
def print_minus():
    print('-', end=' ')
def print_pipe():
    print('|', end=' ')
def print_space():
    print(' ', end=' ')
    
def print_horz():
    print_plus()
    print_minus()
    print_minus()
    print_minus()
    print_minus()
    print_plus()
    print_minus()
    print_minus()
    print_minus()
    print_minus()
    print_plus()
    print()
    
def print_vert():
    print_pipe()
    print_space()
    print_space()
    print_space()
    print_space()
    print_pipe()
    print_space()
    print_space()
    print_space()
    print_space()
    print_pipe()
    print()

def print_rect():
    print_horz()
    print_vert()
    print_vert()
    print_vert()
    print_vert()
    print_horz()
    print_vert()
    print_vert()
    print_vert()
    print_vert()
    print_horz()
    
print_rect()
```

{: class="nb-output"}

    + - - - - + - - - - + 
    |         |         | 
    |         |         | 
    |         |         | 
    |         |         | 
    + - - - - + - - - - + 
    |         |         | 
    |         |         | 
    |         |         | 
    |         |         | 
    + - - - - + - - - - + 




```python
def drawGrid():
    line1 = '+ ' + '- '*4 + '+ ' + '- '*4 + '+'
    line2 = '|' + ' '*9 + '|'+ ' '*9 + '|'
    print(line1)
    print(line2)
    print(line2)
    print(line2)
    print(line2)
    print(line1)
    print(line2)
    print(line2)
    print(line2)
    print(line2)
    print(line1)
    
drawGrid()
```

{: class="nb-output"}

    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +




```python
single_divider = '+ ' + '- ' * 4
single_body = '| ' + '  ' * 4
print(single_divider * 2 + '+')
print(single_body * 2 + '|')
print(single_body * 2 + '|')
print(single_body * 2 + '|')
print(single_body * 2 + '|')
print(single_divider * 2 + '+')
print(single_body * 2 + '|')
print(single_body * 2 + '|')
print(single_body * 2 + '|')
print(single_body * 2 + '|')
print(single_divider * 2 + '+')
```

{: class="nb-output"}

    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +




```python
def grid():
    print('+','- '*4,'+','- '*4,'+')
    print('|', ' '*8,'|', ' '*8, '|')
    print('|', ' '*8,'|', ' '*8, '|')
    print('|', ' '*8,'|', ' '*8, '|')
    print('|', ' '*8,'|', ' '*8, '|')
    print('+','- '*4,'+','- '*4,'+')
    print('|', ' '*8,'|', ' '*8, '|')
    print('|', ' '*8,'|', ' '*8, '|')
    print('|', ' '*8,'|', ' '*8, '|')
    print('|', ' '*8,'|', ' '*8, '|')
    print('+','- '*4,'+','- '*4,'+')
    
grid()
```

{: class="nb-output"}

    + - - - -  + - - - -  +
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    + - - - -  + - - - -  +
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    + - - - -  + - - - -  +




```python
def drawThisParticularGrid():
    lineType1 = 2*('+' + (4*' -') + ' ') + '+\n'
    lineType2 = 2*('|'+9*' ')+'|\n'
    drawing = 2*(lineType1 + 4*lineType2) + lineType1
    print(drawing)

drawThisParticularGrid()
```

{: class="nb-output"}

    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    




```python
#without loops I guess
def line():
    print('+', ("- " * 4),end=' ')

def space():
    print('|', (" " * 8), end=' ')

def linerow():
    line()
    line()
    print('+')

def spacerow():
    space()
    space()
    print('|')

def printrow():
    linerow()
    spacerow()
    spacerow()
    spacerow()
    spacerow()

def printgrid():
    printrow()
    printrow()
    linerow()



printgrid()

```

{: class="nb-output"}

    + - - - -  + - - - -  +
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    + - - - -  + - - - -  +
    |          |          |
    |          |          |
    |          |          |
    |          |          |
    + - - - -  + - - - -  +




```python
s1 = '+ - - - - + - - - - +'
s2 = '|         |         |'
print(s1)
print(s2)
print(s2)
print(s2)
print(s2)
print(s1)
print(s2)
print(s2)
print(s2)
print(s2)
print(s1)
```

{: class="nb-output"}

    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +




```python
def grid1():
    p = '+' #plus
    m = '-' #minus
    l = '|' #line
    s = ' ' #space
    
    hori = (p+s+m+s+m+s+m+s+m+s)*2 + p
    sp = (l + s*9)*2 +l
    
    print(hori)
    print(sp)
    print(sp)
    print(sp)
    print(sp)
    print(hori)
    print(sp)
    print(sp)
    print(sp)
    print(sp)
    print(hori)
    return
#I'm sure theres a more efficient way to do this. 
#If I have time I'll get back to it.

grid1()
    
```

{: class="nb-output"}

    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +




```python
def printyfunc():
    print('+', end=' ')
    print('-', end=' ')
    print('-', end=' ')
    print('-', end=' ') 
    print('-', end=' ')
    print('+', end=' ')
    print('-', end=' ')
    print('-', end=' ')
    print('-', end=' ')
    print('-', end=' ')
    print('+')
    print('|', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print('|', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print('|')
    print('|', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print('|', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print('|')
    print('|', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print('|', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print('|')
    print('|', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print('|', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print('|')
    print('+', end=' ')
    print('-', end=' ')
    print('-', end=' ')
    print('-', end=' ')
    print('-', end=' ') 
    print('+', end=' ')
    print('-', end=' ')
    print('-', end=' ')
    print('-', end=' ')
    print('-', end=' ')
    print('+')
    print('|', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print('|', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print('|')
    print('|', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print('|', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print('|')
    print('|', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print('|', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print('|')
    print('|', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print('|', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print(' ', end=' ')
    print('|')
    print('+', end=' ')
    print('-', end=' ')
    print('-', end=' ')
    print('-', end=' ') 
    print('-', end=' ')
    print('+', end=' ') 
    print('-', end=' ')
    print('-', end=' ') 
    print('-', end=' ')
    print('-', end=' ')
    print('+') 
printyfunc()
```

{: class="nb-output"}

    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +




```python
def horiz():
    print('+ - - - - + - - - - +')
def vert():
    print('|         |         |')
def box():
    horiz()
    vert()
    vert()
    vert()
    vert()
    horiz()
    vert()
    vert()
    vert()
    vert()
    horiz()
    
box()
```

{: class="nb-output"}

    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +




```python
def grid_function():
   print('+ - - - - + - - - - +')
   print('|'+' '*9+'|'+' '*9+'|')
   print('|'+' '*9+'|'+' '*9+'|')
   print('|'+' '*9+'|'+' '*9+'|')
   print('|'+' '*9+'|'+' '*9+'|')
   print('+ - - - - + - - - - +')
   print('|'+' '*9+'|'+' '*9+'|')
   print('|'+' '*9+'|'+' '*9+'|')
   print('|'+' '*9+'|'+' '*9+'|')
   print('|'+' '*9+'|'+' '*9+'|')
   print('+ - - - - + - - - - +')
grid_function()
```

{: class="nb-output"}

    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +




```python
def draw_window():
    draw_plus();
    draw_lines();
    draw_lines();
    draw_lines();
    draw_lines();
    draw_plus();
    draw_lines();
    draw_lines();
    draw_lines();
    draw_lines();
    draw_plus();
    
def draw_lines():
    print('|' + ' '*9 + '|' + ' '*9 + '|')
    
def draw_plus():
    print('+ ' + '- '*4 + '+ ' + '- '*4 + '+')
    
draw_window();
```

{: class="nb-output"}

    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +


