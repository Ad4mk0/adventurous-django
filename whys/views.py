from django.http import JsonResponse
from .utils import select_obj, serialize

from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import AttributeNameSerializer, AttributeSerializer, AttributeValueSerializer
from .serializers import CatalogSerializer, ImageSerializer, ProductAttributesSerializer
from .serializers import ProductImageSerializer, ProductSerializer

from sys import modules


@api_view(['POST'])
def parser(request):
    '''Loads all the data into apropriate models'''
    if request.method == 'POST':
        for elem in request.data:
            [key] = elem.keys()
            [vals] = elem.values()
            try:
                serializer = getattr(modules['whys.serializers'], key+"Serializer")(data=vals)
            except:
                return JsonResponse(data="Object to be inserted could not be recognized",
                                    status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                    safe=False)

            if serializer.is_valid():
                serializer.save()

        return JsonResponse(data="Success!",
                            status=status.HTTP_201_CREATED,
                            safe=False)


@api_view(['GET'])
def detail(request, name: str):
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
def close_detail(request, name: str, id: int):
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
