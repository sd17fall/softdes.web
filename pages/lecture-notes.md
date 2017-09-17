---
permalink: notes/
title: Lecture Notes
---

{% for p in site.posts limit: 1 %}
  <h1>{{ p.title }}</h1>
  {{ p.content }}
{% endfor %}

## Previous Days

<ul>
{% for p in site.posts offset: 1 %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
{% endfor %}
<ul>