from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.db import models

urlpatterns = [
    path('profile/',views.profile ),
]


