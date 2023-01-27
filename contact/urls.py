from django.urls import path, include
from . import views            # . == path of the file in the same file of url


app_name = 'contact'

urlpatterns = [
    path('', views.send_message, name='contact'),



]
