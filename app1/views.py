from django.shortcuts import render
from .forms import EmployeeForm
# Create your views here.

def empreg(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=EmployeeForm()
    return render(request,'form.html',{'form':form})

