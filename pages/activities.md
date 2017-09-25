---
permalink: activities/
title: Activities
omit_title: true
---

## Instructions

<ul>
{% assign activities = site.activities | sort: 'date' %}
{% for page in activities reversed %}
<li><a href="{{ page.url }}">{{ page.title }}</a></li>
{% endfor %}
</ul>

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
