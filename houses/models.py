from django.db import models
from accounts.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class LandLords(models.Model):
    """
    Stores Information about landLords of Houses
    """
    user_id = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    num_houses = models.IntegerField(default=0)

class Houses(models.Model):
    """
    Will Hold Information about the House
    """
    name = models.CharField(max_length=100, null=False, blank=False, default="")
    rent_amount = models.DecimalField(null=False, blank=False,
                                      decimal_places=2, max_digits=10)
    landlord_id = models.ForeignKey(LandLords, on_delete=models.CASCADE,
                                     null=True, blank=False)
    rating = models.PositiveSmallIntegerField(default=0, null=False, blank=False, )
    description = models.TextField()
    location = models.CharField(default="", max_length=50)
    image = models.ImageField(upload_to='house_images/', null=True, blank=True)
    # TODO implement ratings from teenants and non teenants
    #validators=[MinValueValidator(0), MaxValueValidator(5)]



class CareTaker(models.Model):
    """
    Stores Information about Caretakers
    """
    user_id = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    house_id = models.ForeignKey(Houses, null=True, on_delete=models.CASCADE)

class Teenants(models.Model):
    """
    Stores Information about Teenants
    """
    user_id = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    house_id = models.ForeignKey(Houses, null=True, on_delete=models.CASCADE)