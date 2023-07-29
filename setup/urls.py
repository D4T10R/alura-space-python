from django.urls import path, include
from django.contrib import admin
from galeria.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls'))
]
