from django.urls import path
from snippets import views
# new tutorail 2
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
	path('', views.api_root),
	path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
	path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
	#tutorial 4 inclusion
	path('users/', views.UserList.as_view(), name='user-list'),
	path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
	
	path('snippets/<int:pk>/highlight', views.SnippetHighlight.as_view(), name='snippet-highlight')
]

urlpatterns = format_suffix_patterns(urlpatterns)