from rest_framework import serializers
from .models import ClassName, Parent, Student


class ClassNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = '__all__'


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'       