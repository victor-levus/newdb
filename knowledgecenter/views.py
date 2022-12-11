from pprint import pp, pprint
from django.http import HttpResponse
from django.shortcuts import render
from requests import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated

from knowledgecenter.models import Coordinator, Programme, Student
from knowledgecenter.serializers import CoordinatorSerializer, ProgrammeSerializer, StudentSerializer

# Create your views here.
# def say_hello(request):
#     return render( request, 'hello.html', {'name': 'Mosh'} )


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    # def create(self, request, *args, **kwargs):
    #     pprint(request.data)
    #     return Response('ok')



    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class ProgrammeViewSet(ModelViewSet):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer



class CoordinatorViewSet(ModelViewSet):
    queryset = Coordinator.objects.all()
    serializer_class = CoordinatorSerializer