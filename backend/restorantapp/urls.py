from django.urls import path, include
import restorantapp.views as views

urlpatterns = [
    path('index/',  views.index , name="index"),
]
