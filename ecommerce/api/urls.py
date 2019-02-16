from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()

# Register the 'products' urls in the router
router.register('products', views.ProductModelViewSet, base_name='products')

urlpatterns = []
urlpatterns += router.urls
