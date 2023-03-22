from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('dob', 'age', 'gender', 'phone_number', 'email', 'address',
                  'materials_provided')


# from django import forms
#
# from .models import Person, Branch
#
#
# class PersonCreationForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['city'].queryset = Branch.objects.none()
#
#         if 'country' in self.data:
#             try:
#                 country_id = int(self.data.get('country'))
#                 self.fields['city'].queryset = Branch.objects.filter(country_id=country_id).order_by('name')
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty City queryset
#         elif self.instance.pk:
#             self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
#
# # from django import forms
#
# # creating a form
# class InputForm(forms.Form):
#
#     first_name = forms.CharField(max_length = 200)
#     last_name = forms.CharField(max_length = 200)
#     roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
#     password = forms.CharField(widget = forms.PasswordInput())
