from .views import RegisterAPI,LoginAPI,AdvisiorViewSet
from knox import views as knox_views
from django.urls import path,include
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'Advisior', AdvisiorViewSet.as_view())

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
  path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    path('api/', include(router.urls))
]
