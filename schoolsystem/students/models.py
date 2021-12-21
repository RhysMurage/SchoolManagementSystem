from django.db import models
from django.db.models.base import Model

# Create your models here.
from django.shortcuts import renders



class ClassStreams(models.Model):
    class_stream = models.CharField(max_length=10)

    def __str__(self):
        return self.class_stream

class ClassGrade(models.Model):
    grade = models.IntegerField(default=1)


class StudentClassInfo(models.Model):
    class_grade = models.ForeignKey(ClassGrade, on_delete=models.CASCADE, related_name='')
    class_name = models.ForeignKey(ClassStreams, on_delete=models.CASCADE, related_name='')
    population = models.IntegerField(default=1)
 
    def __str__(self):
        return self.class_name
 
 
class Subjects(models.Model):
    subject_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subject_name
 
 
class StudentShiftInfo(models.Model):
    """
    Indicates whether the student is a dayscholar or boarder
    """
    shift_name = models.CharField(max_length=100)
 
    def __str__(self):
        return self.shift_name
 
 
class StudentInfo(models.Model):
    academic_year = models.CharField(max_length=100)
    admission_date = models.DateField()
    admission_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    class_type = models.ForeignKey(StudentClassInfo, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    shift_type = models.ForeignKey(StudentShiftInfo, on_delete=models.CASCADE)
    fathers_name = models.CharField(max_length=100)
    fathers_id = models.IntegerField(unique=True)
    fathers_number = models.IntegerField(unique=True)
    mothers_name = models.CharField(max_length=100)
    mothers_id = models.IntegerField(unique=True)
    mothers_number = models.IntegerField()
 

    def __str__(self):
        return self.name
 
 
class DutyTeacher(models.Manager):
    def create_attendance(self, student_class, student_id):
        student_obj = StudentInfo.objects.get(
            class_type__class_short_form=student_class,
            admission_id=student_id
        )
        attendance_obj = Attendance.objects.create(student=student_obj, status=1)
        return attendance_obj
 
 
class Attendance(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)
 
    objects = DutyTeacher()
 

    def __str__(self):
        return self.student.admission_id
