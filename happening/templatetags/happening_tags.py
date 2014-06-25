# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.inclusion_tag('tags/event_cards.html')
def show_events(event_list):
    return {'event_list': event_list}