# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from ..models import Event

from model_mommy.recipe import Recipe

client = Client()


class IndexTest(TestCase):

    def setUp(self):
        last_hour = datetime.now() - timedelta(hours=1)
        # Next hour has 1 minute more because the delay between
        # the creation of the event and the test execution
        next_hour = datetime.now() + timedelta(minutes=61)
        self.event_last_hour = Recipe(Event, ends=last_hour, published=True)
        self.event_next_hour = Recipe(Event, ends=next_hour, published=True)
        self.event_unpublished = Recipe(Event, ends=next_hour, published=False)

    def test_index_response(self):
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_event_list(self):
        self.event_last_hour.make(_quantity=1)
        self.event_next_hour.make(_quantity=1)
        self.event_unpublished.make(_quantity=1)
        response = client.get(reverse('index'))
        self.assertEqual(response.context_data.get('event_list').count(), 1)


class AboutTest(TestCase):

    def test_about_response(self):
        response = client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)