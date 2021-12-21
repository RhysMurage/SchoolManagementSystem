from django.db import models
from django.db.models import fields

from students.models import ClassGrade, ClassStreams, StudentClassInfo

from rest_framework import serializers

class ClassStreamsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClassStreams
        fields = '__all__'

class ClassGradeSerilizer(serializers.ModelSerializer):

    class Meta:
        model = ClassGrade
        fields = '__all__'


class StudentClassInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentClassInfo
        fields = '__all__'