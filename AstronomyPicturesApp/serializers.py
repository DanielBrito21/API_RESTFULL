from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Picture

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model=Picture
        fields=['id','title','hdurl','url','explanation']