---
permalink: /
---

## Coming Up

{% assign assignments = site.assignments | sort: "due" %}
{% for assignment in assignments %}
{% assign announce = assignment.announce | default: site.time %}
{% if announce <= site.time and assignment.due >= site.time %}
[{{ assignment.title }}]({{ assignment.url }}) {% if assignment.parts == nil %} is due {{ assignment.due | date: '%-H:%M %P, %a %-d %b' }} {% endif %}
{% assign parts = assignment.parts | where_exp: "part", "part.due > site.time" %}
{% for part in parts limit: 1 %}
“{{ part.name }}” is due {{ part.due | date: '%-H:%M %P, %a %-d %b' }}.
{% endfor %}
{% endif %}
{% endfor %}

## Recent

{% assign assignments = site.assignments | sort: due %}
{% for assignment in assignments reversed %}
{% assign start_s = assignment.due | date: '%s' %}
{% assign d = site.time | date: '%s' | minus: start_s | divided_by: 86400 %}
{% if assignment.due < site.time and d < 5 %}
[{{ assignment.title }}]({{ assignment.url }}) was due {{ assignment.due | date: '%-H:%M %P, %a %-d %b' }}.
{% endif %}
{% endfor %}

## Office Hours

| Who     | When                      | Where                       |
|---------|---------------------------|-----------------------------|
| Duncan  | Sunday, 6-8pm             | Library                     |
| Emily   | Saturday, 4-6pm           | Library                     |
| Hannah  | Tuesdays 7-9 pm           | Library                     |
| Matt    | TBD because SCOPE         | Library                     |
| Seungin | Sunday, 4-6pm             | Library                     |
| Tony    | Wednesday TBD             |                             |
| Oliver  | Drop in or by appointment | MH 365, or Slack to find me |

## Course Materials

* [Think Python, by Allen Downey](http://greenteapress.com/wp/think-python-2e/) is the course text
* Optional books are [on reserve in the Olin Library](https://olin.tind.io/record/1512034?ln=en)
