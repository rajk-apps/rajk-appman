from django.shortcuts import render
from . import urls
#from pip._internal import main as pipmain
import subprocess
import io
from contextlib import redirect_stdout
from copy import copy

def home(request):
    v = []
    for u in urls.urlpatterns:
        try:
            u.app_name
        except:
            continue
        if u.app_name != 'admin':
            
            appdic = {'app_name':u.app_name}
            
            f = io.StringIO()
            with redirect_stdout(f):
                subprocess.call('pip show %s' %u.app_name)
            out = f.getvalue()
            if 'Summary:' in out:
                appdic['desc'] = out.split('Summary:')[-1].split('\n')[0].strip()
            
            if 'Home-page:' in out:
                appdic['page'] = out.split('Home-page:')[-1].split('\n')[0].strip()
            
    
            appdic['link'] = u.pattern.describe().replace('"','').replace("'",'')
            v.append(copy(appdic))

    return render(request, 'rajk-appman/home.html',
                   {'applist': v})