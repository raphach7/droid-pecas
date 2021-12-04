from django.contrib.auth.models import User, Group
from rest_framework import serializers
from core.models import Endereco


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class EnderecoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Endereco
        fields = ["cep", "rua", "numero", "bairro", "estado", "cidade", "complemento"]
        
