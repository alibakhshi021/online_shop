{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ user.name }}
{% endblock %}

{% block html %}
This is an <strong>html</strong> message.
<img src='https://www.google.com/url?sa=i&url=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fimage&psig=AOvVaw2dmEWrZ01NwWeQN9EGUjx4&ust=1752821894069000&source=images&cd=vfe&opi=89978449&ved=0CBYQjRxqFwoTCNigqsuow44DFQAAAAAdAAAAABAL'>
{% endblock %}