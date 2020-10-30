from django import template

register = template.Library()

def range_blog(value):
    return value[0:300] + '...........'

register.filter('range_blog', range_blog)
