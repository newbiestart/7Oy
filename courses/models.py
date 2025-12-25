from django.db import models

class Course(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title


class Student(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.full_name


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')  

    def __str__(self):
        return f"{self.student} -> {self.course}"
