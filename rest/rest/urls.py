"""
URL configuration for rest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from restaurant.views import *
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'food', FoodViewSet, basename='food')
# router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),

    path('api/v1/category/', CategoryListView.as_view(), name='category-list'),  # GET для всех объектов и POST для создания
    path('api/v1/category/create', CategoryCreateView.as_view(), name='category-create'),  # GET для всех объектов и POST для создания
    path('api/v1/category/<int:pk>/', CategoryAPIDetail.as_view(), name='category-detail'),  #

    path('api/v1/users/', CustomUserListView.as_view(), name='user-list'),
    path('api/v1/users/create/', CustomUserCreateView.as_view(), name='user-create'),
    path('api/v1/users/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),

    path('api/v1/tables/', TableListView.as_view(), name='table-list'),
    path('api/v1/tables/create/', TableCreateView.as_view(), name='table-create'),
    path('api/v1/tables/<int:pk>/', TableDetailView.as_view(), name='table-detail'),

    path('api/v1/food/', FoodListView.as_view(), name='food-list'),
    path('api/v1/food/create/', FoodCreateView.as_view(), name='food-create'),
    path('api/v1/food/<int:pk>/', FoodDetailView.as_view(), name='food-detail'),

    path('api/v1/books/', BookListView.as_view(), name='book-list'),
    path('api/v1/books/create/', BookCreateView.as_view(), name='book-create'),
    path('api/v1/books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    path('api/v1/orders/', OrderListView.as_view(), name='order-list'),
    path('api/v1/orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('api/v1/orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),

    path('api/v1/order_items/', OrderItemListView.as_view(), name='orderitem-list'),
    path('api/v1/order_items/create/', OrderItemCreateView.as_view(), name='orderitem-create'),
    path('api/v1/order_items/<int:pk>/', OrderItemDetailView.as_view(), name='orderitem-detail'),

    path('api/v1/order_items_cook/', OrderItemCookListView.as_view(), name='orderitemCook-list'),
    path('api/v1/order_items_cook/create/', OrderItemCookCreateView.as_view(), name='orderitemCook-create'),
    path('api/v1/order_items_cook/<int:pk>/', OrderItemCookDetailView.as_view(), name='orderitemCook-detail'),

    path('api/v1/payments/', PaymentListView.as_view(), name='payment-list'),
    path('api/v1/payments/create/', PaymentCreateView.as_view(), name='payment-create'),
    path('api/v1/payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),

]
