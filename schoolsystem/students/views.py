from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from django.forms import CreateStudent


# Create your views here.
def student_list(request):
    students = StudentInfo.objects.all()
    paginator = Paginator(students, 1)
    page = request.GET.get('page')
    paged_students = paginator.get_page(page)
 
    context = {
        "students": paged_students
    }

 
 