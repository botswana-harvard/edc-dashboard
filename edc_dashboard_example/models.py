from django.db import models

from edc_base.model.models import BaseUuidModel
from django_crypto_fields.fields.firstname_field import FirstnameField
from django_crypto_fields.fields.lastname_field import LastnameField


class Subject(BaseUuidModel):

    subject_identifier = models.CharField(
        max_length=25)

    first_name = FirstnameField()

    last_name = LastnameField()

    initials = models.CharField(
        max_length=25)

    dob = models.DateField()

    class Meta:
        app_label = 'edc_dashboard_example'
