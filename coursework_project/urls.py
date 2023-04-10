from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView

from market.api_views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'product', MarketViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    # path('api/v1/productlist/', MarketViewSet.as_view({'get': 'list'})),
    # path('api/v1/productlist/<int:pk>/', MarketViewSet.as_view({'patch': 'update'})),
    path('', include('market.urls')),
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
