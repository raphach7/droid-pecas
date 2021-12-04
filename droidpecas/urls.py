from django.urls import include, path
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]