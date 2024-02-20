from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import SomeItem
from .serializers import SomeItemSerializer
from .permissions import IsOwnerOrReadOnly

class SomeItemList(ListCreateAPIView):
    queryset = SomeItem.objects.all()
    serializer_class = SomeItemSerializer
    permission_classes = [IsOwnerOrReadOnly]

class SomeItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = SomeItem.objects.all()
    serializer_class = SomeItemSerializer
    permission_classes = [IsOwnerOrReadOnly]

