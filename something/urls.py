from django.urls import path
from .views import SomeItemList, SomeItemDetail
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  path("someitems/", SomeItemList.as_view(), name="someitem_list"),
  path("someitems/<int:pk>/", SomeItemDetail.as_view(), name="someitem_detail"),
  path("api-token-auth/", obtain_auth_token),
]
