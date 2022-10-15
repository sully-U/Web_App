from django.urls import path

from . import views

# app_name = "register"
# app_name2 = "homepage"
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.register, name="register"),
    path('', views.homepage, name='homepage')
]