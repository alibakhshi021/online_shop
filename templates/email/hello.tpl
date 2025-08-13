{% extends "mail_templated/base.tpl" %}

{% block subject %}
Account Activate
{% endblock %}

{% block html %}
{{token}}
{% endblock %}