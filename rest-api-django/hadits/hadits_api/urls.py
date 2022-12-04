from django.urls import path, include
from .views import (
    ShahihBukhariListApiView,
)

urlpatterns = [
    path('api', ShahihBukhariListApiView.as_view()),
    path('api/create', ShahihBukhariListApiView.post),
]