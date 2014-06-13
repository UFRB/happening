from django.test import TestCase

from model_mommy import mommy

from ..models import Event, City, Discipline


class EventTestMommy(TestCase):

    def test_event_creation_mommy(self):
        party = mommy.make(Event)
        self.assertTrue(isinstance(party, Event))
        self.assertEqual(party.__unicode__(), party.name)


class CityTestMommy(TestCase):

    def test_city_creation_mommy(self):
        city = mommy.make(City)
        self.assertTrue(isinstance(city, City))
        self.assertEqual(city.__unicode__(), "%s - %s" % (city.name, city.state))


class DisciplineTestMommy(TestCase):
    def test_discipline_creation_mommy(self):
        discipline = mommy.make(Discipline)
        self.assertTrue(isinstance(discipline, Discipline))
        self.assertEqual(discipline.__unicode__(), discipline.name)