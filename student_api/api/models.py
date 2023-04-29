from django.db import models

# Create your models here.
GENDER={
    ("m", 'male'),
    ("f",'female'),
    ("u", 'undefined')
}
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)
    email=models.EmailField(max_length=100)
    gender=models.CharField(max_length=1 , choices=GENDER)
    percentage=models.FloatField()

    Institute = models.ForeignKey('Institute', on_delete=models.CASCADE, null=True, blank=True)
class Institute(models.Model):

    TYPES = {
        ("c", "college"),
        ("h", "high school")
    }

    name= models.CharField(max_length=200)
    type_of_institude=models.CharField(max_length=1,choices=TYPES)