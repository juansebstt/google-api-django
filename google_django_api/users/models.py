from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    Users profile model extends from the built-in Django User Model
    """
    # Timestamp of when the user was created
    timestamp = models.DateTimeField(auto_now_add=True)
    # Timestamp of when the user was last updated
    updated = models.DateTimeField(auto_now=True)
    # One to one relationship with the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Address fields
    address = models.CharField(verbose_name="Address", max_length=100, null=True, blank=True)
    town = models.CharField(verbose_name="Town/City", max_length=100, null=True, blank=True)
    county = models.CharField(verbose_name="County", max_length=100, null=True, blank=True)
    post_code = models.CharField(verbose_name="Post Code", max_length=8, null=True, blank=True)
    country = models.CharField(verbose_name="Country", max_length=100, null=True, blank=True)
    # Location coordinates
    longitude = models.CharField(verbose_name="Longitude", max_length=50, null=True, blank=True)
    latitude = models.CharField(verbose_name="Latitude", max_length=50, null=True, blank=True)

    # Captcha score from reCAPTCHA
    captcha_score = models.FloatField(default=0.0)
    # Flag indicating if the user has completed their profile
    has_profile = models.BooleanField(default=False)

    # Flag indicating if the user is active
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """
        Returns a string representation of the user.
        """
        return f'{self.user}'
