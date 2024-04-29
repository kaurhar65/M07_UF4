from django.http import HttpResponse
from django.shortcuts import render

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