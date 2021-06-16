from django.shortcuts import render, redirect
from myapp.forms import StudentForm
from myapp.models import Student
# Create your views here.
def addnew(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = StudentForm()
    return render(request,'index.html',{'form':form})
#this function works for show the details
def index(request):
    students = Student.objects.all()
    return render(request,"show.html",{'students':students})

#this function works for edit the details
def edit(request, id):
    student = Student.objects.get(id=id)
    return render(request,'edit.html', {'student':student})

#this function works for update the existing details
def update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance = student)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'edit.html', {'student': student})

#this function works for deleted the details
def destroy(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/")