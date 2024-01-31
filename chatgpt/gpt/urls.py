from django.urls import path
from . import views
urlpatterns = [
path('', views.gpt,name='chatbot')

]