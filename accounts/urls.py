from django.urls import path, include
from . import views            # . == path of the file in the same file of url


app_name = 'accounts'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
]
