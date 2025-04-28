from django.urls import path, include
from store.views.categories import CategoryViewSet
from store.views.products import ProductViewSet
from rest_framework.routers import DefaultRouter
from store.views.product_details import ProductDetailListCreateGenericView, ProductDetailRetrieveUpdateDestroyGenericView

router = DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('product_details/', ProductDetailListCreateGenericView.as_view()),
    path('product_details/<int:pk>/', ProductDetailRetrieveUpdateDestroyGenericView.as_view())

]