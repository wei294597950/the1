from  django import template
from the1.settings import IS_DEVELOP
register = template.Library

@register.filter
def assets(value):
    if IS_DEVELOP:
        return "/static/" + value
    value = "/static/assets/" + value
    return value