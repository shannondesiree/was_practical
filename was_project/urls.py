from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from cats import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('cats/', include('cats.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
