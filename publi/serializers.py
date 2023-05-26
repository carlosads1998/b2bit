from . import models
from rest_framework import serializers

class publiSerializers(serializers.ModelSerializer):
    class Meta:
        model= models.publi
        fields= '__all__'