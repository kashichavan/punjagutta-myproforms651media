from django import forms
from .models import EmployeeReg
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=EmployeeReg
        fields='__all__'
        widgets={
            'address':forms.Textarea()
        }
        
