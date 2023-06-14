from django.forms import ModelForm, TextInput, Textarea, DateInput, Select, CheckboxInput
from .models import RequestCall, ServiceRegistration

class FormRequestCall(ModelForm):
    class Meta:
        model = RequestCall
        fields = ['call_question_type', 'call_mod_car', 'call_customer_name',
                  'call_customer_phnum', 'call_customer_comment', 'call_personal_info', 'call_personal_reklama']

        widgets = {
            'call_question_date': DateInput(attrs={
                'class': 'input_field',
            }),
            'call_question_type': Select(attrs={
                'class': 'Select',
                'blank': 'False',
            }),
            'call_mod_car': Select(attrs={
                'class': 'Select',
            }),
            'call_customer_name': TextInput(attrs={
                'class': 'input_field',
                'blank': 'False',
            }),
            'call_customer_phnum': TextInput(attrs={
                'class': 'input_field',
                'blank': 'False',
            }),
            'call_customer_comment': Textarea(attrs={
                'class': 'input_field_textarea',
                'required': 'True',
                # 'blank': 'True',
                # 'null': 'False',
            }),
            'call_personal_info': CheckboxInput(attrs={
                'class': 'checkbox',
                'blank': 'False',
            }),
            'call_personal_reklama': CheckboxInput(attrs={
                'class': 'checkbox',
            }),
        }

class FormServiceRegistration(ModelForm):
    class Meta:
        model = ServiceRegistration
        fields = ['service_vin_number', 'service_mod_avto', 'service_work_type', 'service_date',
                  'service_customer_name', 'service_customer_phone', 'service_customer_comment',
                  'service_personal_info', 'service_personal_reklama']
        widgets = {
            'service_vin_number': TextInput(attrs={
                'class': 'serv_input_field',
            }),
            'service_mod_avto': Select(attrs={
                'class': 'serv_input_field',
            }),
            'service_work_type': Select(attrs={
                'class': 'serv_input_field',
            }),
            'service_date': DateInput(attrs={
                'class': 'serv_input_field',
                'type': 'date',
            }),
            'service_customer_name': TextInput(attrs={
                'class': 'serv_input_field',
            }),
            'service_customer_phone': TextInput(attrs={
                'class': 'serv_input_field',
            }),
            'service_customer_comment': Textarea(attrs={
                'class': 'input_field_textarea',
            }),
            'service_personal_info': CheckboxInput(attrs={
                'class': 'checkbox',
                'blank': 'False',
            }),
            'service_personal_reklama': CheckboxInput(attrs={
                'class': 'checkbox',
                'blank': 'False',
            }),
        }
