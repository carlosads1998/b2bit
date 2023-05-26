from django.db import models
from publi.models import *

class posts(models.Model):
    feed= models.ForeignKey(publi, on_delete=models.CASCADE)

        