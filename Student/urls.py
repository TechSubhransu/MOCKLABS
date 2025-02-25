from django.urls import path
from Student.views import *
urlpatterns = [
    path("Student_home",Student_home,name="Student_home"),
    path("Student_register",Student_register,name="Student_register"),
    path("Student_login",Student_login,name="Student_login"),
    path("Student_logout",Student_logout,name="Student_logout"),
    path("my_ratings",my_ratings,name="my_ratings")
]
