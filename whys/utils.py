from sys import modules

def select_obj(name: str):
    '''Returns Object for specified request'''
    try:
        return getattr(modules['whys.models'], name)
    except:
        return None



def serialize(name: str, que):
    '''Returns serialized data for specified object Name and QuerySet'''
    try:
        return getattr(modules['whys.serializers'], name+"Serializer")(que, many=True)
    except:
        return None
