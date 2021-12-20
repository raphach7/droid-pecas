from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from core.models import Endereco, Anunciante, Contato, Demanda
from core.serializers import UserSerializer, GroupSerializer, EnderecoSerializer, AnuncianteSerializer, ContatoSerializer, DemandaSerializer

    
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    
class EnderecoViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os Enderecos sejam visualizados ou editados.
    """
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    
class AnuncianteViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os Anunciantes sejam visualizados ou editados.
    """
    queryset = Anunciante.objects.all()
    serializer_class = AnuncianteSerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    
class ContatoViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os Contatos sejam visualizados ou editados.
    """
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    
    
class DemandaViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os Demandas sejam visualizados ou editados.
    """
    queryset = Demanda.objects.all()
    serializer_class = DemandaSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    
    def create(self, request, *args, **kwargs):
        dados=request.data
        try:
            anunciante = Anunciante.objects.get(usuario=request.user)
        except:
            return Response({"detail": "Usuário não é anunciante"}, status=status.HTTP_400_BAD_REQUEST)
        endereco, e = Endereco.objects.get_or_create(cep=dados["endereco_entrega"]["cep"],
                                                      rua=dados["endereco_entrega"]["rua"],
                                                      numero=dados["endereco_entrega"]["numero"] if "numero" in dados else "sn",
                                                      bairro=dados["endereco_entrega"]["bairro"],
                                                      estado=dados["endereco_entrega"]["estado"],
                                                      cidade=dados["endereco_entrega"]["cidade"],
                                                      complemento=dados["endereco_entrega"]["complemento"] if "complemento" in dados else ""
                                                    )
        contato, c = Contato.objects.get_or_create(ddd=dados["contato"]["ddd"],
                                                    celular=dados["contato"]["celular"],
                                                  )
        demanda = Demanda.objects.create(anunciante=anunciante,
                                            endereco_entrega=endereco,
                                            descricao=dados["descricao"],
                                            contato=contato
                                        )
        return Response(DemandaSerializer(demanda).data, status=status.HTTP_201_CREATED)
    
    def get_queryset(self):
        return Demanda.objects.filter(anunciante__usuario=self.request.user)
    
    def update(self, request, pk=None):
        dados=request.data
        demanda = Demanda.objects.get(id=pk)
        if demanda.anunciante.usuario == request.user:
            if "endereco_entrega" in dados:
                endereco, e = Endereco.objects.get_or_create(cep=dados["endereco_entrega"]["cep"],
                                                               rua=dados["endereco_entrega"]["rua"],
                                                               numero=dados["endereco_entrega"]["numero"] if "numero" in dados else "sn",
                                                               bairro=dados["endereco_entrega"]["bairro"],
                                                               estado=dados["endereco_entrega"]["estado"],
                                                               cidade=dados["endereco_entrega"]["cidade"],
                                                               complemento=dados["endereco_entrega"]["complemento"] if "complemento" in dados else ""
                                                             )
                demanda.endereco_entrega = endereco
            
            if "contato" in dados:
                contato, c = Contato.objects.get_or_create(ddd=dados["contato"]["ddd"],
                                                          celular=dados["contato"]["celular"],
                                                        )
                demanda.contato = contato

            if "descricao" in dados:
                demanda.descricao = dados["descricao"]

            if "status_finalizacao" in dados:
                demanda.status_finalizacao = dados["status_finalizacao"]
        
            demanda.save()
            return Response(DemandaSerializer(demanda).data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": f"Usuário não tem permissão para deletar essa demanda"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    
    def destroy(self, request, pk=None):
        demanda = Demanda.objects.get(id=pk)
        if demanda.anunciante.usuario == request.user:
            demanda.delete()
            return Response({"detail": f"Demanda de descrição {demanda} deletada"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": f"Usuário não tem permissão para deletar essa demanda"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    
    @action(detail=True, methods=["get"])
    def finalizar(self, request, pk=None):
        demanda = Demanda.objects.get(id=pk)
        if demanda.anunciante.usuario == request.user:
            demanda.status_finalizacao = True
            demanda.save()
            return Response({"detail": f"Demanda de descrição {demanda} finalizada"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": f"Usuário não tem permissão para finalizar essa demanda"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
