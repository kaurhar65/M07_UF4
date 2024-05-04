# fichero en app, para todas las ruatas del proyecto.
from django.urls import path
from . import views

urlpatterns=[
# ------------urls para la práctica 1------------------------
    # path('', views.infoPaginaPrincipal, name='principal'),    
    # path('centre/students/', views.infoStudents, name='students'),
    # path('centre/teachers/', views.infoTeachers, name='teachers'),
    # path('centre/teachers/teacher/<int:id>', views.infoTeacher, name='teacher'),

# ------------urls para la práctica 2------------------------
    path('', views.index, name='principal'),
    path('centre/students/', views.userStudents, name='students'),
    path('centre/teachers/', views.userTeachers, name='teachers'),
    path('centre/users/user/<str:pk>', views.userById, name='user'),
    path('user-form/', views.user_form, name='user_form'),
    path('update/<str:pk>', views.updateUser, name='update'),
    path('delete/<str:pk>', views.deleteUser, name='delete'),
]


