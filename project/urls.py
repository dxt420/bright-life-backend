
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
router = DefaultRouter() 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('bl.urls')),
    path('rf', include(router.urls)),
    path('api/', include('api.urls')),
    path('doc/', include('rest_framework_docs.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
