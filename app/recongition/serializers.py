from dataclasses import field
from rest_framework import serializers
from recongition.models import face

class faceSerializer(serializers.ModelSerializer):

    class Meta:
        model = face
        fields = ['img']