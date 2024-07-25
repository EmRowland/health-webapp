from django import template

register = template.Library()


@register.filter
def first_words(value):
    words = value.split()
    if words:
        return words[0]
    else:
        return ""
