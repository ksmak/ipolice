from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny

from .models import Catergory, Item
from .serializers import (
    CategorySerializer,
    ItemSerializer
)


class CategoryViewSet(ReadOnlyModelViewSet):
    """
    Category viewset.
    """
    queryset = Catergory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny, )


class ItemViewSet(ReadOnlyModelViewSet):
    """
    Item viewset.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (AllowAny, )
