from django.conf.urls import url,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetsViewSet,UserViewSet
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"snippets",views.SnippetsViewSet)
router.register(r"users",views.UserViewSet)
urlpatterns = [
    url(r"^",include(router.urls)),
    url(r"^api-auth",include("rest_framework.urls",namespace="rest_framework"))
]

# snippet_list = SnippetsViewSet.as_view({
#     "get":"list",
#     "post":"create"
# })
# snippet_detail = SnippetsViewSet.as_view({
#     "get":"retrieve",
#     "put":"update",
#     "patch":"partial_update",
#     "delete":"destroy"
# })
# snippet_highlight = SnippetsViewSet.as_view({
#     "get":"highlight",
# },renderer_classes=[renderers.StaticHTMLRenderer])
#
# user_list = UserViewSet.as_view({
#     "get":"list"
# })
# user_detail = UserViewSet.as_view({
#     "get":"retrieve"
# })
#
# urlpatterns = format_suffix_patterns([#实现.python.json加不加无所谓
#     url(r"^$", views.api_root),
#     url(r"^snippets/$", snippet_list, name="snippet-list"),
#     url(r"^snippets/(?P<pk>\d+)/$", snippet_detail, name="snippet-detail"),
#     url(r"^users/$", user_list, name="user-list"),
#     url(r"^users/(?P<pk>\d+)/$", user_detail, name="user-detail"),
#     url(r"snippets/(?P<pk>\d+)/highlight/$", snippet_highlight, name="snippet_highlight")
# ])
