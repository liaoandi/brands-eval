'''
Company and result urls are created 
Type: Original
'''


from django.urls import path 
from . import views

urlpatterns = [
    path('', views.search, name = 'search'),
    path('company/<int:comp_id>/', views.detail, name = 'detail'),
    path(r'^result/(?P<brand_name>\w+?)/$', views.result, name = 'result')
]