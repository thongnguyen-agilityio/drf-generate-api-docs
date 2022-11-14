import humps
from django.contrib.auth.models import User, Group
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from tutorial.quickstart.serializers import UserSerializer, GroupSerializer, PayeeSerializer, RequestSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'test':
            self.filterset_fields = ['speed']
            return PayeeSerializer
        return UserSerializer

    @action(detail=True, methods=['get'])
    def test(self, request, pk=None):
        return Response({'test_abc': 'test'})

    @extend_schema(
        request=RequestSerializer,
        responses={200: PayeeSerializer},
        parameters=[RequestSerializer],
    )
    @action(detail=False, methods=['post'])
    def test2(self, request):
        data = request.data
        params = request.query_params
        print(data)
        print(params)
        return Response({'test_abc': 'test2'})

    @extend_schema(
        request=RequestSerializer,
        responses={200: PayeeSerializer},
        parameters=[
            OpenApiParameter(name='artistName', description='Filter by artist', required=False, type=str),
            OpenApiParameter(
                name='releaseDate',
                type=OpenApiTypes.DATE,
                location=OpenApiParameter.QUERY,
                description='Filter by release date',

            ),
        ]
    )
    @action(detail=False, methods=['post'])
    def test3(self, request):
        data = request.data
        params = humps.decamelize(request.query_params)
        print(data)
        print(params)
        return Response({'test_abc': 'test3'})

    @action(detail=False, methods=['post'])
    def test4(self, request):
        """
        API to format params, body and response to camelCase
        """
        params = humps.decamelize(request.query_params)
        body = humps.decamelize(request.data)
        print(params)
        print(body)
        return Response({'test_abc': 'test4'})


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
