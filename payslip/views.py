from django.shortcuts import render
from .models import staff

#for geting the pdf 
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# Create your views here.

def home(request):
    getstaff = staff.objects.all()

    context = {
        'getstaff':getstaff
    }
    return render(request,'home.html',context)


def payslip(request,pk):
    pay = staff.objects.get(id=pk)
    template_path = 'payslip.html'
    logo = finders.find('logo.jpeg')
    context = {
        'pay':pay,
        'static':{
        'logo':logo
        },
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response





