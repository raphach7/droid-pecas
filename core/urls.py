from django.urls import path
from django.urls import include
from rest_framework import routers
from core import views


router = routers.DefaultRouter()
# router.register(r'enderecos', views.EnderecoViewSet)
# router.register(r'anunciantes', views.AnuncianteViewSet)
# router.register(r'contatos', views.ContatoViewSet)
router.register(r'demandas', views.DemandaViewSet)
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
]