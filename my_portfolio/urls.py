
#from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
#    path('admin/', admin.site.urls),
    path('wchome/', views.wchomepage),
    path('wchome/count', views.wccount, name='wccount'),

]
