
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    #Admin url
    path('admin/', admin.site.urls),

    #Store app
    path('', include('store.urls')),

    #Cart app
    path('cart/', include('cart.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
