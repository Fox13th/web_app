from django.shortcuts import render


def records_home(request):
    return render(request, 'records/records_home.html')
# Create your views here.
