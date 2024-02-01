from django import template

register = template.Library()

censor_list = ['редиска']

@register.filter()
def censor(value):
    for world in censor_list:
        value = value.replace(world[1:], '*' * len(world[1:]))


@register.simple_tag()
def current_time(format_string='%b %d %Y'):
   return datetime.now().strftime(format_string)