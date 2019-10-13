from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("create",views.create,name="create"),
    path("login",views.login,name="login"),
    path("dashbord",views.dashbord,name="dashbord"),
    path("logout",views.logout,name="logout"),
    path("homebtn",views.homebtn,name="homebth")
]