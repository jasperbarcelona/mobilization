from django.conf.urls import url, include
from django.contrib import admin


admin.site.site_header = 'Essilor SMS'
urlpatterns = [
	url(r'^dashboard/', include('dashboard.urls')),
    url(r'^admin/', admin.site.urls),
]
