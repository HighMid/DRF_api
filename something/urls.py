from django.urls import path
from .views import SomeItemList, SomeItemDetail

urlpatterns = [
  path("someitems/", SomeItemList.as_view(), name="someitem_list"),
  path("someitems/<int:pk>/", SomeItemDetail.as_view(), name="someitem_detail"),
]
