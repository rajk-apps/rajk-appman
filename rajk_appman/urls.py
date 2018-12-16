from django.urls import path,include
from . import views
import teach
import rajksimple

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('teach/', include('teach.urls')),
    path('riki/', include('riki.urls')),
    path('rajksimple/', include('rajksimple.urls'))
]
