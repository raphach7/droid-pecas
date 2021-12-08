# Droid Peças

## Introdução

Este é o repositório de uma API REST utilizando o Django e Django Rest Framework resposável pelo backend de uma aplicação que possibilita a publicação de cotações especificas de Droids.

## Requisito

* Docker
* Docker Compose

## O que foi usado

* PostgreSQL
* Python
* Django
* Django REST Framework
* Docker
* Docker Compose
* Test do Django REST Framework

## Como funciona

Para executar é necessário fazer a `build` usando o docker-compose:

```
docker-compose build
```

Após a build, é necessário realizar um `up` nos containes:

```
docker-compose up
```

###### Observações:

* A API está configurada para usar o arquivo `.env` com as configurações, este arquivo está no repositório.
* Para as requisições no Postman, existe uma pasta de nome `Postman` que contém o `JSON` para importar

## Considerações finais

Na modelagem, foi pensado uma estrutura onde foi criado Endereco, Contato, Anunciante e Demanda:

* Um Anunciante tem um ou mais Endereco e um ou mais Contato.
* Uma Demanda tem um Anunciante, um Endereco e um Contato.
