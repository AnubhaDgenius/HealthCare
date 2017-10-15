from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^health/', include('health.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),            
    url(r'^$', RedirectView.as_view(url='/health/')), 
    url(r'^captcha/', include('captcha.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
