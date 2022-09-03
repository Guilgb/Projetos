from django.contrib import admin
from django.urls import path, include
from dompizzaioloApp.views import UserViewSet, FoodViewSet, OrderViewSet, ListOrderFoods
from rest_framework import routers


router = routers.DefaultRouter()

router.register('users', UserViewSet, basename='Users')
router.register('foods', FoodViewSet, basename='Foods')
router.register('orders', OrderViewSet, basename='Orders')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('users/<int>/order/', ListOrderFoods.as_view())
]
