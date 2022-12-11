
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet, basename='courses')

courses_router = routers.NestedDefaultRouter(router, 'courses', lookup='course')
courses_router.register('images', views.CourseImageViewSet, basename='course-images')


urlpatterns = router.urls + courses_router.urls