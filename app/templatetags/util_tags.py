from django import template

register = template.Library()

@register.filter(name='addClass')
def addClass(value, arg):
    return value.as_widget(attrs={'class':arg})

# def changeType(value, arg):
#     return value.as_widget(attrs={'type':arg})