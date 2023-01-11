from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('novo/', views.adicionar_contato, name='adicionar_contato'),
    path('editar/<int:pk>', views.editar_contato, name='editar_contato'),
    path('excluir/<int:pk>', views.excluir_contato, name='excluir_contato'),
]

