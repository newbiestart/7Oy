from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action


from .models import Course, Student, Enrollment
from .serializers import CourseSerializer, StudentSerializer, EnrollmentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        qs = Course.objects.all()

        status_param = self.request.GET.get("status")
        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")

        if status_param:
            qs = qs.filter(status=status_param)

        if min_price:
            qs = qs.filter(price__gte=min_price)

        if max_price:
            qs = qs.filter(price__lte=max_price)
        return qs

    @action(detail=True, methods=['get'])
    def students(self, request, pk=None):
        enrollments = Enrollment.objects.filter(course_id=pk)
        students = [e.student for e in enrollments]
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    @action(detail=True, methods=['get'])
    def courses(self, request, pk=None):
        enrollments = Enrollment.objects.filter(student_id=pk)
        courses = [e.course for e in enrollments]
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
