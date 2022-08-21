from .models import AttributeName, Attribute, AttributeValue, Catalog
from .models import Image, ProductAttributes, ProductImage, Product

from .serializers import AttributeNameSerializer, AttributeSerializer, AttributeValueSerializer
from .serializers import CatalogSerializer, ImageSerializer, ProductAttributesSerializer
from .serializers import ProductImageSerializer, ProductSerializer


def select_obj(name: str):
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


def serialize(name: str, que):
    '''Returns serialized data for specified object Name and QuerySet'''
    if name == "AttributeName":
        return AttributeNameSerializer(que, many=True)
    if name == 'AttributeValue':
        return AttributeValueSerializer(que, many=True)
    if name == 'Attribute':
        return AttributeSerializer(que, many=True)
    if name == 'Product':
        return ProductSerializer(que, many=True)
    if name == 'Image':
        return ImageSerializer(que, many=True)
    if name == 'Catalog':
        return CatalogSerializer(que, many=True)
    if name == 'ProductImage':
        return ProductImageSerializer(que, many=True)
    if name == 'ProductAttributes':
        return ProductAttributesSerializer(que, many=True)
    return None
