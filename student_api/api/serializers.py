from rest_framework import serializers
from api import models

class Instituteserializer(serializers.ModelSerializer):
    class Meta:
        model = models.Institute
        fields = '_all_'


class Studentserializer(serializers.ModelSerializer):
    Institute = Instituteserializer(read_only=True)
    class Meta:
        model = models.Student
        field=  '_all_'