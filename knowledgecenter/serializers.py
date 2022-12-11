from decimal import Decimal
from rest_framework import serializers

from knowledgecenter.models import Coordinator, Programme, ProgramState, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'phone', 'state', 'programme', 'programstate']

class ProgrammeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programme
        fields = ['title']

class ProgramStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramState
        fields = ['title']

class CoordinatorSerializer(serializers.ModelSerializer):
    programme = ProgrammeSerializer(many=True)
    programstate = ProgramStateSerializer(many=True,)

    class Meta:
        model = Coordinator
        fields = ['id', 'user', 'phone', 'role', 'programme', 'programstate']