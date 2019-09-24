from rest_framework import routers
from .api import LeadViewSet
from django.urls import path, include
from django.conf.urls import url


router = routers.DefaultRouter()
router.register('leads', LeadViewSet, 'leads')

urlpatterns = router.urls
