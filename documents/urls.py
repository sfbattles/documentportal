from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('docportal',views.DocumentAllView) # how we access it from the website

urlpatterns = [
   path('',include(router.urls)),
]