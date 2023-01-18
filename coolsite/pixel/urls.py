from django.urls import path

from .views import *

urlpatterns = [
    path('', PixelHome.as_view(), name='home'),
    path('about/',about_us,name='about'),
    path('best/', Bests.as_view(), name='best'),
    path('categorie/',Categorie.as_view(), name='categorie'),
    path('addgame/', Addgame.as_view(), name='addgame'),
    path('best/<int:name_id>/', show_best, name='show_best'),
    path('categorie/<str:name_id>/', show_janr, name='show_janr'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
]