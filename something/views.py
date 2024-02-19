from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import SomeItem
from .serializers import SomeItemSerializer

class SomeItemList(ListCreateAPIView):
    queryset = SomeItem.objects.all()
    serializer_class = SomeItemSerializer

class SomeItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = SomeItem.objects.all()
    serializer_class = SomeItemSerializer
