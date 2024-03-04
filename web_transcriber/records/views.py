from django.shortcuts import render
from .models import Records


def records_home(request):
    rec = Records.objects.order_by('-date')
    return render(request, 'records/records_home.html', {'rec': rec})
# Create your views here.
