import json

from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q

from Customers.models import CustomerProfile

# Create your views here.



def autocomplete(request):

	if 'term' in request.GET:
		qs = CustomerProfile.objects.filter(name__icontains=request.GET.get('term'))|\
		CustomerProfile.objects.filter(address__icontains=request.GET.get('term'))

		name = list()
		for profile in qs:
			name.append(profile.name)


		return JsonResponse(name, safe=False)
	return render(request, './home.html')