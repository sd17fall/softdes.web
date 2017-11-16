{% extends 'markdown.tpl' %}
{% block header -%}
---
date: %MODTIME%
source: %SOURCE%
---
{% raw %}
{% include toc %}
{% endraw %}
{% endblock header %}

{% block output_group %}
{: class="nb-output"}
{{ super() }}
{% endblock output_group %}
