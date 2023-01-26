from django.urls import path, include
from . import views            # . == path of the file in the same file of url


app_name = 'accounts'

urlpatterns = [
    path('signup', views.job_list, name='job_list'),
]
