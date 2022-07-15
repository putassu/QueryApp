from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'queries', views.QueryListView.as_view(), name='queries'),
    re_path(r'^query/(?P<pk>\d+)$', views.query_detail_view, name='query-detail'),
]
urlpatterns += [
    re_path(r'^query/create/$', views.QueryCreate.as_view(), name='new-query')]