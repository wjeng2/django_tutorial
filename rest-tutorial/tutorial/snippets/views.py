from django.shortcuts import render

# Create your views here.

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

#tutorial 1
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser

#tutorial 2
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

#tutorial 3
# from django.http import Http404 
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

#mixins
# from rest_framework import mixins
# from rest_framework import generics

#just generics
from rest_framework import generics

#tutorial 4
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly

#tutorial 5
from rest_framework.decorators import api_view
# from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

#tutorial 6
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

"""
-----------------------------------
Origianl
-----------------------------------
"""

# # @csrf_exempt
# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
# 	"""
# 	List all code snippets, or create a new snippet.
# 	"""
# 	if request.method == 'GET':
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets, many=True)
# 		# return JsonResponse(serializer.data, safe=False)
# 		return Response(serializer.data)

# 	elif request.method == "POST":
# 		# data = JSONParser().parse(request)
# 		# serializer = SnippetSerializer(data=data)
# 		serializer = SnippetSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			# return JsonResponse(serializer.data, status=201)
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		# return JsonResponse(serializer.errors, status=400)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
# 	"""
# 	Retrieve, update or delete a code snippet.
# 	"""
# 	try:
# 		snippet = Snippet.objects.get(pk=pk)
# 	except Snippet.DoesNotExist:
# 		# return HttpResponse(status=404)
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'GET':
# 		serializer = SnippetSerializer(snippet)
# 		# return JsonResponse(serializer.data)
# 		return Response(serializer.data)
# 	elif request.method == 'PUT':
# 		# data = JSONParser().parse(request)
# 		serializer = SnippetSerializer(snippet, data=request.data)
# 		# serializer = SnippetSerializer(snippet, data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			# return JsonResponse(serializer.data)
# 			return Response(serializer.data)
# 		# return JsonResponse(serializer.errors, status=400)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	elif request.method == 'DELETE':
# 		snippet.delete()
# 		# return HttpResponse(Status=204)
# 		return Response(status=status.HTTP_204_NO_CONTENT)

"""
-----------------------------
tutorial 3 class version
----------------------------
"""

# class SnippetList(APIView):
# 	"""
# 	List all snippets, or create a new snippet
# 	"""
# 	def get(self, request, format=None):
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets, many=True)
# 		return Response(serializer.data)
# 	#create
# 	def post(self, request, format=None):
# 		serializer = SnippetSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SnippetDetail(APIView):
# 	"""
# 	Retrieve, update, or delete a snippet instance.
# 	"""
# 	def get_object(self, pk):
# 		#check if exist
# 		try:
# 			return Snippet.objects.get(pk=pk)
# 		except Snippet.DoesNotExist:
# 			raise Http404

# 	#get single from pk
# 	def get(self, request, pk, format=None):
# 		snippet = self.get_object(pk)
# 		serializer = SnippetSerializer(snippet)
# 		return Response(serializer.data)

# 	#update
# 	def put(self, request, pk, format=None):
# 		snippet = self.get_object(pk)
# 		serializer = SnippetSerializer(snippet, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	#delete
# 	def delete(self, request, pk, format=None):
# 		snippet = self.get_object(pk)
# 		snippet.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)




"""
----------------------------------
tutorial 3 mixin version
----------------------------------
"""

# class SnippetList(mxins.ListModelMixin, mixins.CreateModelMixin, generics.GenercAPIView):
# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer

# 	def get(self, request, *args, **kwargs):
# 		return self.list(request, *args, **kwargs)

# 	def post(self, request, *args, **kwargs):
# 		return self.create(request, *args, **kwargs)

# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



"""
--------------------------------------
tutorial 3 generic class-based views
--------------------------------------
"""

# class SnippetList(generics.ListCreateAPIView):
# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer
# 	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
# 	#tutorial 4 override perform create to include user
# 	def perform_create(self, serializer):
# 		serializer.save(owner=self.request.user)

# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer
# 	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

"""
-----------------------------------
tutorial 4 user read-only view
-----------------------------------
"""
# class UserList(generics.ListAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer


"""
------------------------------
#tutorial 5
------------------------------
"""

#handled by router

# @api_view(['GET'])
# def api_root(request, format=None):
# 	#reverse = return fully-qualified URL?
# 	return Response({
# 		'users': reverse('user-list', request=request, format=format),
# 		'snippets': reverse('snippet-list', request=request, format=format)
# 		})

# class SnippetHighlight(generics.GenericAPIView):
# 	queryset = Snippet.objects.all()
# 	renderer_classes = [renderers.StaticHTMLRenderer]

# 	def get(self, request, *args, **kwargs):
# 		snippet = self.get_object()
# 		return Response(snippet.highlighted)


"""
-----------------------------------
tutorial 6 user view sets
-----------------------------------
"""
class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	generate list and detail
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer


"""
-----------------------------------
tutorial 6 snippet view set
-----------------------------------
"""

class SnippetViewSet(viewsets.ModelViewSet):
	"""
	Automatically provide list, create, retrieve, update, and destroy

	Additionally provide extra 'highlight' action
	"""

	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

	#default react to GET /  need methods argument to respond to POST
	@action (detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

	def perform_create(self, serializer):
		serializer.save(owner.self.request.user)