from django.shortcuts import render, redirect
from .models import Records
from .forms import RecordsForm
from django.views.generic import DetailView


def records_home(request):
    rec = Records.objects.order_by('-date')
    return render(request, 'records/records_home.html', {'rec': rec})


class RecordsDetailView(DetailView):
    model = Records
    template_name = 'records/details_view.html'
    context_object_name = 'record'


def create(request):
    error = ''
    if request.method == 'POST':
        form = RecordsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма была неверной"

    form = RecordsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'records/create.html', data)