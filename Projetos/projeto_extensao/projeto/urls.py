from django.urls import path

from . import views

app_name = 'projeto'

urlpatterns = [
  path('lista/', views.projetoList, name='lista'),
  path('detalhe/<int:projeto_id>/', views.projetoDetail, name='detalhe'),
]