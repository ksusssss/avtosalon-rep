from django.shortcuts import render
from .forms import FormRequestCall, FormServiceRegistration
from .models import AvtoModel, AllAvto


def index(request):
    models_list = AvtoModel.objects.all()
    return render(request, 'main_page.html', {'models_list': models_list})

def models_page(request):
    models_list = AvtoModel.objects.all()
    return render(request, 'model_page.html', {'models_list': models_list})

def all_avto_page(request):
    avto_list = AllAvto.objects.all()
    return render(request, 'all_avto_page.html', {'avto_list': avto_list})

def customer_page(request):
    return render(request, 'customer.html')

def new_avto_page(request):
    avto_list = AllAvto.objects.filter(probeg=0)
    return render(request, 'new_avto_page.html', {'avto_list': avto_list})

def bu_avto_page(request):
    avto_list = AllAvto.objects.exclude(probeg=0)
    return render(request, 'bu_avto_page.html', {'avto_list': avto_list})

def users_page(request):
    return render(request, 'users.html')

def service_registration(request):
    error = ''
    if request.method == 'POST':
        form =FormServiceRegistration(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'ОШИБКА'

    form = FormServiceRegistration()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'service.html', data)

def instruction_page(request):
    models_list = AvtoModel.objects.all()
    return render(request, 'instruction_page.html', {'models_list': models_list})

def request_call_page(request):
    error = ''
    if request.method == 'POST':
        form = FormRequestCall(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'ОШИБКА'

    form = FormRequestCall()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'request_call_page.html', data)

def contact_page(request):
    return render(request, 'contact_page.html')

def request_call(request):
    error = ''
    if request.method == 'POST':
        form =FormRequestCall(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'ОШИБКА'

    form = FormRequestCall()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'test_drive_page.html', data)
