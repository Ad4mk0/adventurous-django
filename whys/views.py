from django.http import JsonResponse
# from rest_framework.response import Response

from .models import AttributeName, Attribute, AttributeValue, Catalog
from .models import Image, ProductAttributes, ProductImage, Product

from .serializers import AttributeNameSerializer, AttributeSerializer, AttributeValueSerializer
from .serializers import CatalogSerializer, ImageSerializer, ProductAttributesSerializer
from .serializers import ProductImageSerializer, ProductSerializer

from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['POST'])
def parser(request):
    '''Loads all the data into apropriate models'''
    if request.method == 'POST':
        for elem in request.data:
            [key]=elem.keys()
            [vals]= elem.values()
    
            if key == 'AttributeName':
                serializer = AttributeNameSerializer(data=vals)
            elif key == 'AttributeValue':
                serializer = AttributeValueSerializer(data=vals)
            elif key == 'Attribute':
                serializer = AttributeSerializer(data=vals)
            elif key == 'Product':
                serializer = ProductSerializer(data=vals)
            elif key == 'Image':
                serializer = ImageSerializer(data=vals)
            elif key == 'Catalog':
                serializer = CatalogSerializer(data=vals)
            elif key == 'ProductImage':
                serializer = ProductImageSerializer(data=vals)
            elif key == 'ProductAttributes':
                serializer = ProductAttributesSerializer(data=vals)
            else:
                return JsonResponse(data="Object to be inserted could not be recognized", 
                                    status=status.HTTP_422_UNPROCESSABLE_ENTITY, 
                                    safe=False)

            if serializer.is_valid():
                serializer.save()
            # else:
            #     print(">>>>>>>", key)
        return JsonResponse(data="Success!", 
                            status=status.HTTP_201_CREATED, 
                            safe=False)


@api_view(['GET'])
def detail(request, name:str):
    '''Returns JsonResponse with QuerySet of specified Object name'''
    if request.method == 'GET':
        obj = select_obj(name)
        if obj == None:
            return JsonResponse(data="Requested Object does not exist", 
                                status=status.HTTP_404_NOT_FOUND, 
                                safe=False)  
        que = obj.objects.all()

        serializer = serialize(name, que)

        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def close_detail(request, name:str, id:int):
    '''Returns JsonResponse with QuerySet of specified Object name and id'''
    # QuerySet to vracia aj preto, ze 'id' som nepovazoval za primary_key, 
    # z dovodu ze sa pre jednotlive objekty v test_data.json opakuje,
    # napr. mame Image s id=3 je tam 2x
    if request.method == 'GET': 
        obj = select_obj(name)
        if obj == None:
            return JsonResponse(data="Requested Object does not exist",
                                status=status.HTTP_404_NOT_FOUND, 
                                safe=False)

        que = obj.objects.filter(id=id)
        serializer = serialize(name, que)

        return JsonResponse(serializer.data, safe=False)


def select_obj(name:str):
    '''Returns Object for specified request'''
    # vyuzitie dict by skazilo citatelnost
    if name == "AttributeName":
        return AttributeName
    if name == 'AttributeValue':
        return AttributeValue
    if name == 'Attribute':
        return Attribute
    if name == 'Product':
        return Product
    if name == 'Image':
        return Image
    if name == 'Catalog':
        return Catalog
    if name == 'ProductImage':
        return ProductImage
    if name == 'ProductAttributes':
        return ProductAttributes
    return None

def serialize(name:str, que):
    '''Returns serialized data for specified object Name and QuerySet'''
    if name == "AttributeName":
        return AttributeNameSerializer(que, many = True)
    if name == 'AttributeValue':
        return AttributeValueSerializer(que, many = True)
    if name == 'Attribute':
        return AttributeSerializer(que, many = True)
    if name == 'Product':
        return ProductSerializer(que, many = True)
    if name == 'Image':
        return ImageSerializer(que, many = True)
    if name == 'Catalog':
        return CatalogSerializer(que, many = True)
    if name == 'ProductImage':
        return ProductImageSerializer(que, many = True)
    if name == 'ProductAttributes':
        return ProductAttributesSerializer(que, many = True)
    return None
