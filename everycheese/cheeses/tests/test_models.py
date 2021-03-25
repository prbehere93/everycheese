import pytest
from ..models import cheese

#connect the tests with our db
pytestmark=pytest.mark.django_db

def test___str__():
    cheese1 = cheese.objects.create(name="Stracchino",
    description="Semi-sweet cheese that goes well with starches.",firmness=cheese.Firmness.SOFT,
    )
    assert cheese1.__str__() == "Stracchino"
    assert str(cheese1) == "Stracchino"
