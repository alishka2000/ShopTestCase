from django.urls import path
from shop_app.views import StorageView, CategoryView

urlpatterns = [
    path('storage/', StorageView.as_view()),
    path('storage/<int:pk>', StorageView.as_view()),
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>', CategoryView.as_view()),
]
