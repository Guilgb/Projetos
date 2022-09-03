from dompizzaioloApp.serializer import (FoodSerializer, ListOrderFoodsSerializer,
                                        OrderSerializer,
                                        UserSerializer)
from dompizzaioloApp.models import Food, Order, User
from rest_framework import (viewsets, generics)
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListOrderFoods(generics.ListAPIView):
    def get_queryset(self):
        queryset = Order.objects.filter(name_user_id=self.kwargs['int'])
        return queryset
    serializer_class = ListOrderFoodsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
