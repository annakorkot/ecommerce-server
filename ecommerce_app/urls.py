from django.urls import path
from . import views
from .views import RegisterView , RetrieveUserView


urlpatterns = [
	path('register/',RegisterView.as_view()),
	path('me/',RetrieveUserView.as_view()),
	path('product-list/', views.product_list, name="product-list"),
	path('product-detail/<str:pk>/', views.product_detail, name="product-detail"),
	path('product-create/', views.product_list, name="product-create"),
	path('product-update/<str:pk>/', views.product_detail, name="product-update"),
	path('product-delete/<str:pk>/', views.product_detail, name="product-delete"),
	path('category-list/', views.category_list , name="category-list"),
]
