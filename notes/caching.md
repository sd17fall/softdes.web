

{% include toc %}


# Caching web requests

## HTTP requests (without caching)
First import the [requests package](http://docs.python-requests.org/en/master/).


```python
import requests
```

## A diversion – one for the bugbook

The following typo (`sofdes` for `softdes`, for a domain that doesn't exist) produced some error about address or nodeinfo the first time I ran it, and never terminated (Jupyter labels it with `In [*]`, where the `*` means "curently executing") each subsequent time. I'm adding both of those to my bug dictionary: "if you see this symptom, it might be because you did a `request.get` on a domain name that doesn't exist".


```python
requests.get('https://sofdes.olin.build')
```

## Back to the working request

Fixed the URL (below). I'm only showing the first 500 characters of the response text.


```python
requests.get('https://softdes.olin.build').text[:500]
```

{: class="nb-output"}




    '<!DOCTYPE html>\n<html>\n  <head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n\n    <title>\n      \n         &middot; Software Design | Fall 2017\n      \n    </title>\n\n    <link rel="stylesheet" href="https://unpkg.com/bulmaswatch/litera/bulmaswatch.min.css">\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">\n    <script type="text/x-mathjax-config">\n  MathJax.Hub.Config({\n    TeX: {\n  '




## Create cache and analyze functions

Let's turn that expression into an `analyze_page` function, that takes the URL as a parameter.


```python
def analyze_page(url):
    return requests.get(url).text

analyze_page('https://softdes.olin.build')[:500]
```

{: class="nb-output"}




    '<!DOCTYPE html>\n<html>\n  <head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n\n    <title>\n      \n         &middot; Software Design | Fall 2017\n      \n    </title>\n\n    <link rel="stylesheet" href="https://unpkg.com/bulmaswatch/litera/bulmaswatch.min.css">\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">\n    <script type="text/x-mathjax-config">\n  MathJax.Hub.Config({\n    TeX: {\n  '




…and actually do some analysis. (Here, just compute the length of the text.)


```python
def analyze_page(url):
    return len(requests.get(url).text)

analyze_page('https://softdes.olin.build')
```

{: class="nb-output"}




    8552




Introduce a temporary variable, and use it to factor the `requests.get(url).text` expression out from last line.


```python
def analyze_page(url):
    text = requests.get(url).text
    return len(text)

analyze_page('https://softdes.olin.build')
```

{: class="nb-output"}




    8552




Introduce a new function, and use it to factor the code that talks to the web out from the code that analyzes the responses.

The function is *called* `cached_get` in anticipation of where we're going with it, but it doesn't yet do caching. The following code has the same *functionality* as the preceding code, it's just *organized* in a way that sets us up to to make the next change.


```python
def cached_get(url):
    return requests.get(url).text

def analyze_page(url):
    text = cached_get(url)
    return len(text)

analyze_page('https://softdes.olin.build')
```

{: class="nb-output"}




    8552




## Implement the cache

Now we can get to work on actually adding the cache.

The strategy is: create a dictionary whose keys are the function parameter value, and whose values are the function return values. For example, `cached_get` wraps a call to `requests.get(url).text` – it works with a dictionary whose keys are URLs, and whose values are the text responses to querying those URLs.


```python
def cached_get(url):
    cached_urls = {}
    if url in cached_urls:
        print('cache hit')
        return cached_urls[url]
    else:
        print('cache miss')
        text = requests.get(url).text
        cached_urls[url] = text
        return text

def analyze_page(url):
    text = cached_get(url)
    return len(text)

analyze_page('https://softdes.olin.build')
analyze_page('https://softdes.olin.build')
```

{: class="nb-output"}

    cache miss
    cache miss





    8552




The returned value indicates that `cached_get` returns the correct value. The `print` statements reveal that the caching code didn't work. Each call to `cached_get` results in a cache miss (and therefore a fresh call to `requests.get`).

The issue is that `cached_urls` is local variable to `cached_get`. Each call to `cached_get` creates a new local frame with a new entry `cached_get`, and creates a new, empty dictionary to assign to that variable.

We fix this by making `cached_urls` a global variable:


```python
cached_urls = {}

def cached_get(url):
    if url in cached_urls:
        print('cache hit')
        return cached_urls[url]
    else:
        print('cache miss')
        text = requests.get(url).text
        cached_urls[url] = text
        return text

def analyze_page(url):
    text = cached_get(url)
    return len(text)

analyze_page('https://softdes.olin.build')
analyze_page('https://softdes.olin.build')
```

{: class="nb-output"}

    cache miss
    cache hit





    8552




## A caveat about Jupyter

The above is sufficient for a Python *script*.

In Jupyter, each time I run the cell above, the first call to `analyze_page` is going to result in a cache miss. This is because running the cell assigns `cached_urls` from a new empty dict `{}`.

If I'm iterating with `analyze_page` – modifying the function definition, running the cell again, and repeating – the caching doesn't buy me anything.

Fix this by putting the definition of `cached_urls` in one cell, and the code you're iterating on in another cell that you can run separately. In class, I put `cached_urls` in a cell by itself, the idea being initialize the global variables in their own cell. Below, I've put `cached_urls` and `cached_get` in a cell together (that's separate from `analyze_page`, the idea being to put the caching layer in its own cell that's separate from the code that uses it.


```python
cached_urls = {}

def cached_get(url):
    if url in cached_urls:
        print('cache hit')
        return cached_urls[url]
    else:
        print('cache miss')
        text = requests.get(url).text
        cached_urls[url] = text
        return text
```


```python
def analyze_page(url):
    text = cached_get(url)
    return len(text)

analyze_page('https://softdes.olin.build')
```

{: class="nb-output"}

    cache hit





    8552




## `cached_get` final touches

Here's another implementation of `cached_get`.


```python
cached_urls = {}

def cached_get(url):
    if url not in cached_urls:
        print('cache miss')
        text = requests.get(url).text
        cached_urls[url] = text
    return cached_urls[url]
```

Finally, whichever version of `cached_get` I ended up with, I'd remove the `print` statements once I had it working.


```python
cached_urls = {}

def cached_get(url):
    if url not in cached_urls:
        text = requests.get(url).text
        cached_urls[url] = text
    return cached_urls[url]
```

## More analysis

This beefed-up `analyze_page` counts the number of (lowercase) `e`s. It gets to use the same cache.


```python
def analyze_page(url):
    text = cached_get(url)
    n = 0
    for c in text:
        if c == 'e':
            n += 1
    return n
#     return len(text)

analyze_page('https://softdes.olin.build')
```

{: class="nb-output"}

    cache hit





    329




Note that I left the original `return len(text)` line in, commented-out, as a reference to look at and easily revert to while I'm working on the lines that replace it. Once it's working, I would delete the commented-out lines.

In class, I modified `analyze_page` to return a table (dictionary) listing how many upper case, and how many lower case, `e`s are in the text. Here, I'm writing a new function that does this. `analyze_page` (above) and `count_some_vowels` (below) can share the same cache – once either function is called for a given URL, applying the other function to the same URL can use the value from the cache, instead of hitting the web again.


```python
def analyze_page(url):
    text = cached_get(url)
    d = {'e': 0, 'E': 0}
    for c in text:
        if c in 'eE':
            d[c] += 1
    return d

analyze_page('https://softdes.olin.build')
```

{: class="nb-output"}




    {'E': 4, 'e': 329}




## Caching and Pickle

This concludes the material that was covered in class. This caches the value while the current Python session is running.

To save the cache *between* sessions, you will need to save it to disk. The structure of your code would look something like:


```python
import os
import pickle

cache_file_name = 'cache.pickle'
cached_urls = {}
if os.path.exists(cache_file_name):
    # use pickle.load to load the cache from disk

def cached_get(url):
    if url not in cached_urls:
        text = requests.get(url).text
        cached_urls[url] = text
        # use pickle.dump to save the cache to disk
    return cached_urls[url]
```
