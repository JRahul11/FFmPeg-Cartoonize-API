from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import CartoonizeVideo

urlpatterns = [
    path('admin/', admin.site.urls),

    path('cartoonizeVideo/', CartoonizeVideo.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
