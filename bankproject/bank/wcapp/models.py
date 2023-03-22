from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    # district = models.ForeignKey()
    # branch = models.ForeignKey()
    # account_type = models.ForeignKey()
    materials_provided = models.CharField(max_length=100)

    def __str__(self):
        return self.name



# Create your models here.
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
# class Person(models.Model):
#     name = models.CharField(max_length=124)
#     country = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
#     city = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)
#
#     def __str__(self):
#         return self.name


