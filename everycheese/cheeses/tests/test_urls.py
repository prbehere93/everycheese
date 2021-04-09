import pytest
from django.urls import reverse, resolve
from .factories import CheeseFactory
pytestmark=pytest.mark.django_db

#creating a fixture which will be used by many of the url tests
@pytest.fixture
def cheese():
    return(CheeseFactory())

def test_list_reverse():
    "cheeses:list should reverse to /cheeses/"
    assert reverse('cheeses:list')=='/cheeses/'

def test_list_resolve():
    "/cheeses/ should resolve to cheeses:list"
    assert resolve('/cheeses/').view_name=='cheeses:list'

def test_add_reverse():
    assert reverse('cheeses:add')=='/cheeses/add/'

def test_add_resolve():
    assert resolve('/cheeses/add/').view_name=='cheeses:add'

#importing cheese objec to check for the slug
def test_detail_reverse(cheese):
    "cheeses:detail reverse should match /cheeses/cheeseslug"
    url=reverse('cheeses:detail',kwargs={'slug':cheese.slug})
    assert url==f'/cheeses/{cheese.slug}'

def test_detail_resolve(cheese):
    url=f'/cheeses/{cheese.slug}'
    assert resolve(url).view_name=='cheeses:detail'



