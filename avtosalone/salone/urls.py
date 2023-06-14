from django.urls import path
from . import views
from django.views.generic import DetailView
from .models import AvtoModel, AllAvto

urlpatterns = [
    path('', views.index, name='index'),
    path('models/', views.models_page, name='models_page'),
    path('all_avto/', views.all_avto_page, name='all_avto_page'),
    path('models/<int:pk>/', DetailView.as_view(model=AvtoModel, template_name='page_of_model.html')),
    path('customer/', views.customer_page, name='customer'),
    path('customer/new_avto_page/', views.new_avto_page, name='new_avto_page'),
    path('customer/new_avto_page/<int:pk>/', DetailView.as_view(model=AllAvto, template_name='page_of_new_car.html')),
    path('customer/bu_avto_page/', views.bu_avto_page, name='bu_avto_page'),
    path('customer/bu_avto_page/<int:pk>/', DetailView.as_view(model=AllAvto, template_name='page_of_bu_car.html')),
    path('users/', views.users_page, name='users'),
    path('users/service_registration/', views.service_registration, name='service_registration'),
    path('users/instruction/', views.instruction_page, name='instruction_page'),
    path('contact_page/', views.contact_page, name='contact_page'),
    path('test-drive/', views.request_call, name='test-drive'),
    path('request_call/', views.request_call_page, name='request_call'),
]
