from django.urls import path
from .views import *
from .serializer import *
urlpatterns = [
    path('PositionJob/', Api.as_view(model=PositionJob, serializer=PositionJobSerializer, model_name='PositionJob')),
    path('PositionJob/<int:pk>/', Api.as_view(model=PositionJob, serializer=PositionJobSerializer, model_name='PositionJob')),

    path('Status/', Api.as_view(model=Status, serializer=StatusSerializer, model_name='Status')),
    path('Status/<int:pk>/', Api.as_view(model=Status, serializer=StatusSerializer, model_name='Status')),

    path('Employee/', Api.as_view(model=Employee, serializer=EmployeeSerializer, model_name='Employee')),
    path('Employee/<int:pk>/', Api.as_view(model=Employee, serializer=EmployeeSerializer, model_name='Employee')),

    path('Order/', Api.as_view(model=Order, serializer=OrderSerializer, model_name='Order')),
    path('Order/<int:pk>/', Api.as_view(model=Order, serializer=OrderSerializer, model_name='Order')),
]
