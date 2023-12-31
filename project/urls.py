
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
  path('i18n/', include('django.conf.urls.i18n')),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls')) ,
    path('accounts/',include('accounts.urls')) 

]
# Media setting #
if settings.DEBUG is True:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


