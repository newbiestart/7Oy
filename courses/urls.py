from django.urls import path, include
from rest_framework.routers import  DefaultRouter


from .views import StudentViewSet, CourseViewSet, EnrollmentViewSet

router = DefaultRouter()

router.register('courses', CourseViewSet)
router.register('students', StudentViewSet)
router.register('enrollments', EnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

