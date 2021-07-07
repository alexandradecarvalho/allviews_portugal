from django import template

register = template.Library()

@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)

@register.filter
def mystrip(str1, str2):
    result = ""
    for character in str1:
        if character != " ":
            result += character
    return result