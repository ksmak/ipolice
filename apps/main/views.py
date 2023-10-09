from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Item, Info
from .serializers import (
    CategorySerializer,
    ItemSerializer,
    InfoSerializer,
)


class CategoryViewSet(ReadOnlyModelViewSet):
    """
    Category viewset.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny, )


class ItemViewSet(ReadOnlyModelViewSet):
    """
    Item viewset.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (AllowAny, )
    
    @action(detail=False)
    def last(self, request):
        limit = request.query_params.get('limit', '10')
        items = Item.objects.all()[:int(limit)]
        return Response(self.serializer_class(items, many=True).data)
    

class InfoViewSet(ReadOnlyModelViewSet):
    """
    Info viewset.
    """
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = (AllowAny, )