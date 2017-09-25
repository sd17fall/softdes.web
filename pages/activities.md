---
permalink: activities/
title: Activities
omit_title: true
---

## Instructions

* [Recursion Practice]({% link _activities/recursion.md %})
* [Set Up Your Development Environment]({% link _activities/setup.md %})

## Handouts

<ul>
{% for page in site.html_pages %}
  {% assign test = page.url | replace: '/files/activities/day' %}
  {% if page.url != test %}
  {% assign components = page.url | split: '/' %}
  <li><a href="{{ page.url }}">{{ components[-1] | split: '.' | first }}</a></li>
  {% endif %}
{% endfor %}
</ul>
