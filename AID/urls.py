from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from.import views
#from.django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^artikel/$', views.artikel),
    url(r'^analisis/$', views.analisis),
    url(r'^$', views.homepage),
    url(r'^hasilanalisis/$', views.hasilanalisis),
    path('search_bar/', views.search_bar, name='search-bar'),
    path('admin/', admin.site.urls),
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
