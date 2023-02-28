from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api/', include('base.api.urls')),
    # path('', include('main.urls')),
]

# urlpatterns = patterns(
#     '',
#     url(r'^admin/', include(admin.site.urls)),
#     url('', include('social.apps.django_app.urls', namespace='social')),
# )

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)