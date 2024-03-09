from django.urls import path
from . import views

urlpatterns = [
    path('', views.records_home, name='records_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.RecordsDetailView.as_view(), name='record-detail'),
    path('<int:pk>/update', views.RecordsUpdateView.as_view(), name='record-update'),
    path('<int:pk>/delete', views.RecordsDeleteView.as_view(), name='record-delete')
]