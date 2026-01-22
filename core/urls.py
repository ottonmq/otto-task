from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), # Aquí sucede la magia del login
    path('', include('tasks.urls')),
]
