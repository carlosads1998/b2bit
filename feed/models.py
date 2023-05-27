from django.db import models
from publi.models import *

class Posts(models.Model):
    feed= models.ForeignKey(publi, on_delete=models.CASCADE)

        