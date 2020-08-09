from django.contrib import admin
from Customers.models import CustomerProfile

# Register your models here.



class CustomerProfileAdmin(admin.ModelAdmin):



	search_fields= [
		'name',
		'email',
		'mobile',
		'address',

		]
	list_display= [
		'name',
		'email',
		'mobile',
		'gender',
		
		]



admin.site.register(CustomerProfile,CustomerProfileAdmin)