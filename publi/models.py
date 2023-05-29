from django.db import models
from api.models import User

class publi(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    published= models.TextField(max_length=256)
    date= models.DateField(auto_now_add=True)
    update= models.DateField(auto_now=True)
    
    class Meta:
        verbose_name= 'publicação'
        verbose_name_plural= 'Publicações'
        
    def __str__(self):
        return self.published