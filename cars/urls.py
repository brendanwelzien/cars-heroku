from django.urls import path
from .views import CarList, CarDetail
# urls
urlpatterns = [
    path('', CarList.as_view(), name='car-list'),
    path('<int:pk>/', CarDetail.as_view(), name='car-detail'),
]