from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('confirmarVoto/<int:id>/<str:cedula>',views.confirmarVoto,name="confirmarVoto"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
