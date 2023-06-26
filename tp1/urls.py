from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.index),
    path('connexion/', app.views.connexion),
    path('game/<int:id>/', app.views.game, name='game'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)