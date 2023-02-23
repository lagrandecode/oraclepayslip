from django.shortcuts import render
from .models import staff

# Create your views here.

def home(request):
    getstaff = staff.objects.all()

    context = {
        'getstaff':getstaff
    }
    return render(request,'home.html',context)


def payslip(request,pk):
    pay = staff.objects.get(id=pk)
    context = {
        'pay':pay
    }
    return render(request,'payslip.html',context)

