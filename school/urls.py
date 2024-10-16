from rest_framework.routers import DefaultRouter

from school.apps import SchoolConfig
from school.views import CourseViewSet

app_name = SchoolConfig.name

router = DefaultRouter()
router.register(f'course', CourseViewSet, basename='course')

urlpatterns = [

]+router.urls
