from django.db import models
from django.core.validators import RegexValidator
from localflavor.us.models import USStateField, USZipCodeField
from datetime import datetime


# class ContactManager(models.Manager):
#     def get_by_natural_key(self, name):
#         return self.get(name=name)


class Contact(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?\d{10}$',
        message="Phone number must be entered in the format: '+9999999999'.")

    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=11,
                                    validators=[phone_regex],
                                    null=True,
                                    blank=True)
    address_1 = models.CharField(max_length=255, null=True, blank=True)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = USStateField(null=True, blank=True)
    zip_code = USZipCodeField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    # objects = ContactManager()


class Note(models.Model):
    text = models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=datetime.now)
    author = models.CharField(max_length=20, null=True)
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, null=True, related_name="notes")
