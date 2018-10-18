"""NaturalSearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from natural_search.views import home
from rest_framework import routers
from natural_search.views import ProjetoListViewSet, PropositionViewSet, ProponentViewSet

router = routers.DefaultRouter()
router.register('projeto', ProjetoListViewSet)
router.register('propostas', PropositionViewSet)
router.register('proponente', ProponentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('api-RedeCultural', include('rest_framework.urls'))
]

urlpatterns += router.urls
