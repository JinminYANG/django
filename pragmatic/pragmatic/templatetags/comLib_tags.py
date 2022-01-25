from django import template

register = template.Library()


@register.inclusion_tag('header.html', takes_context=True)
def comLib_navbar(context):
    return context


@register.inclusion_tag('footer.html', takes_context=True)
def comLib_footer(context):
    return context
