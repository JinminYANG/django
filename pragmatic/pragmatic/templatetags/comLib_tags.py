from django import template

register = template.Library()

# 실행 오류
@register.inclusion_tag('header.html', takes_context=True)
def comLib_navbar(context):
    return context

