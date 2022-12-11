from cgitb import lookup
from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register('students', views.StudentViewSet, basename='students')
router.register('programmes', views.ProgrammeViewSet, basename='programmes')
router.register('coordinators', views.CoordinatorViewSet, basename='coordinators')


urlpatterns = router.urls
