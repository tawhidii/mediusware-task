from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Product,ProductVariantPrice
from .serializers import ProductModelSerializer

class ProductCreateView(APIView):
    
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductModelSerializer(products,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        serializer = ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response({'message':'Successfully Created Product !'})
        return Response(serializer.errors)