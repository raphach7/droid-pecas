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

Copie `.env-exemple` para `.env` e configure as variáveis de ambiente.

```shell
cp .env-exemple .env
```

Para executar é necessário fazer a `build` usando o docker-compose:

```
docker-compose build
```

Após a build, é necessário realizar um `up` nos containes:

```
docker-compose up
```

Dentro do container, também é necessário criar um superuser:

```
./manage.py createsuperuser
```

Com isso o admin estará funcionando e possível acessar.

A criação de um Anunciante só é possível pela tela de admin. Com o Anunciante criado, é necessário passar as credenciais dentro do Postman.

O Anunciante só pode manipular e ver as suas próprias demandas.

##### Teste

O teste pode ser executado dentro do container `api`:

```
docker-compose exec api bash
./manage.py test
```

Esse teste irá testar a criação de uma Demanda, listagem de Demandas, ver Demanda, alterar Demanda, finalizar Demanda e deletar Demanda

###### Observações:

* A API está configurada para usar o arquivo `.env` com as configurações, este arquivo está no repositório.

## Considerações finais

Na modelagem, foi pensado uma estrutura onde foi criado Endereco, Contato, Anunciante e Demanda:

* Um Anunciante tem um ou mais Endereco e um ou mais Contato.
* Uma Demanda tem um Anunciante, um Endereco e um Contato.
