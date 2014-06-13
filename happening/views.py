# -*- coding: utf-8 -*-
from django.views.generic import ListView

from .models import Event


class Index(ListView):
    queryset = Event.active.order_by('-starts')
    context_object_name = 'event_list'
    paginate_by = 15