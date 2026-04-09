from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import ProductSerializer
from .services import ProductService


@api_view(['GET'])
def product_list(request):
    products = ProductService.list_products()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_detail(request, pk):
    product = ProductService.get_product(pk)
    if not product:
        return Response({"error": "Not found"}, status=404)

    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['POST'])
def product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        product = ProductService.create_product(serializer.validated_data)
        return Response(ProductSerializer(product).data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def product_update(request, pk):
    product = ProductService.get_product(pk)
    if not product:
        return Response({"error": "Not found"}, status=404)

    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        product = ProductService.update_product(product, serializer.validated_data)
        return Response(ProductSerializer(product).data)

    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def product_delete(request, pk):
    product = ProductService.get_product(pk)
    if not product:
        return Response({"error": "Not found"}, status=404)

    ProductService.delete_product(product)
    return Response(status=204)