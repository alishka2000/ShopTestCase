from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from shop.tutorial.quickstart.serializer import ShopSerializer, ProductSerializer, CategorySerializer
import json

from shop.tutorial.quickstart.models import Product, Shop, Category


@permission_classes((permissions.AllowAny,))
class StorageView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(instance=product, many=True)
        return Response({"Product": serializer.data})

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))['Product']
        name = data['name']
        category = data['category_id']
        product = Product(name=name, category=Category.objects.get(id=category))
        product.save()
        return JsonResponse(model_to_dict(product))

    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        data = json.loads(request.body.decode('utf-8'))['Product']
        for i in data:
            if i == 'id':
                temp = data['id']
                product.id = temp
            if i == 'name':
                temp = data['name']
                product.name = temp
            if i == 'category_id':
                temp = data['category_id']
                product.category_id = temp
        product.save()
        return JsonResponse(model_to_dict(product))


@permission_classes((permissions.AllowAny,))
class CategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(instance=category, many=True)
        return Response({"category": serializer.data})

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))['Category']
        name = data['name']

        for i in data:
            if i == 'shop':
                shop = data['shop']
                category = Category(name=name, parent=Category.objects.get(id=shop))
            else:
                category = Category(name=name)

        category.save()
        return JsonResponse(model_to_dict(category))

    def put(self, request, pk):
        category = Category.objects.get(pk=pk)
        data = json.loads(request.body.decode('utf-8'))['Category']
        for i in data:
            if i == 'name':
                name = data['name']
                category.name = name
            if i == 'shop':
                shop = data['shop']
                category.shop = shop
        category.save()
        return JsonResponse(model_to_dict(category))

