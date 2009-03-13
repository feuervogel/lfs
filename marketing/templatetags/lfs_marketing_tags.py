# django imports
from django import template

# lfs imports
import lfs.marketing.utils

register = template.Library()

@register.inclusion_tag('marketing/topseller_portlet.html', takes_context=True)
def topseller_portlet(context, limit):
    """Displays topseller
    """
    topseller = lfs.marketing.utils.get_topseller(limit)
    return {
        "topseller" : topseller,
    }

@register.inclusion_tag('marketing/topseller_portlet.html', takes_context=True)
def topseller_for_category_portlet(context, category, limit):
    """Displays topseller
    """
    topseller = lfs.marketing.utils.get_topseller_for_category(category, limit)
    return {
        "topseller" : topseller,
    }
