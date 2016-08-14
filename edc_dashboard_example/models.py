from django.db import models

from django_crypto_fields.fields import FirstnameField, LastnameField
from edc_base.model.models import BaseUuidModel


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
