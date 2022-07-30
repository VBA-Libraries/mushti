from django import template
register = template.Library()

@register.filter
def index(indexable, i):
    amt = indexable[i]
    if amt is None:
        return 0
    else:
        return indexable[i]

@register.filter
def complete(str, add, add2):
    return str + " " + add + " " + add2