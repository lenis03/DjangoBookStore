from django import template

register = template.Library()


@register.filter(name='low')
def to_lowercase(value, arg):
    return f'{arg}:{value.lower()}'
