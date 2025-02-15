from django.urls import path
from .views import student_list, student_create, student_update, student_delete

urlpatterns = [
    path('', student_list, name='student_list'),
    path('add/', student_create, name='student_create'),  # Ensure this exists
    path('update/<int:pk>/', student_update, name='student_update'),
    path('delete/<int:pk>/', student_delete, name='student_delete'),
]
