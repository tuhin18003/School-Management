from django.db import models

# Create your models here.

class ClassName(models.Model):
    name = models.CharField(max_length=500, unique=True)
    total_seat = models.IntegerField()


class Parent(models.Model):
    name = models.CharField(max_length=500, unique=True)
    relation_to_student = models.CharField(max_length=512)
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=2024)
    occupation = models.CharField(max_length=1024, blank=True)
    prefered_contact_time = models.CharField(max_length=1024, blank=True)


class Student(models.Model):
    name = models.CharField(max_length=200)
    roll_no = models.IntegerField()
    class_id = models.ForeignKey(ClassName, on_delete='SET_NULL')
    parent_id = models.ForeignKey(Parent, on_delete='CASCADE')



