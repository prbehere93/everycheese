from django.db import models
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from django_countries.fields import CountryField

class cheese(TimeStampedModel):
    class Firmness(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "soft", "Soft"
        SEMI_SOFT = "semi-soft", "Semi-Soft"
        SEMI_HARD = "semi-hard", "Semi-Hard"
        HARD = "hard", "Hard"
    #fields of the model/table here
    name=models.CharField("Name of cheese",max_length=200)
    slug=AutoSlugField("Cheese Address", unique=True, always_update=False, populate_from="name")
    description=models.TextField("Description", blank=True)
    firmness=models.CharField("Firmness", max_length=25,choices=Firmness.choices,default=Firmness.UNSPECIFIED)
    country_of_origin=CountryField("Country of Origin", blank=True)

    def __str__(self):
        return self.name

# Note that we defined the firmness constants as variables within the scope of the Cheese model. This allows us to do things like
# this comparison:
# if cheese.firmness == Cheese.Firmness.SOFT:
# # Do Something
