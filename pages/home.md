---
permalink: /
---

## Coming Up

{% assign assignments = site.assignments | sort: due %}
{% for assignment in assignments %}
{% assign announce = assignment.announce | default: site.time %}
{% if announce <= site.time and assignment.due >= site.time %}
[{{ assignment.title }}]({{ assignment.url }})
{%- if assignment.parts %} ({{ assignment.parts[0].name }}){% endif -%}
&nbsp;is due {{ assignment.due | date: '%-H %P, %a %-d %b' }}.
{% endif %}
{% endfor %}

## Recent

{% assign assignments = site.assignments | sort: due %}
{% for assignment in assignments reversed %}
{% if assignment.due < site.time %}
[{{ assignment.title }}]({{ assignment.url }}) is due {{ assignment.due | date: '%-H %P, %a %-d %b' }}.
{% endif %}
{% endfor %}

## Office Hours

| Who           | When                      | Where                       |
|---------------|---------------------------|-----------------------------|
| Emily         | Saturday, 4-6pm           | Library                     |
| Seungin       | Sunday, 4-6pm             | Library                     |
| Duncan        | Sunday, 6-8pm             | Library                     |
| Matt          | TBD because scope         | Library                     |
| Tony          | Wednesday TBD             |                             |
| Oliver Steele | Drop in or by appointment | MH 365, or Slack to find me |

## Course Materials

* [Think Python, by Allen Downey](http://greenteapress.com/wp/think-python-2e/) is the course text
* Optional books are [on reserve in the Olin Library](https://olin.tind.io/record/1512034?ln=en)
