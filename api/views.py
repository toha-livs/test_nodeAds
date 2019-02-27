from rest_framework import viewsets
from rest_framework.decorators import api_view

from api.models import Group, Element
from api.serializers import GroupSerialize, ElementSerialize


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerialize


class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerialize


@api_view(['POST'])
def element(request):
    return None