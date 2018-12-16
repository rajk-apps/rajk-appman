from django.contrib import admin
from .models import *
from . import urls
from pip._internal import main as pipmain
import subprocess
import io
from contextlib import redirect_stdout

'https://api.github.com/users/rajk-apps/repos'

def update_applist(modeladmin, request, queryset):
    for u in urls.urlpatterns:
        try:
            u.app_name
        except:
            continue
        if u.app_name != 'admin':
            
            newapp = App()            
            newapp.id = u.app_name
            
            f = io.StringIO()
            with redirect_stdout(f):
                pipmain(['show',u.app_name])
            out = f.getvalue()
            if 'Summary:' in out:
                newapp.description = out.split('Summary:')[-1].split('\n')[0].strip()
            
            if 'Home-page:' in out:
                newapp.link = out.split('Home-page:')[-1].split('\n')[0].strip()
            
            if 'Version:' in out:
                newapp.version = out.split('Version:')[-1].split('\n')[0].strip()
    
            newapp.save()

def update_app(modeladmin, request, queryset):
    
    print('UPDATING!!')
    
    for a in queryset:
        app_name = a.id
        f = io.StringIO()
        with redirect_stdout(f):
            pipmain(['show',app_name])
        out = f.getvalue()
        
        if 'Home-page:' in out:
            page = out.split('Home-page:')[-1].split('\n')[0].strip()
            subprocess.call(['pip','uninstall',app_name,'-y'])
            subprocess.call(['pip','install','git+' + page])
    
    update_applist(modeladmin, request, queryset)
    
@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    actions = [update_applist]

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    actions = [update_app]