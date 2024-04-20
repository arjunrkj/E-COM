from django import template

register = template.Library()

@register.simple_tag(name='status')
def ordstatus(status):
    status_list=['CART_STAGE','ORDER_CONFIRMED','ORDER_PROCESSING','ORDER_PROCESSED','ORDER_DELIVERED','ORDER_REJECTED']
    return status_list[status]