# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.inclusion_tag('tags/event_cards.html')
def show_events(event_list):
    """Render each event on a bootstrap thumbnail"""
    return {'event_list': event_list}


@register.inclusion_tag('tags/event_date.html')
def show_date(start_date, end_date):
    """Render the date in a especific format depending if the start and end of
    the event are on the same day, month or year."""
    return {'start_date': start_date, 'end_date': end_date}