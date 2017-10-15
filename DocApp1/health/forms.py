from django import forms
from health.models import Patient,Book
from django.urls.base import reverse_lazy
from captcha.fields import CaptchaField 
class PatientForm(forms.ModelForm):
    captcha = CaptchaField()    
    class Meta:
        model = Patient
        fields = ['p_age', 'p_name', 'p_addr', 'phone_number', 'p_email', 'p_img', 'disease']
        
class BookForm(forms.ModelForm):
    captcha = CaptchaField()    
    class Meta:
        model = Book
        fields = ['date','time','description']
