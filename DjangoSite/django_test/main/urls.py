from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('advantages', views.advantages, name='advantages'),
    path('Authorization', views.authorization, name='authorization'),
    path('photos', views.photos, name='photos')
]
