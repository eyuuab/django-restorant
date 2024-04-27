from django.urls import path, include
import restorantapp.views as views

urlpatterns = [
    path('user/',views.userHandler,name='user'),
    path('order/',  views.order , name="order"),
    path('menu/', views.menuHandler , name="menu"),
    path('payment/', views.payment, name='payment'),
]
