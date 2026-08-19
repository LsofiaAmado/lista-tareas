from django.urls import path
from .views import TareaListCreateView, TareaDetailView


urlpatterns = [
    path('tareas/', TareaListCreateView.as_view(), name='lista-tareas'),
    path('tareas/<int:pk>/', TareaDetailView.as_view(), name='detalle-tarea'),
]