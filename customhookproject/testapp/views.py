from django.shortcuts import render
from testapp.models import Student
# Create your views here.
def viewpage(request):
    student_list=Student.objects.all()
    my_dict={'student_list':student_list}
    return render(request,'testapp/dowm.html',my_dict)