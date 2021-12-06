from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Endereco, Anunciante, Contato, Demanda
from core.serializers import UserSerializer, GroupSerializer, EnderecoSerializer, AnuncianteSerializer, ContatoSerializer, DemandaSerializer

    
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    
class EnderecoViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os Enderecos sejam visualizados ou editados.
    """
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    
class AnuncianteViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os Anunciantes sejam visualizados ou editados.
    """
    queryset = Anunciante.objects.all()
    serializer_class = AnuncianteSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    
class ContatoViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os Contatos sejam visualizados ou editados.
    """
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    
    
class DemandaViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os Demandas sejam visualizados ou editados.
    """
    queryset = Demanda.objects.all()
    serializer_class = DemandaSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    
