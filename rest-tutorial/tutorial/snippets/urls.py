from django.urls import path
from snippets import views
# new tutorail 2
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	path('snippets/', views.SnippetList.as_view()),
	path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)