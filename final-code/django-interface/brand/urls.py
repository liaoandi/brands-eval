'''
Create home search page url. The suffix is 'search/'
Type: Original
'''
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include('search.urls'))
]
