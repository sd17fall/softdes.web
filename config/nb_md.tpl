{% extends 'markdown.tpl' %}
{% block header -%}
---
omit_title: true
---
{% raw %}
{% include toc %}
{% endraw %}
{% endblock header %}

{% block output_group %}
{: class="nb-output"}
{{ super() }}
{% endblock output_group %}
