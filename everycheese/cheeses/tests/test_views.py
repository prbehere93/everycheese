import pytest
from pytest_django.asserts import (assertContains, assertRedirects)
from django.urls import reverse
from django.contrib.sessions.middleware \
import SessionMiddleware
from django.test import RequestFactory
from everycheese.users.models import User
from ..models import cheese
from ..views import (
CheeseCreateView,
CheeseListView,
CheeseDetailView
)
from .factories import CheeseFactory

pytestmark = pytest.mark.django_db

def test_good_cheese_list_view(rf):
    # Get the reauest
    request = rf.get(reverse("cheeses:list"))
    # Use the request to get the response
    response = CheeseListView.as_view()(request)
    # Test that the response is valid
    assertContains(response, 'Cheese List')

def test_good_cheese_detail_view(rf):
    # Order some cheese from the CheeseFactory
    cheese = CheeseFactory()    
    #make a request for the new cheese
    url=reverse("cheeses:detail",kwargs={'slug':cheese.slug})
    request = rf.get(url)

    #using the request to get a response
    callable_obj=CheeseDetailView.as_view()
    response=callable_obj(request,slug=cheese.slug)
    #test for a valid response
    assertContains(response,cheese.name)

def test_good_cheese_create_view(rf, admin_user):
    cheese=CheeseFactory()
    #make a request for the newly created cheese
    request = rf.get(reverse("cheeses:add"))
    #add an authenticated user
    request.user=admin_user
    #use the request to get a response
    response=CheeseCreateView.as_view()(request)
    #test for a valid response
    assert response.status_code==200

def test_cheese_list_contains_2_cheeses(rf):
    # Let's create a couple cheeses
    cheese1 = CheeseFactory()
    cheese2 = CheeseFactory()
    # Create a request and then a response
    # for a list of cheeses
    request = rf.get(reverse('cheeses:list'))
    response = CheeseListView.as_view()(request)
    # Assert that the response contains both cheese names
    # in the template.
    assertContains(response, cheese1.name)
    assertContains(response, cheese2.name)

def test_detail_contains_cheese_data(rf):
    cheese = CheeseFactory()
    # Make a request for our new cheese
    url = reverse("cheeses:detail",kwargs={'slug': cheese.slug})
    request = rf.get(url)
    # Use the request to get the response
    callable_obj = CheeseDetailView.as_view()
    response = callable_obj(request, slug=cheese.slug)
    # Let's test our Cheesy details!
    assertContains(response, cheese.name)
    assertContains(response, cheese.get_firmness_display())
    assertContains(response, cheese.country_of_origin.name)

def test_cheese_create_form_valid(rf, admin_user):
    # Submit the cheese add form
    form_data = {
    "name": "Paski Sir",
    "description": "A salty hard cheese",
    "firmness": cheese.Firmness.HARD
    }
    request = rf.post(reverse("cheeses:add"), form_data)
    request.user = admin_user
    response = CheeseCreateView.as_view()(request)
    # Get the cheese based on the name
    cheese1 = cheese.objects.get(name="Paski Sir")
    # Test that the cheese matches our form
    assert cheese1.description == "A salty hard cheese"
    assert cheese1.firmness == cheese.Firmness.HARD
    assert cheese1.creator == admin_user