from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

admin.site.site_header = 'FireFile Yönetimi'
admin.site.index_title = 'FireFile Yönetimi'
admin.site.site_title = 'FireFile Yönetim Paneli'

from django.urls import include
from django.urls import path

from django.conf.urls import url
from django.contrib.auth import views

from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns

from apps.main.views import *

app_name = 'metaverse_game'

urlpatterns = i18n_patterns(

    path('admin/', admin.site.urls),

    path('rosetta/', include("rosetta.urls")),

    path('', include('apps.main.urls', namespace='main')),

    path('login/', LoginView.as_view(), name="login_url"),


) + static(settings.STATIC_URL, document_root=settings.STATIC_URL) + static(settings.MEDIA_URL,
                                                                            document_root=settings.MEDIA_ROOT)
