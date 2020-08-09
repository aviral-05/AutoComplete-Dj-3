from django.db import models

# Create your models here.


class CustomerProfile(models.Model):

    name =models.CharField(max_length=70,verbose_name=' Name')
    address =models.CharField(max_length=70,verbose_name='Address')
    mobile =models.CharField(max_length=70,verbose_name='Mobile')
    gender = models.CharField(choices=(
										("0","Male"),
										("1","Female"),),
										max_length=30,
		verbose_name='Gender', null=True,blank=True)
    email =models.EmailField(max_length=70,verbose_name='Email Address')

    def __str__(self):
      return str(self.name)