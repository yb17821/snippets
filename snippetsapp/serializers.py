from rest_framework import serializers
from .models import Snippet  # , LANGUAGE_CHOICE, STYLE_CHOICE
from django.contrib.auth.models import User


# class SnippetSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source="owner.username")#owner字段，用户只能读，不能写
#     highlight =serializers.HyperlinkedIdentityField(view_name="snippet_highlight",format="html")
#     class Meta:
#         model = Snippet
#         fields = ("id", "title", "code", "linenos", "language", "style","owner","highlight")


# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.HyperlinkedRelatedField(many=True,view_name="snippet-detail",read_only=True)
#     class Meta:
#         model = User
#         fields = ("id", "username","snippets")
class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True,view_name="snippet-detail",read_only=True)
    class Meta:
        model = User
        fields = ("url","id", "username","email","snippets")
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source="owner.username")#owner字段，用户只能读，不能写
    owner = serializers.HyperlinkedRelatedField(view_name="user-detail",read_only=True)
    highlight =serializers.HyperlinkedIdentityField(view_name="snippet-highlight",format="html")
    class Meta:
        model = Snippet
        fields = ("url","id","highlight","owner", "title", "code", "linenos", "language", "style")


