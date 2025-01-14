from django.urls import path

from . import views

urlpatterns = [
    path('', views.myapp1, ),
    path('home/', views.home, ),
    path('server/', views.server, ),
    path('Four0Four/', views.Four0Four, ),
]
