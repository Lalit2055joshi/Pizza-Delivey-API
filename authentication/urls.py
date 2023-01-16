from django.urls import path
from .views import AuthView,UserCreateView
urlpatterns = [
    path('',AuthView.as_view(),name='authview'),
    path('signup/',UserCreateView.as_view(),name='signup'),
]