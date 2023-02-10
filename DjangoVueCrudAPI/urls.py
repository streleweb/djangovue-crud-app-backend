"""DjangoVueCrudAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView)
from users.views import CreateTokenView, ManageUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todos.urls'), name='todos'),
    path('notes/', include('notes.urls'), name='notes'),
    path('users/', include('users.urls'), name='users'),
    # path('register/', CreateUserView.as_view(), name='create-user'),
    path('login/', CreateTokenView.as_view(), name='user-token'),
    path('myuser/', ManageUserView.as_view(), name='my-user'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='api-docs'),

]
