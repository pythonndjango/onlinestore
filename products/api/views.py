from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView


from products.models import Product
from products.api.serializers import ProductSerializer


class ProductListCreateAPIView(APIView):
    def get(self, request):
        pro = Product.objects.filter()
        serializer = ProductSerializer(pro, many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# code get post trong serizlizer gui du lieu len server

class ProductDetailAPIView(APIView):
    def get_object(self,pk):
        pro = get_object_or_404(Product, pk=pk)
        return pro

    def get(self,request,pk):
        pro = self.get_object(pk)
        serializer = ProductSerializer(pro)
        return Response(serializer.data)
    def put(self,request,pk):
        pro = self.get_object(pk)
        serializer = ProductSerializer(pro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                                          

    def delelte(self,request,pk):
        Product = self.get_object(pk)
        Product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)