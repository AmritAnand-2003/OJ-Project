from django.urls import path, include
from rest_framework import routers
from . import views

# router = routers.SimpleRouter()
# router.register(r'regist', views.UserRegisterView)

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
]
# urlpatterns += router.urls