from django.template.defaultfilters import slugify
import factory
import factory.fuzzy
from everycheese.users.tests.factories import UserFactory
from ..models import cheese
import pytest

class CheeseFactory(factory.django.DjangoModelFactory):
    name=factory.fuzzy.FuzzyText()
    slug=factory.LazyAttribute(lambda obj:slugify(obj.name))
    description=factory.Faker('paragraph', nb_sentences=3, variable_nb_sentences=True)
    firmness = factory.fuzzy.FuzzyChoice([x[0] for x in cheese.Firmness.choices])
    country_of_origin = factory.Faker('country_code')
    creator=factory.SubFactory(UserFactory) #creates a user

    class Meta:
        model=cheese

@pytest.fixture
def cheese_1():
    return CheeseFactory()
    