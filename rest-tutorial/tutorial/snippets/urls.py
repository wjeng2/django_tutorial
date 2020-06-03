# from django.urls import path
# from snippets import views
# new tutorial 2
# from rest_framework.urlpatterns import format_suffix_patterns

#tutorial 6 w/out router
# from snippets.views import SnippetViewSet, UserViewSet, api_root
# from rest_framework import renderers

#tutorial 6 w/ router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views


"""
---------------------
Original
---------------------
"""

# snippet_list = SnippetViewSet.as_view({
# 	'get': 'list',
# 	'post': 'create'

# 	})
# snippet_detail = SnippetViewSet.as_view({
# 	'get': 'retrieve',
# 	'put': 'update',
# 	'patch': 'partial_update',
# 	'delete': 'destroy'
# 	})
# snippet_highlight = SnippetViewSet.as_view({
# 	'get': 'highlight'
# 	}, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
# 	'get': 'list'
# 	})
# user_detail = UserViewSet.as_view({
# 	'get': 'retrieve'
# 	})


# urlpatterns = [
# 	path('', api_root),
# 	path('snippets/', snippet_list, name='snippet-list'),
# 	path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
# 	#tutorial 4 inclusion
# 	path('users/', user_list, name='user-list'),
# 	path('users/<int:pk>/', user_detail, name='user-detail'),
	
# 	path('snippets/<int:pk>/highlight', snippet_highlight, name='snippet-highlight')
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)


"""
---------------------
Router
---------------------
"""

#create router and register viewset
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

#API URLS determined automatically
urlpatterns =[
	path('', include(router.urls)),
]