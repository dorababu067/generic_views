from django.conf.urls import url
from cbsviews.views import (IndexView,
							SchoolListView,
							SchoolDetailsView,
							SchoolCreatView,
							SchoolUpdateView,
							SchoolDeleteView,
							)

app_name = 'cbsviews'


urlpatterns =[
	url(r'^$',IndexView.as_view(),name='index'),
	url(r'^list$',SchoolListView.as_view(),name='list'),
	url(r'^details/(?P<pk>[0-9]+)/$',SchoolDetailsView.as_view(),name='details'),
	url(r'^creat$',SchoolCreatView.as_view(),name='creat'),
	url(r'^update/(?P<pk>[0-9]+)/$',SchoolUpdateView.as_view(),name='update'),
	url(r'^delete/(?P<pk>[0-9]+)/$',SchoolDeleteView.as_view(),name='delete'),

]