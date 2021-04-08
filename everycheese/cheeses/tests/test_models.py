import pytest
from ..models import cheese
from .factories import CheeseFactory

#connect the tests with our db
pytestmark=pytest.mark.django_db

def test___str__():
    cheese1 = CheeseFactory()
    assert cheese1.__str__() == cheese1.name
    assert str(cheese1) == cheese1.name

def test_get_absolute_url():
    cheese1=CheeseFactory()
    url=cheese1.get_absolute_url()
    assert url == f'/cheeses/{cheese1.slug}'