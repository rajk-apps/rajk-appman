Rajk Django Application Management
=====

0.0.2


## mechanics:

reads from its own urls.py file, looks for apps, if it finds one, uses pip to get github link and description. puts these apps on a home page with as cards

#### to include a new app

add it to rajk_appman/urls.py like this:

```python
import rajksimple

urlpatterns = [
    path('', views.home, name='home'),
    ...
    path('rajksimple/', include('rajksimple.urls'))
]

```

and to project/settings:

```

INSTALLED_APPS = [
	...
    'rajk_appman',
    ...
    'rajksimple'
]
```

#### update an app

in the admin page, perform action update applist on any config model

then perform action update app on any of the app models created

#### user management

handles a login page, will later handle general user management

## requirements:

project urls.py to be set like this:

```python

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rajk_appman.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

```
