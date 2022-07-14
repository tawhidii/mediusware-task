from django.urls import path
from product.api.views import ProductCreateView


urlpatterns = [
    path('api/create/',ProductCreateView.as_view(),name='product-create')
]