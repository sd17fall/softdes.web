---
permalink: assignments/
---

<ul>
  {% assign assignments = site.assignments | sort: due | reverse %}
  {% for page in assignments %}
    <li><a href="{{ page.url }}">{{ page.title }}</a> – due {{ page.due | date: '%-H %P, %a %-d %b' }}</li>
  {% endfor %}
</ul>
