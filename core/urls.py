from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("create",views.create,name="create"),
    path("login",views.login,name="login"),
    path("dashbord",views.dashbord,name="dashbord"),
    path("dashbord",views.dashbord,name="dashbord"),
    path("logout",views.logout,name="logout"),
    path("homebtn",views.homebtn,name="homebth"),
    path("newevent",views.newevent,name="newevent"),
    path("<int:id>/",views.player,name="player"),
    path("back",views.back,name="player"),
    path("<int:id>/player",views.player,name="player"),
    
]