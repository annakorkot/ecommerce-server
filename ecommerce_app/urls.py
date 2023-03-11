from django.urls import path
from . import views
from .views import RegisterView , RetrieveUserView ,productDetail


urlpatterns = [
	path('register/',RegisterView.as_view()),
	path('me/',RetrieveUserView.as_view()),
	path('product/', views.product_list, name="product-list"),
	path('product/<str:pk>', productDetail.as_view(), name="product"),
	#path('product-detail/<str:pk>/', productDetail.as_view(), name="product-detail"),
	#path('product-create/', views.product_list, name="product-create"),
	# path('product-update/<str:pk>/', productDetail.as_view(), name="product-update"),
	# path('product-delete/<str:pk>/', productDetail.as_view(), name="product-delete"),
	path('category/', views.category_list , name="category-list"),
	path('category/<str:pk>/product/', views.get_products_by_category , name="products-by-category"),
]
