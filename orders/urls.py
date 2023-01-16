from django.urls import path
from .views import *
urlpatterns = [
    path('',OrderCreateListView.as_view(), name='orderview'),
    path('<int:order_id>/',OrderDetailView.as_view(), name='detail'),
    path('update-status/<int:order_id>/',UpdateOrderStatusView.as_view(), name='status'),
    path('userorder/',UserOrderView.as_view(), name='userorder'),
    # path('user/<int:user_id>/order/<int:order_id>',UserOrderDetail.as_view(),name='user_specific_detail')
]