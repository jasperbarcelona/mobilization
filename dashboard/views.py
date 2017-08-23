from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from dashboard.models import Region, City, Barangay, Cluster, Household, Citizen, ParentChild

def index(request):
	regions = Region.objects.order_by('name')
	return render(request, 'dashboard/index.html', {'regions':regions})