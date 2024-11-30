from django.urls import path
from . import views

urlpatterns = [
    path("", views.OrderCreateListView.as_view(), name="order_all"),
    path("<int:order_id>/", views.OrderDetailView.as_view(), name="order"),
    path("order-status/<int:order_id>/", views.UpdateOrderStatus.as_view(), name="order-status"),
    path("user/<int:user_id>/orders/", views.UserOrdersView.as_view(), name="user-order"),
    path("user/<int:user_id>/order/<int:order_id>/", views.UserOrderDetail.as_view(), name="user-order-detail"),
]