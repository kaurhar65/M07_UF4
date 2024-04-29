# fichero en app, para todas las ruatas del proyecto.
from django.urls import path
from . import views

urlpatterns=[
    path('', views.infoPaginaPrincipal, name='principal'),
    path('centre/students/', views.infoStudents, name='students'),
    path('centre/teachers/', views.infoTeachers, name='teachers'),
    path('centre/teachers/teacher/<int:id>', views.infoTeacher, name='teacher')
]


