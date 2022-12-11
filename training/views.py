from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from training.models import Course, CourseImage
from training.serializers import CourseImageSerializer, CourseSerializer, CreateCourseSerializer


# Create your views here.

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateCourseSerializer
        if self.request.method == 'PUT':
            return CreateCourseSerializer
        return CourseSerializer


class CourseImageViewSet(ModelViewSet):
    serializer_class = CourseImageSerializer

    def get_queryset(self):
        return CourseImage.objects.filter(course_id=self.kwargs['course_pk'])

    def get_serializer_context(self):
        return {"course_id": self.kwargs['course_pk']}