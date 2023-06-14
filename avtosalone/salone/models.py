from django.db import models

# Create your models here.
choice_mod_car = (
    ('Patriot', 'Patriot'),
    ('Hunter', 'Hunter'),
    ('Пикап', 'Пикап'),
    ('Профи', 'Профи'),
    ('СГР', 'СГР'),
)

choice_fuel = (
    ('Бензин', 'Бензин'),
    ('Дизель', 'Дизель'),
)

choice_kpp = (
    ('МКПП', 'МКПП'),
    ('АКПП', 'АКПП'),
)

choice_privod = (
    ('Полный привод', 'Полный привод'),
)

#   таблица всех авто
class AllAvto(models.Model):
    mod_avto = models.CharField(max_length=7, choices=choice_mod_car)  # модель авто
    production_year = models.CharField(max_length=4)    # год производства
    probeg = models.CharField(max_length=7)     # пробег
    engin_capacity = models.CharField(max_length=3)    # объем двигателя
    engen_power = models.CharField(max_length=3)    # мощность двигателя
    fuel = models.CharField(max_length=10, choices=choice_fuel)  # топливо
    transmission = models.CharField(max_length=4, choices=choice_kpp, default='МКПП')   # кпп
    privod = models.CharField(max_length=13, choices=choice_privod)    # тип привода
    cvet_avto = models.CharField(max_length=10)     # цвет авто
    complectation = models.CharField(max_length=20)     # комплектация авто
    cena = models.CharField(max_length=8)   # цена авто
    photo_avto_1 = models.ImageField(upload_to='image/')    # фото авто 1
    photo_avto_2 = models.ImageField(upload_to='image/')  # фото авто 2
    photo_avto_3 = models.ImageField(upload_to='image/')  # фото авто 3
    description = models.TextField()    # описание

    def __str__(self):
        return self.mod_avto

#   таблица записи на сервис
choice_work_type = (
    ('Замена моторного масла и масляного фильтра', 'Замена моторного масла и масляного фильтра'),
    ('Промывка топливных баков', 'Промывка топливных баков'),
    ('Балансировка колес и перестановка по схеме', 'Балансировка колес и перестановка по схеме'),
    ('Диагностика систем управления двигателем, ABS/ESP', 'Диагностика систем управления двигателем, ABS/ESP'),
    ('Проверка суммарного люфта рулевого управления, свободного ходапедали тормоза',
     'Проверка суммарного люфта рулевого управления, свободного ходапедали тормоза'),
    ('Проверка свечей зажигания', 'Проверка свечей зажигания'),
    ('Проверка состояни колес и шин', 'Проверка состояни колес и шин'),
    ('Проверка состония передней и задней подвески, карданных валов и защитных чехлов, проверка люфта подшипников ступиц колес',
     'Проверка состония передней и задней подвески, карданных валов и защитных чехлов, проверка люфта подшипников ступиц колес'),
    ('Замена колес', 'Замена колес'),
)
class ServiceRegistration(models.Model):
    service_vin_number = models.CharField(max_length=17)     # vin-номер
    service_mod_avto = models.CharField(max_length=20, choices=choice_mod_car)  # модель авто
    service_work_type = models.CharField(max_length=130, choices=choice_work_type)    # тип работы
    service_date = models.DateField()   # дата визита, DateTimeField?
    service_customer_name = models.CharField(max_length=15)      # имя заказчика
    service_customer_phone = models.CharField(max_length=16)    # номер телефона заказчика
    service_customer_comment = models.TextField()    # комментарий заказчика
    service_personal_info = models.BooleanField()     # согласие на обработку персональных данных
    service_personal_reklama = models.BooleanField()    # согласие на рекламу

    def __int__(self):
        return self.id

#   таблица заказа обратного звонка
choice_question_type = (
    ('Запись на тест-драйв', 'Запись на тест-драйв'),
    ('Запись на просмотр авто', 'Запись на просмотр авто'),
    ('Запись на консультацию', 'Запись на консультацию'),
)

class RequestCall(models.Model):
    call_question_date = models.DateField(auto_now=True)
    call_question_type = models.CharField(max_length=23, choices=choice_question_type)   # тип вопроса
    call_mod_car = models.CharField(max_length=7, choices=choice_mod_car)      # модель авто
    call_customer_name = models.CharField(max_length=15)    # имя заказчика
    call_customer_phnum = models.CharField(max_length=16)   # номер телефона заказчика
    call_customer_comment = models.TextField()      # комментарий заказчика
    call_personal_info = models.BooleanField()  # согласие на обработку персональных данных
    call_personal_reklama = models.BooleanField()   # согласие на рекламу

    def __int__(self):
        return self.id

#   таблица всех моделей авто
class AvtoModel(models.Model):
    model_model = models.CharField(max_length=50, choices=choice_mod_car)
    model_engin_capacity = models.CharField(max_length=3)
    model_engin_power = models.CharField(max_length=3)
    model_fuel = models.CharField(max_length=10, choices=choice_fuel)
    model_transmission = models.CharField(max_length=4, choices=choice_kpp)
    model_privod = models.CharField(max_length=13, choices=choice_privod)
    model_complectation = models.CharField(max_length=20)
    model_cena = models.CharField(max_length=8)
    model_ph_1 = models.ImageField(upload_to='image/')
    model_ph_2 = models.ImageField(upload_to='image/')
    model_ph_3 = models.ImageField(upload_to='image/')
    model_instruction = models.FileField(upload_to='book/', blank=True)

    def __str__(self):
        return self.model_model
