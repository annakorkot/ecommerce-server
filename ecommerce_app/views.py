from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer , CategorySerializer
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import UserCreateSerializer ,UserSerializer
class RegisterView(APIView):

    def post(self,request):
        data = request.data
        
        serializer = UserCreateSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        user = serializer.create(serializer.validated_data)
        user_serializer = UserSerializer(user)

        return Response(user_serializer.data,status=status.HTTP_201_CREATED)
class RetrieveUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        user = request.user
        user =UserSerializer(user)

        return Response(user.data , status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def product_list(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class productDetail(APIView):
    permission_classes = [permissions.IsAuthenticated , permissions.IsAdminUser]

    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
    def get(self ,request,pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        product_serializer =ProductSerializer(product)
        return Response(product_serializer.data)
    def put(self,request,pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def category_list(request):

    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


