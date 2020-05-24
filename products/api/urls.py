from django.urls import path
from products.api.views import (ProductDetailAPIView,ProductListCreateAPIView)



urlpatterns = [
    path("pro/",ProductListCreateAPIView.as_view(),name="pro-list"),
    path("pro/<int:pk>",ProductDetailAPIView.as_view(),name="pro-detail"),
       
]