from django.contrib import admin
from .models import AllAvto
from .models import ServiceRegistration
from .models import RequestCall
from .models import AvtoModel

# Register your models here.

admin.site.register(AllAvto)
admin.site.register(ServiceRegistration)
admin.site.register(RequestCall)
admin.site.register(AvtoModel)
