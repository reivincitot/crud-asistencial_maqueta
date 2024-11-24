from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegionsViewSets, ProvinceViewSets, CommuneViewSets, AddressViewSets

router = DefaultRouter()
router.register(r'region', RegionsViewSets)
router.register(r'province', ProvinceViewSets)
router.register(r'commune', CommuneViewSets)
router.register(r'address', AddressViewSets)

urlPatterns = [
    path('api/', include('locations.urls')),
]
