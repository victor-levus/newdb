from dataclasses import field
from rest_framework import serializers

from training.models import Course, CourseImage


class CourseImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        course_id = self.context['course_id']
        return CourseImage.objects.create(course_id=course_id, **validated_data)

    class Meta:
        model = CourseImage
        fields = ['id', 'image']

class CreateCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price']

class CourseSerializer(serializers.ModelSerializer):
    course_image = CourseImageSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'created_at', 'last_update', 'course_image']