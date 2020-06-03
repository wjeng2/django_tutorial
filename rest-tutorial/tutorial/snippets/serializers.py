from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# #tutorial 4
# from django.contrib.auth.models import User

# class SnippetSerializer(serializers.ModelSerializer):
# 	#tutorail 4
# 	owner = serializers.ReadOnlyField(source='owner.username')

# 	class Meta:
# 		model = Snippet
# 		fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']

# class UserSerializer(serializers.ModelSerializer):
# 	snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

# 	class Meta:
# 		model = User
# 		fields = ['id', 'username', 'snippets']

#tutorail 5 addition
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'owner',
                  'title', 'code', 'highlight','linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']