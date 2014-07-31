# coding=utf-8
from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('google_analytics/analytics.html')
def analytics():
    return {
        "analytics_id": getattr(settings, 'ANALYTICS_ID', None),
        "sitename": getattr(settings, 'ANALYTICS_SITENAME', None)
    }
