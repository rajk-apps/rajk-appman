from django.urls import path,include
from . import views
import teach
import rajksimple

urlpatterns = [
    path('', views.home, name='home'),
    path('teach/', include('teach.urls')),
    path('rajksimple/', include('rajksimple.urls'))
]