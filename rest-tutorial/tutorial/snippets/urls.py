from django.urls import path
from snippets import views
# new tutorail 2
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	path('snippets/', views.snippet_list),
	path('snippets/<int:pk>/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)