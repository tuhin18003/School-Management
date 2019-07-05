from rest_framework import viewsets, permissions
from .serializers import ClassNameSerializer, ParentSerializer, StudentSerializer
from .models import ClassName, Parent, Student


class ClassNameViewset(viewsets.ModelViewSet):
    queryset = ClassName.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClassNameSerializer


class ParentViewset(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ParentSerializer


class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentSerializer
