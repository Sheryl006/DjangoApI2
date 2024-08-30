
from django.contrib import admin
from django.urls import path, include



from django.conf.urls.static import static
from django.conf import settings

from api.views import ProductView, CarView,YourModelViewSet


from rest_framework import routers


route = routers.DefaultRouter()
route.register("products",ProductView)

route = routers.DefaultRouter()
route.register("cars",CarView)

router = routers.DefaultRouter()
router.register("items", YourModelViewSet)






urlpatterns = ([
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('products', ProductView.as_view({'get': 'list'})),
    path('cars', CarView.as_view({'get': 'list'})),
    path('items', YourModelViewSet.as_view({'get': 'list'}))
    

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))



