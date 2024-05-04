from django.http import HttpResponse
from django.shortcuts import render
from .form import PersonaFrom
from django.shortcuts import render, redirect
from .models import Usuari

teachersList = [
    {"id":1,
     "nom":"Roger",
     "cognom":"Sobrino",
     "edat":39,
     "rol":"teacher",
     "curs":"Daw2"
    },
    {"id":2,
     "nom":"Oriol",
     "cognom":"Roca",
     "edat":25,
     "rol":"teacher",
     "curs":"Daw2"
    },
    {"id":3,
     "nom":"Juanma",
     "cognom":"San",
     "edat":24,
     "rol":"teacher",
     "curs":"Daw2"
    }
]

studentsList = [
    {"id":1,
     "nom":"David",
     "cognom":"Arg",
     "edat":20,
     "rol":"Student",
     "curs":"Daw2B"
    },
    {"id":2,
     "nom":"Harpreet",
     "cognom":"Kaur",
     "edat":23,
     "rol":"Student",
     "curs":"Daw2B"
    },
    {"id":3,
     "nom":"Laia",
     "cognom":"Rodriguez",
     "edat":24,
     "rol":"Student",
     "curs":"Daw2B"
    }
]

def infoTeachers(request):
    return render(request, 'teachers.html', {"teachers": teachersList})

def infoStudents(request):
    return render(request, 'students.html', {"students": studentsList})

def infoTeacher(request, id):
    for teacher in teachersList:
        if teacher["id"] == id:
            teacherInfo = teacher
            break
        else:
            print("Teacher not found")
    return render(request, 'teacher.html', {"teacherInfo" : teacherInfo})

def infoPaginaPrincipal(request):
    return render(request, 'paginaPrincipal.html', {"teachers": teachersList})

# --------------------Views de la práctica de CRUD------------
def user_form(request):
    form = PersonaFrom(request.POST)
    if form.is_valid():
        form.save()
        return redirect('principal')
    context = {'form':form}
    return render(request, 'form.html', context)

#Get all users
def index(request):
    allUsuers = Usuari.objects.all()
    context = {'usuaris': allUsuers}
    return render(request, 'users.html', context)

#Get all stidents
def userStudents(request):
    estudiants = Usuari.objects.filter(rol__rol='estudiant')
    context = {'estudiants': estudiants}    
    return render(request, 'students.html', context)

#Get all teachers
def userTeachers(request):
    professors = Usuari.objects.filter(rol__rol='professorat')
    context = {'professors': professors}    
    return render(request, 'teachers.html', context)

#Get user by id
def userById(request, pk):
    user = Usuari.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'user.html', context)

# update
def updateUser(request, pk):
    user = Usuari.objects.get(id=pk)
    form = PersonaFrom(instance=user)
    if request.method == 'POST':
        form = PersonaFrom(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('principal')
    else:
        context = {'form': form}
        return render(request, 'form.html', context)
    
# delete
def deleteUser(request, pk):
    user = Usuari.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('principal')
    return render(request, 'delete_object.html', {'usuari': user})