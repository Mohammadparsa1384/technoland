from django import template
from product.models import Product

register = template.Library()

@register.filter()
def sep_number(number):
    return ('{:,}'.format(number))


@register.filter()
def sep_email(email):
    return email.split("@")[0]
    