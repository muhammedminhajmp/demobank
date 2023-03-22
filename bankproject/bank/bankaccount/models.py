# from django.db import models
#
#
#
# class Account(models.Model):
#     name = models.CharField(max_length=100)
#     dob = models.DateField()
#     age = models.IntegerField()
#     gender = models.CharField(max_length=12)
#     phone_number = models.CharField(max_length=12)
#     email = models.EmailField()
#     password = models.CharField(max_length=10)
#     address = models.CharField(max_length=250)
#     # class Meta:
#     #     fields=['name','age']
# # Create your models here.
#
#
#  # district = models.ChoiceField(
#  #  choices=[(‘thrissur’, ‘Thrissur’), (‘ernamkulam’, ‘Ernamkulam’), (‘palakkad’, ‘Palakkad’), (‘kottayam’, ‘Kottayam’),
#  #           (‘trivandrum’, ‘Trivandrum’)])
#  # branch = models.ChoiceField(choices=)
#  # account_type = models.ChoiceField(choices=[(‘savings’, ‘Savings’), (‘current’, ‘Current’)])
#  # materials_required = models.MultipleChoiceField(
#  #  choices=[(‘debit’, ‘Debit Card’), (‘credit’, ‘Credit Card’), (‘cheque’, ‘Chequebook’)],
#  #  widget=models.CheckboxSelectMultiple)
#  #  class Meta:
#  #   fields=['name','password']
#
from django.db import models


# class District(models.Model):
#     name = models.CharField(max_length=40)
#
#     def __str__(self):
#         return self.name
#
#
# class Branch(models.Model):
#     country = models.ForeignKey(District, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)
#
#     def __str__(self):
#         return self.name
#
#
# class Account(models.Model):
#     name = models.CharField(max_length=124)
#     district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
#     branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)
#
#     def __str__(self):
#         return self.name


#

